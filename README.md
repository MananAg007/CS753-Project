# CS753-Project 

## Team Asriel README 

### Hacker and Poster 
### Submitted by : Adarsh (19D180003), Manan (190050065), Shreya (190050050)



##### Poster Paper : GenerSpeech
##### Hacker Paper : VisualVoice 


* The poster is added in the root folder of the repository.

* Download the python Notebook and run it step by step to get a working model of the code.

* Two parts in the setup :
    - Version Matching for proper Execution -> Done in the .ipynb notebook
    - VoxCeleb2 Dataset Extraction and PreProcessing 

* Features implemented : 
    - Dataset extraction after making a split on the unseen_unheard_test set (20G mp4+mp3, 20G mouth_rois)
        - Refer to the .ipynb file for this
        - Extracted mouth_rois, added code to extract selected ids to save disk space 
        - Added code to extract mp4(video) and m4a (audio) data from VoxCeleb2 for same ids
    - Data processing and mapping for the correct tree structure as in the paper 
        - Refer to the .ipynb file for this
        - Added code to restructure the dataset directory as per the code changes
        - Added code to modify the hdf5 files after making the split in the existing dataset 
    - Added scripts to enable evaluation and testing on a number of mixture samples in one go
        - Refer to files within Evaluation Script directory
        - Usage : 
                python multi_test.py --test_count <value> --testset_root <root dir of data> --testset_type <data split> 
                python multi_eval.py --results_dir <directory of test_videos>
        - multi_test.py uses all other arguments from test.py, just replace the first 6 arguments with the above three
        - multi_test.py: Chooses two random videos from data split of the root directory provided to make a synthetic mixture and performs separation. Repeats this process test_count times.
        - multi_eval.py : Evaluates all examples in the test_videos directory and appends results to one eval.txt file in the same directory. Lastly, appends the average values of all the result metrics in the file.
    - Mean Frame Feature of Facial Encodings (Code Changes/audioVisual_dataset.py)
        - Refer from line 173 to line 194 in the mentioned file
        - Instead of choosing one random frame for facial attributes, it chooses <num_frames> frames randomly and passes the average facial frame for further processing.
    - Attempted adding a Self-Attention Layer in the AudioVisual Model (Code Changes/Networks.py)
        - Refer to lines 158-162 and lines 180-187 in the mentioned file.
        - Tried to add a self-attention layer to the audioVisual feature vector.
        - Couldn't present results for this part as while running we figured out there are some issues with the data_loader itself in train.py, because of which we were not able to access the network layers for debugging.
    - Results attached in Evaluation Results directory:
        - eval_50samples.txt : contains results from first run of multi_test and multi_eval on 50 examples
        - eval_100samples_tweak.txt : contains results from run over 100 examples, after changing learning rates and weight of cross_modal loss
        - eval_10frame.txt : Applied random seeding, implemented mean_frame idea with num_frames as 10 for 100 examples
        - eval_1frame.txt : Applied same seeding, implemented the above idea with num_frames as 1 for 100 examples 
        - The last two files do differ at some points (for example, line 1). Do a git diff for more info on differences.
    - Input Samples : Contains separated and example files for two set of samples we tried running the code on, just for completeness and better understanding on how results are processed. 
    - Pending Idea to implement : Tweaking the training algorithm for smarter learning
        

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
        - Self Attention to lip reading over facial attributes
        - Devising a training method to first learn over more distinct speakers in a mixture

    
        