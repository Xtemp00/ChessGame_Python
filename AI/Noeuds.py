from tensorflow import keras
from keras.utils.vis_utils import plot_model
import pydot

# Charger le modèle sauvegardé
model = keras.models.load_model('mon_modele.h5')

# Afficher le graphe du modèle
plot_model(model, to_file='model.png', show_shapes=True, show_layer_names=True)
