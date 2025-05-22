import sys
import os

# Ajoutez le chemin vers le répertoire racine de nnUNet
sys.path.append(os.path.abspath("medical_image_analyzer/nnUNet"))

from nnunetv2.inference.predict import predict_from_folder

def segment_brain_mri(input_folder, output_folder, model_folder):
    predict_from_folder(
        model_folder=model_folder,
        input_folder=input_folder,
        output_folder=output_folder,
        save_probabilities=False,
        disable_postprocessing=False,
        num_threads_preprocessing=1,
        num_threads_nifti_save=1,
        lowres_segmentations=None,
        step_size=0.5,
        checkpoint_name="model_final_checkpoint",
        mode="normal"
    )
    return {"status": "Segmentation terminée", "output": output_folder}