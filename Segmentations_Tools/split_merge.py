import numpy as np
import cv2
import matplotlib.pyplot as plt

# Fonction qui divise récursivement l'image
def split(image, threshold=0.1):
    """Divise l'image en blocs jusqu'à ce qu'ils respectent un seuil de variance"""
    if is_homogeneous(image, threshold):
        return [image]
    
    # Diviser l'image en 4 sous-blocs (haut-gauche, haut-droit, bas-gauche, bas-droit)
    h, w = image.shape
    half_h, half_w = h // 2, w // 2
    
    # Créer les 4 sous-blocs
    top_left = image[:half_h, :half_w]
    top_right = image[:half_h, half_w:]
    bottom_left = image[half_h:, :half_w]
    bottom_right = image[half_h:, half_w:]
    
    # Diviser récursivement chaque sous-bloc
    subregions = []
    subregions.extend(split(top_left, threshold))
    subregions.extend(split(top_right, threshold))
    subregions.extend(split(bottom_left, threshold))
    subregions.extend(split(bottom_right, threshold))
    
    return subregions

def is_homogeneous(region, threshold):
    """Vérifie si la région est homogène en fonction de la variance"""
    return np.var(region) < threshold

def merge(subregions, threshold=0.1):
    """Fusionne les sous-régions adjacentes homogènes"""
    merged_regions = []
    for i in range(len(subregions)):
        if i == len(subregions) - 1:
            merged_regions.append(subregions[i])
            continue
        
        # Comparer la variance des régions voisines
        region1 = subregions[i]
        region2 = subregions[i + 1]
        
        # Si les deux régions sont homogènes, on peut les fusionner
        if np.var(region1) < threshold and np.var(region2) < threshold:
            merged_regions.append(region1 + region2)
        else:
            merged_regions.append(region1)
    return merged_regions

# Fonction principale
def split_merge_segmentation(image, threshold=0.1):
    """Application de la segmentation par split/merge descendante sur une image binaire"""
    # Diviser l'image
    subregions = split(image, threshold)
    
    # Fusionner les sous-régions homogènes
    merged_regions = merge(subregions, threshold)
    
    return merged_regions

# Exemple d'utilisation
if __name__ == "__main__":
    # Charger une image binaire (0 ou 255)
    image = cv2.imread('image_binaire.png', cv2.IMREAD_GRAYSCALE)
    if image is None:
        print("Erreur: l'image n'a pas été trouvée.")
    else:
        # Appliquer la segmentation
        segmented_image = split_merge_segmentation(image)
        
        # Afficher les résultats
        plt.imshow(segmented_image, cmap='gray')
        plt.show()

