import sys
import os
import numpy as np
import SimpleITK as ST
import utils as ut
import cPickle as pickle
import scipy.io as sio


root_dir='./dicom_data'
type = 'airway'

if __name__ == '__main__' :
    origin_datas = ut.get_original_arrays(root_dir,type)
    data_pairs = ut.organize_data_pairs(origin_datas)
    # pickle_writer = open('./data_pairs.pkl','wb')
    # pickle.dump(data_pairs,pickle_writer)
    # pickle_writer.close()
    # maxs = ut.get_proper_range(data_pairs)
    # print maxs
    print data_pairs.keys()
    # ut.out_put_data_pairs(data_pairs)
