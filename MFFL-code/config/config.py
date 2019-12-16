config = {}

training_opt = {}

training_opt['feature_dim'] = 200
training_opt['open_threshold'] = 0.1
training_opt['scheduler_params'] = {'step_size': 500, 'gamma': 0.1}
training_opt['label_smoothing_epsilon'] = 0.1
training_opt['add_inverse_relation'] = True
training_opt['grad_norm'] = 5
config['training_opt'] = training_opt

networks = {}

feature_param = {'entity_dim': 200, 'emb_2D_d1': 10, 'emb_2D_d2': 20, 'relation_dim': 200,
                 'num_out_channels': 32, 'hidden_dropout_rate': 0.3,'kernel_size': 3,
                 'feat_dropout_rate': 0.2, 'emb_dropout_rate': 0.3}
networks['emb_model'] = {'def_file': './models/Score_aware_model.py',
                          'params': feature_param}

classifier_param = {'in_dim': 200, 'entity_dim': 200, 'relation_dim': 200}

networks['relation_aware_model'] = {'def_file': './models/Relation_aware_model.py',
                          'params': classifier_param}
config['networks'] = networks

criterions = {}
criterions['Score_Aware_Loss'] = {'def_file': './loss/Score_Aware_Loss.py', 'weight': 1}

criterions['Relation_Aware_Loss'] = {'def_file': './loss/Relation_Aware_Loss.py', 'weight': 0.01}

config['criterions'] = criterions

