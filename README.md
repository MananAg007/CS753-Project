# CS753-Project 

## Team Asriel README 

### Hacker and Poster 
### Submitted by : Adarsh (19D180003), Manan (190050065), Shreya (190050050)



##### Poster Paper : GenerSpeech
##### Hacker Paper : VisualVoice 


* The poster is added in the root folder of the repository.

* Download the python Notebook and run it step by step to get a working model of the code.

* Two parts in the setup :
    - Version Matching for proper Execution
    - VoxCeleb2 Dataset Extraction and PreProcessing 

* Features implemented : 
    - Dataset extraction after making a split on the unseen_unheard_test set (20G mp4+mp3, 20G mouth_rois)
    - Data processing and mapping for the correct tree structure as in the paper 
    - Added scripts to enable evaluation and testing on a number of mixture samples in one go
    - Mean Frame Feature of Facial Encodings (data/audioVisual_dataset.py)
    - Attempted adding a Self-Attention Layer in the AudioVisual Model (model/Networks.py)
    - Pending Idea : Tweaking the training algorithm for smarter learning

* Challenges Faced :
    - VoxCeleb2 is not readily available online as it used to be 
    - Dataset splitting and modifying hdf5 files
    - Strict Version Matching (didn't expect it in the first go)
    - Google Colab Limitations (Disk Usage too high to store locally, Compute Units limited)
    - Paper lacked enough information about the coding setup and most of available info is outdated now
    - Self Attention Layer hindered by DataLoader issues: heavy-duty debugging
    - Most of the weights and models are pretrained with little room for major implementation changes

* Learning and Future Scope:
    - Subtle and interesting designs are not always easy to replicate
    - From an exploratory perspective, an interesting challenge
    - If the training pipeline's dataloader issues are resolved, there's room for development
        -> Self Attention to lip reading over facial attributes
        -> Devising a training method to first learn over more distinct speakers in a mixture

    
        