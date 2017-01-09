from keras.layers import Dense
from keras.models import Sequential

from preprocessing import preprocess_data

model = Sequential()


def train_net(x, y):
    model.add(Dense(256, input_dim=22, activation='relu', init='normal'))
    # model.add(Dropout(0.2))
    model.add(Dense(128, activation='relu', init='normal'))
    # model.add(Dropout(0.2))
    model.add(Dense(32, activation='relu', init='normal'))
    # model.add(Dropout(0.2))
    model.add(Dense(1, activation='sigmoid', init='normal'))

    model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

    model.fit(x, y, nb_epoch=50, batch_size=10, validation_split=0.15)


features, labels = preprocess_data()
train_net(features, labels)
