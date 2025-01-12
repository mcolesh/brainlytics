import os
import scipy.io

class DataTransformer:
  def __init__(self,modeltype,path_of_session,last_frame):
    """
    modeltype: 'CNN' or 'SVM'
    session_name (example): '13AugA'
    path_of_session (example): "C:/Users/Shaked/Msc/project/SVM/13AugA/condXnoTarget/condXnoTarget"
    """

    self.modeltype = modeltype
    self.session_name = os.path.normpath(path_of_session).split(os.sep)[-3]
    self.path_of_session = path_of_session
    self.last_frame = last_frame
  
  def create (self):
    last_frame = self.last_frame
    mat = scipy.io.loadmat(self.path_of_session)
    Attentd_in = mat['cond4'].T
    Distributed = mat['cond8'].T
    Attend_away = mat['cond1'].T
        
    trials = {}
    trials[4] = Attentd_in[:,:last_frame,:]
    trials[8] = Distributed[:,:last_frame,:]
    trials[1] = Attend_away[:,:last_frame,:]
        
    if self.modeltype =="CNN":
        trials[8] = trials[8].reshape(trials[8].shape[0],trials[8].shape[1],100,100)
        trials[4] = trials[4].reshape(trials[4].shape[0],trials[4].shape[1],100,100)
        trials[1] = trials[1].reshape(trials[1].shape[0],trials[1].shape[1],100,100)
    return (self.session_name,trials)