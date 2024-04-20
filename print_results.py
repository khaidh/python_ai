#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/print_results.py
#                                                                             
# PROGRAMMER: KhaiDH2
# DATE CREATED: 2024/04/19
# REVISED DATE: 
# PURPOSE: Create a function print_results that prints the results statistics
#          from the results statistics dictionary (results_stats_dic). It 
#          should also allow the user to be able to print out cases of misclassified
#          dogs and cases of misclassified breeds of dog using the Results 
#          dictionary (results_dic).  
#         This function inputs:
#            -The results dictionary as results_dic within print_results 
#             function and results for the function call within main.
#            -The results statistics dictionary as results_stats_dic within 
#             print_results function and results_stats for the function call within main.
#            -The CNN model architecture as model within print_results function
#             and in_arg.arch for the function call within main. 
#            -Prints Incorrectly Classified Dogs as print_incorrect_dogs within
#             print_results function and set as either boolean value True or 
#             False in the function call within main (defaults to False)
#            -Prints Incorrectly Classified Breeds as print_incorrect_breed within
#             print_results function and set as either boolean value True or 
#             False in the function call within main (defaults to False)
#         This function does not output anything other than printing a summary
#         of the final results.
##

def print_results(results_dic, results_stats_dic, model,
                  print_incorrect_dogs=False, print_incorrect_breed=False):
    """
    Prints summary results on the classification and then prints incorrectly 
    classified dogs and incorrectly classified dog breeds if user indicates 
    they want those printouts (use non-default values)
    Parameters:
      results_dic: - Dictionary with key as image filename and value as a List
             (index)idx 0 = pet image label (string)
                    idx 1 = classifier label (string)
                    idx 2 = 1/0 (int)  where 1 = match between pet image and 
                            classifier labels and 0 = no match between labels
                    idx 3 = 1/0 (int)  where 1 = pet image 'is-a' dog and 
                            0 = pet Image 'is-NOT-a' dog. 
                    idx 4 = 1/0 (int)  where 1 = Classifier classifies image 
                            'as-a' dog and 0 = Classifier classifies image  
                            'as-NOT-a' dog.
      results_stats_dic: - Dictionary that contains the results statistics (either
                   a  percentage or a count) where the key is the statistic's 
                     name (starting with 'pct' for percentage or 'n' for count)
                     and the value is the statistic's value 
      model: - Indicates which CNN model architecture will be used by the
              classifier function to classify the pet images,
              values must be either: resnet alexnet vgg (string)
      print_incorrect_dogs: - True prints incorrectly classified dog images and
                             False doesn't print anything(default) (bool)  
      print_incorrect_breed: - True prints incorrectly classified dog breeds and
                              False doesn't print anything(default) (bool) 
    Returns:
           None - simply printing results.
    """

    # Prints summary statistics over the run
    print("\n\n*** Results Summary for CNN Model Architecture", model.upper(), "***")
    for key in results_stats_dic:
        if key.startswith('n'):
            print("{:20}: {:3f}".format(key, results_stats_dic[key]))

    print("\n\n*** Summary statistics (percentages) on Model Run", model.upper(), "***")
    for key in results_stats_dic:
        if key.startswith('pct'):
            print("{:20}: {:3f}".format(key, results_stats_dic[key]))

    # IF print_incorrect_dogs == True AND there were images incorrectly
    # classified as dogs or vice versa - print out these cases
    if (print_incorrect_dogs and
            ((results_stats_dic['n_correct_dogs'] + results_stats_dic['n_correct_notdogs'])
             != results_stats_dic['n_images'])
    ):
        print("\nINCORRECT Dog/NOT Dog Assignments:")
        for key in results_dic:
            value = results_dic[key]
            if value[2] == 1 and value[3] == 0:
                print("\t{:>26}: Pet image label is A-DOG     - Classified as NOT-A-DOG".format(key))

            if value[2] == 0 and value[4] == 1:
                print("\t{:>26}: Pet image label is NOT-A-DOG - Classified as A-DOG".format(key))

    # IF print_incorrect_breed == True AND there were dogs whose breeds
    # were incorrectly classified - print out these cases
    if (
            print_incorrect_breed
            and (results_stats_dic['n_correct_dogs'] != results_stats_dic['n_correct_breed'])
    ):
        print("\nINCORRECT Dog Breed Assignment:")

        # process through results dict, printing incorrectly classified breeds
        # results_dic item: key => [[0]image_label, [1]model_label, [2]match, [3]image_label_dog, [4]model_label_dog]
        for key in results_dic:
            value = results_dic[key]
            if value[3] == 1 and value[4] == 1 and value[2] == 0:
                print("Real: {:>26}   Classifier: {:>30}".format(value[0], value[1]))
