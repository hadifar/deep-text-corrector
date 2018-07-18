# -*- coding: utf-8 -*-
#
# Copyright 2018 Amir Hadifar. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================
from sklearn.model_selection import train_test_split

with open('../preprocessed_movie_lines.txt', 'r') as inputfile, \
        open('../movie_dialog_train.txt', 'w+') as trainfile, \
        open('../movie_dialog_test.txt', 'w+') as testfile, \
        open('../movie_dialog_val.txt', 'w+') as validfile:
    all_lines = inputfile.readlines()

    train_x, test_x = train_test_split(all_lines, test_size=0.2, random_state=1)
    test_x, valid_x = train_test_split(test_x, test_size=0.5, random_state=1)

    for line in train_x:
        trainfile.write(line)

    for line in test_x:
        testfile.write(line)

    for line in valid_x:
        validfile.write(line)
