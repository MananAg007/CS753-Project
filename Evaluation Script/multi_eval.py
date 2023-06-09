#!/usr/bin/env python

# Copyright (c) Facebook, Inc. and its affiliates.
# All rights reserved.
#
# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.

# https://github.com/vBaiCai/python-pesq
# https://github.com/mpariente/pystoi

import os
import librosa
import argparse
import numpy as np
import mir_eval.separation
import time 
from pypesq import pesq
from pystoi import stoi

def getSeparationMetrics(audio1, audio2, audio1_gt, audio2_gt):
    reference_sources = np.concatenate((np.expand_dims(audio1_gt, axis=0), np.expand_dims(audio2_gt, axis=0)), axis=0)
    estimated_sources = np.concatenate((np.expand_dims(audio1, axis=0), np.expand_dims(audio2, axis=0)), axis=0)
    (sdr, sir, sar, perm) = mir_eval.separation.bss_eval_sources(reference_sources, estimated_sources, False)
    #print(sdr, sir, sar, perm)
    return np.mean(sdr), np.mean(sir), np.mean(sar)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--results_dir', type=str, required=True)
    parser.add_argument('--audio_sampling_rate', type=int, default=16000)
    args = parser.parse_args()

    dirs = os.listdir(args.results_dir)
    test_results = []
    for dir in dirs :
      if(dir[:2] == "id") :
        test_results.append(dir)

    metrics = [[], [], [], [], [], [], []]


    i = 0
    for result in test_results:
        print(i)
        i = i + 1 
        audio1, _ = librosa.load(os.path.join(args.results_dir + "/" + result, 'audio1_separated.wav'), sr=args.audio_sampling_rate)
        audio2, _ = librosa.load(os.path.join(args.results_dir + "/" + result, 'audio2_separated.wav'), sr=args.audio_sampling_rate)
        audio1_gt, _ = librosa.load(os.path.join(args.results_dir + "/" + result, 'audio1.wav'), sr=args.audio_sampling_rate)
        audio2_gt, _ = librosa.load(os.path.join(args.results_dir + "/" + result, 'audio2.wav'), sr=args.audio_sampling_rate)
        audio_mix, _ = librosa.load(os.path.join(args.results_dir + "/" + result, 'audio_mixed.wav'), sr=args.audio_sampling_rate)

        # SDR, SIR, SAR
        sdr, sir, sar = getSeparationMetrics(audio1, audio2, audio1_gt, audio2_gt)
        sdr_mixed, _, _ = getSeparationMetrics(audio_mix, audio_mix, audio1_gt, audio2_gt)

        # PESQ 
        pesq_score1 = pesq(audio1, audio1_gt, args.audio_sampling_rate)
        pesq_score2 = pesq(audio2, audio2_gt, args.audio_sampling_rate)
        pesq_score = (pesq_score1 + pesq_score2) / 2

        # STOI
        stoi_score1 = stoi(audio1_gt, audio1, args.audio_sampling_rate, extended=False)
        stoi_score2 = stoi(audio2_gt, audio2, args.audio_sampling_rate, extended=False)
        stoi_score = (stoi_score1 + stoi_score2) / 2

        output_file = open(os.path.join(args.results_dir, 'eval.txt'),'a')
        output_file.write("%3f %3f %3f %3f %3f %3f %3f\n" % (sdr, sdr_mixed, sdr - sdr_mixed, sir, sar, pesq_score, stoi_score))
        output_file.close()

        metrics[0].append(sdr)
        metrics[1].append(sdr_mixed)
        metrics[2].append(sdr - sdr_mixed)
        metrics[3].append(sir)
        metrics[4].append(sar)
        metrics[5].append(pesq_score)
        metrics[6].append(stoi_score)

    metrics = [sum(metric) / len(metric) for metric in metrics]
    output_file = open(os.path.join(args.results_dir, 'eval.txt'),'a')
    output_file.write("sdr: %3f\nsdr_mixed: %3f\nsdr - sdr_mixed: %3f\nsir: %3f\nsar: %3f\npesq_score: %3f\nstoi_score: %3f\n" % (metrics[0], metrics[1], metrics[2], metrics[3], metrics[4], metrics[5], metrics[6]))
    output_file.close()

if __name__ == '__main__':
    main()