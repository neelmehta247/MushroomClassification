def preprocess_data():
    with open('mushrooms.csv') as input_file:
        labels = []
        features = []

        for x in input_file.readlines()[1:]:
            split_line = x.split(',')

            if split_line[0] == 'p':
                labels.append(1)
            else:
                labels.append(0)

            row_features = []

            for feature in split_line[1:]:
                if feature == '?':
                    row_features.append(0)
                elif feature.endswith('\n'):
                    row_features.append((ord(feature[0]) - 96.0) / 26)
                else:
                    row_features.append((ord(feature) - 96.0) / 26)

            features.append(row_features)

    return features, labels


def train_test(features, labels, ratio):
    features_train, features_test, labels_train, labels_test = [], [], [], []

    for i in range(len(features)):

        if ((i * 1.0) / len(features)) > ratio:
            features_train.append(features[i])
            labels_train.append(labels[i])
        else:
            features_test.append(features[i])
            labels_test.append(labels)

    return features_train, features_test, labels_train, labels_test

