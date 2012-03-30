# This file was created automatically by SWIG 1.3.29.
# Don't modify this file, modify the SWIG interface instead.
# This file is compatible with both classic and new-style classes.

import _lsf
import new
new_instancemethod = new.instancemethod
def _swig_setattr_nondynamic(self,class_type,name,value,static=1):
    if (name == "thisown"): return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'PySwigObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    if (not static) or hasattr(self,name):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)

def _swig_setattr(self,class_type,name,value):
    return _swig_setattr_nondynamic(self,class_type,name,value,0)

def _swig_getattr(self,class_type,name):
    if (name == "thisown"): return self.this.own()
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError,name

def _swig_repr(self):
    try: strthis = "proxy of " + self.this.__repr__()
    except: strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

import types
try:
    _object = types.ObjectType
    _newclass = 1
except AttributeError:
    class _object : pass
    _newclass = 0
del types


new_intp = _lsf.new_intp
copy_intp = _lsf.copy_intp
delete_intp = _lsf.delete_intp
intp_assign = _lsf.intp_assign
intp_value = _lsf.intp_value
new_floatp = _lsf.new_floatp
copy_floatp = _lsf.copy_floatp
delete_floatp = _lsf.delete_floatp
floatp_assign = _lsf.floatp_assign
floatp_value = _lsf.floatp_value
PASSWD_FILE_LS = _lsf.PASSWD_FILE_LS
PASSWORD_LEN = _lsf.PASSWORD_LEN
LS_LONG_FORMAT = _lsf.LS_LONG_FORMAT
LS_UNS_LONG_FORMAT = _lsf.LS_UNS_LONG_FORMAT
INVALID_SOCKET = _lsf.INVALID_SOCKET
_VERSION_STR_ = _lsf._VERSION_STR_
_WORKGROUP_STR_ = _lsf._WORKGROUP_STR_
_MINOR_STR_ = _lsf._MINOR_STR_
_BUILD_STR_ = _lsf._BUILD_STR_
_NOTE_STR_ = _lsf._NOTE_STR_
_HOTFIX_STR_ = _lsf._HOTFIX_STR_
_OS_STR_ = _lsf._OS_STR_
LSF_XDR_VERSION2_0 = _lsf.LSF_XDR_VERSION2_0
LSF_XDR_VERSION2_1 = _lsf.LSF_XDR_VERSION2_1
LSF_XDR_VERSION2_2 = _lsf.LSF_XDR_VERSION2_2
LSF_XDR_VERSION3_0 = _lsf.LSF_XDR_VERSION3_0
LSF_XDR_VERSION3_1 = _lsf.LSF_XDR_VERSION3_1
LSF_XDR_VERSION3_2 = _lsf.LSF_XDR_VERSION3_2
LSF_XDR_VERSION3_2_2 = _lsf.LSF_XDR_VERSION3_2_2
LSF_XDR_VERSION4_0 = _lsf.LSF_XDR_VERSION4_0
LSF_XDR_VERSION4_1 = _lsf.LSF_XDR_VERSION4_1
LSF_XDR_VERSION4_2 = _lsf.LSF_XDR_VERSION4_2
LSF_XDR_VERSION5_0 = _lsf.LSF_XDR_VERSION5_0
LSF_XDR_VERSION5_1 = _lsf.LSF_XDR_VERSION5_1
LSF_XDR_VERSION6_0 = _lsf.LSF_XDR_VERSION6_0
LSF_XDR_VERSION6_1 = _lsf.LSF_XDR_VERSION6_1
LSF_XDR_VERSION6_2 = _lsf.LSF_XDR_VERSION6_2
EGO_XDR_VERSION_1_1 = _lsf.EGO_XDR_VERSION_1_1
LSF_XDR_VERSION7_0 = _lsf.LSF_XDR_VERSION7_0
EGO_XDR_VERSION_1_2 = _lsf.EGO_XDR_VERSION_1_2
LSF_XDR_VERSION7_0_EP1 = _lsf.LSF_XDR_VERSION7_0_EP1
LSF_XDR_VERSION7_0_EP2 = _lsf.LSF_XDR_VERSION7_0_EP2
LSF_XDR_VERSION7_0_EP3 = _lsf.LSF_XDR_VERSION7_0_EP3
LSF_XDR_VERSION7_0_EP4 = _lsf.LSF_XDR_VERSION7_0_EP4
LSF_XDR_VERSION7_0_EP5 = _lsf.LSF_XDR_VERSION7_0_EP5
LSF_XDR_VERSION7_0_EP6 = _lsf.LSF_XDR_VERSION7_0_EP6
LSF_XDR_VERSION8_0 = _lsf.LSF_XDR_VERSION8_0
EGO_XDR_VERSION_1_2_2 = _lsf.EGO_XDR_VERSION_1_2_2
EGO_XDR_VERSION_1_2_3 = _lsf.EGO_XDR_VERSION_1_2_3
EGO_XDR_VERSION_1_2_4 = _lsf.EGO_XDR_VERSION_1_2_4
EGO_XDR_VERSION = _lsf.EGO_XDR_VERSION
LSF_DEFAULT_SOCKS = _lsf.LSF_DEFAULT_SOCKS
MAXLINELEN = _lsf.MAXLINELEN
MAXLSFNAMELEN = _lsf.MAXLSFNAMELEN
MAXLSFNAMELEN_70_EP1 = _lsf.MAXLSFNAMELEN_70_EP1
MAXSRES = _lsf.MAXSRES
MAXRESDESLEN = _lsf.MAXRESDESLEN
NBUILTINDEX = _lsf.NBUILTINDEX
MAXTYPES = _lsf.MAXTYPES
MAXMODELS = _lsf.MAXMODELS
MAXMODELS_70 = _lsf.MAXMODELS_70
MAXTYPES_31 = _lsf.MAXTYPES_31
MAXMODELS_31 = _lsf.MAXMODELS_31
MAXFILENAMELEN = _lsf.MAXFILENAMELEN
MAXEVARS = _lsf.MAXEVARS
GENMALLOCPACE = _lsf.GENMALLOCPACE
MAXLOGCLASSLEN = _lsf.MAXLOGCLASSLEN
FIRST_RES_SOCK = _lsf.FIRST_RES_SOCK
R15S = _lsf.R15S
R1M = _lsf.R1M
R15M = _lsf.R15M
UT = _lsf.UT
PG = _lsf.PG
IO = _lsf.IO
LS = _lsf.LS
IT = _lsf.IT
TMP = _lsf.TMP
SWP = _lsf.SWP
MEM = _lsf.MEM
USR1 = _lsf.USR1
USR2 = _lsf.USR2
INFINIT_INT = _lsf.INFINIT_INT
INFINIT_LONG_INT = _lsf.INFINIT_LONG_INT
INFINIT_SHORT = _lsf.INFINIT_SHORT
DEFAULT_RLIMIT = _lsf.DEFAULT_RLIMIT
LSF_RLIMIT_CPU = _lsf.LSF_RLIMIT_CPU
LSF_RLIMIT_FSIZE = _lsf.LSF_RLIMIT_FSIZE
LSF_RLIMIT_DATA = _lsf.LSF_RLIMIT_DATA
LSF_RLIMIT_STACK = _lsf.LSF_RLIMIT_STACK
LSF_RLIMIT_CORE = _lsf.LSF_RLIMIT_CORE
LSF_RLIMIT_RSS = _lsf.LSF_RLIMIT_RSS
LSF_RLIMIT_NOFILE = _lsf.LSF_RLIMIT_NOFILE
LSF_RLIMIT_OPEN_MAX = _lsf.LSF_RLIMIT_OPEN_MAX
LSF_RLIMIT_VMEM = _lsf.LSF_RLIMIT_VMEM
LSF_RLIMIT_SWAP = _lsf.LSF_RLIMIT_SWAP
LSF_RLIMIT_RUN = _lsf.LSF_RLIMIT_RUN
LSF_RLIMIT_PROCESS = _lsf.LSF_RLIMIT_PROCESS
LSF_RLIMIT_THREAD = _lsf.LSF_RLIMIT_THREAD
LSF_RLIM_NLIMITS = _lsf.LSF_RLIM_NLIMITS
LSF_RLIM_NLIMITS5_1 = _lsf.LSF_RLIM_NLIMITS5_1
LSF_NULL_MODE = _lsf.LSF_NULL_MODE
LSF_LOCAL_MODE = _lsf.LSF_LOCAL_MODE
LSF_REMOTE_MODE = _lsf.LSF_REMOTE_MODE
RF_MAXHOSTS = _lsf.RF_MAXHOSTS
RF_CMD_MAXHOSTS = _lsf.RF_CMD_MAXHOSTS
RF_CMD_RXFLAGS = _lsf.RF_CMD_RXFLAGS
STATUS_TIMEOUT = _lsf.STATUS_TIMEOUT
STATUS_IOERR = _lsf.STATUS_IOERR
STATUS_EXCESS = _lsf.STATUS_EXCESS
STATUS_REX_NOMEM = _lsf.STATUS_REX_NOMEM
STATUS_REX_FATAL = _lsf.STATUS_REX_FATAL
STATUS_REX_CWD = _lsf.STATUS_REX_CWD
STATUS_REX_PTY = _lsf.STATUS_REX_PTY
STATUS_REX_SP = _lsf.STATUS_REX_SP
STATUS_REX_FORK = _lsf.STATUS_REX_FORK
STATUS_REX_AFS = _lsf.STATUS_REX_AFS
STATUS_REX_UNKNOWN = _lsf.STATUS_REX_UNKNOWN
STATUS_REX_NOVCL = _lsf.STATUS_REX_NOVCL
STATUS_REX_NOSYM = _lsf.STATUS_REX_NOSYM
STATUS_REX_VCL_INIT = _lsf.STATUS_REX_VCL_INIT
STATUS_REX_VCL_SPAWN = _lsf.STATUS_REX_VCL_SPAWN
STATUS_REX_EXEC = _lsf.STATUS_REX_EXEC
STATUS_REX_MLS_INVAL = _lsf.STATUS_REX_MLS_INVAL
STATUS_REX_MLS_CLEAR = _lsf.STATUS_REX_MLS_CLEAR
STATUS_REX_MLS_RHOST = _lsf.STATUS_REX_MLS_RHOST
STATUS_REX_MLS_DOMIN = _lsf.STATUS_REX_MLS_DOMIN
STATUS_DENIED = _lsf.STATUS_DENIED
REXF_USEPTY = _lsf.REXF_USEPTY
REXF_CLNTDIR = _lsf.REXF_CLNTDIR
REXF_TASKPORT = _lsf.REXF_TASKPORT
REXF_SHMODE = _lsf.REXF_SHMODE
REXF_TASKINFO = _lsf.REXF_TASKINFO
REXF_REQVCL = _lsf.REXF_REQVCL
REXF_SYNCNIOS = _lsf.REXF_SYNCNIOS
REXF_TTYASYNC = _lsf.REXF_TTYASYNC
REXF_STDERR = _lsf.REXF_STDERR
REXF_UNLINK_CHILD = _lsf.REXF_UNLINK_CHILD
REXF_DELETE_CHILD = _lsf.REXF_DELETE_CHILD
REXF_WRITE_ACCT = _lsf.REXF_WRITE_ACCT
EXACT = _lsf.EXACT
OK_ONLY = _lsf.OK_ONLY
NORMALIZE = _lsf.NORMALIZE
LOCALITY = _lsf.LOCALITY
IGNORE_RES = _lsf.IGNORE_RES
LOCAL_ONLY = _lsf.LOCAL_ONLY
DFT_FROMTYPE = _lsf.DFT_FROMTYPE
ALL_CLUSTERS = _lsf.ALL_CLUSTERS
EFFECTIVE = _lsf.EFFECTIVE
RECV_FROM_CLUSTERS = _lsf.RECV_FROM_CLUSTERS
NEED_MY_CLUSTER_NAME = _lsf.NEED_MY_CLUSTER_NAME
SEND_TO_CLUSTERS = _lsf.SEND_TO_CLUSTERS
NO_SORT = _lsf.NO_SORT
EXCLUSIVE_RESOURCE = _lsf.EXCLUSIVE_RESOURCE
DT_CLUSTER_LOAD = _lsf.DT_CLUSTER_LOAD
INCLUDE_EXPIRED = _lsf.INCLUDE_EXPIRED
FROM_MASTER = _lsf.FROM_MASTER
KEEPUID = _lsf.KEEPUID
RES_CMD_REBOOT = _lsf.RES_CMD_REBOOT
RES_CMD_SHUTDOWN = _lsf.RES_CMD_SHUTDOWN
RES_CMD_LOGON = _lsf.RES_CMD_LOGON
RES_CMD_LOGOFF = _lsf.RES_CMD_LOGOFF
LIM_CMD_REBOOT = _lsf.LIM_CMD_REBOOT
LIM_CMD_SHUTDOWN = _lsf.LIM_CMD_SHUTDOWN
LIM_CMD_REMOVEHOST = _lsf.LIM_CMD_REMOVEHOST
LIM_CMD_ACTIVATE = _lsf.LIM_CMD_ACTIVATE
LIM_CMD_DEACTIVATE = _lsf.LIM_CMD_DEACTIVATE
LIM_CMD_ELIM_ENV = _lsf.LIM_CMD_ELIM_ENV
class connectEnt(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, connectEnt, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, connectEnt, name)
    __repr__ = _swig_repr
    __swig_setmethods__["hostname"] = _lsf.connectEnt_hostname_set
    __swig_getmethods__["hostname"] = _lsf.connectEnt_hostname_get
    if _newclass:hostname = property(_lsf.connectEnt_hostname_get, _lsf.connectEnt_hostname_set)
    __swig_setmethods__["csock"] = _lsf.connectEnt_csock_set
    __swig_getmethods__["csock"] = _lsf.connectEnt_csock_get
    if _newclass:csock = property(_lsf.connectEnt_csock_get, _lsf.connectEnt_csock_set)
    def __init__(self, *args): 
        this = _lsf.new_connectEnt(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _lsf.delete_connectEnt
    __del__ = lambda self : None;
connectEnt_swigregister = _lsf.connectEnt_swigregister
connectEnt_swigregister(connectEnt)
cvar = _lsf.cvar

INTEGER_BITS = _lsf.INTEGER_BITS
LIM_UNAVAIL = _lsf.LIM_UNAVAIL
LIM_LOCKEDU = _lsf.LIM_LOCKEDU
LIM_LOCKEDW = _lsf.LIM_LOCKEDW
LIM_BUSY = _lsf.LIM_BUSY
LIM_RESDOWN = _lsf.LIM_RESDOWN
LIM_UNLICENSED = _lsf.LIM_UNLICENSED
LIM_SBDDOWN = _lsf.LIM_SBDDOWN
LIM_LOCKEDM = _lsf.LIM_LOCKEDM
LIM_OK_MASK = _lsf.LIM_OK_MASK
LIM_PEMDOWN = _lsf.LIM_PEMDOWN
LIM_EXPIRED = _lsf.LIM_EXPIRED
LIM_LOCKEDU_RMS = _lsf.LIM_LOCKEDU_RMS
class placeInfo(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, placeInfo, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, placeInfo, name)
    __repr__ = _swig_repr
    __swig_setmethods__["hostName"] = _lsf.placeInfo_hostName_set
    __swig_getmethods__["hostName"] = _lsf.placeInfo_hostName_get
    if _newclass:hostName = property(_lsf.placeInfo_hostName_get, _lsf.placeInfo_hostName_set)
    __swig_setmethods__["numtask"] = _lsf.placeInfo_numtask_set
    __swig_getmethods__["numtask"] = _lsf.placeInfo_numtask_get
    if _newclass:numtask = property(_lsf.placeInfo_numtask_get, _lsf.placeInfo_numtask_set)
    def __init__(self, *args): 
        this = _lsf.new_placeInfo(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _lsf.delete_placeInfo
    __del__ = lambda self : None;
placeInfo_swigregister = _lsf.placeInfo_swigregister
placeInfo_swigregister(placeInfo)

class hostLoad(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, hostLoad, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, hostLoad, name)
    __repr__ = _swig_repr
    __swig_setmethods__["hostName"] = _lsf.hostLoad_hostName_set
    __swig_getmethods__["hostName"] = _lsf.hostLoad_hostName_get
    if _newclass:hostName = property(_lsf.hostLoad_hostName_get, _lsf.hostLoad_hostName_set)
    __swig_setmethods__["status"] = _lsf.hostLoad_status_set
    __swig_getmethods__["status"] = _lsf.hostLoad_status_get
    if _newclass:status = property(_lsf.hostLoad_status_get, _lsf.hostLoad_status_set)
    __swig_setmethods__["li"] = _lsf.hostLoad_li_set
    __swig_getmethods__["li"] = _lsf.hostLoad_li_get
    if _newclass:li = property(_lsf.hostLoad_li_get, _lsf.hostLoad_li_set)
    def __init__(self, *args): 
        this = _lsf.new_hostLoad(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _lsf.delete_hostLoad
    __del__ = lambda self : None;
hostLoad_swigregister = _lsf.hostLoad_swigregister
hostLoad_swigregister(hostLoad)

LS_BOOLEAN = _lsf.LS_BOOLEAN
LS_NUMERIC = _lsf.LS_NUMERIC
LS_STRING = _lsf.LS_STRING
LS_EXTERNAL = _lsf.LS_EXTERNAL
INCR = _lsf.INCR
DECR = _lsf.DECR
NA = _lsf.NA
RESF_BUILTIN = _lsf.RESF_BUILTIN
RESF_DYNAMIC = _lsf.RESF_DYNAMIC
RESF_GLOBAL = _lsf.RESF_GLOBAL
RESF_SHARED = _lsf.RESF_SHARED
RESF_LIC = _lsf.RESF_LIC
RESF_EXTERNAL = _lsf.RESF_EXTERNAL
RESF_RELEASE = _lsf.RESF_RELEASE
RESF_DEFINED_IN_RESOURCEMAP = _lsf.RESF_DEFINED_IN_RESOURCEMAP
RESF_NON_CONSUMABLE = _lsf.RESF_NON_CONSUMABLE
RESF_REDEFINABLE = _lsf.RESF_REDEFINABLE
RESF_ESRES = _lsf.RESF_ESRES
class resItem(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, resItem, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, resItem, name)
    __repr__ = _swig_repr
    __swig_setmethods__["name"] = _lsf.resItem_name_set
    __swig_getmethods__["name"] = _lsf.resItem_name_get
    if _newclass:name = property(_lsf.resItem_name_get, _lsf.resItem_name_set)
    __swig_setmethods__["des"] = _lsf.resItem_des_set
    __swig_getmethods__["des"] = _lsf.resItem_des_get
    if _newclass:des = property(_lsf.resItem_des_get, _lsf.resItem_des_set)
    __swig_setmethods__["valueType"] = _lsf.resItem_valueType_set
    __swig_getmethods__["valueType"] = _lsf.resItem_valueType_get
    if _newclass:valueType = property(_lsf.resItem_valueType_get, _lsf.resItem_valueType_set)
    __swig_setmethods__["orderType"] = _lsf.resItem_orderType_set
    __swig_getmethods__["orderType"] = _lsf.resItem_orderType_get
    if _newclass:orderType = property(_lsf.resItem_orderType_get, _lsf.resItem_orderType_set)
    __swig_setmethods__["flags"] = _lsf.resItem_flags_set
    __swig_getmethods__["flags"] = _lsf.resItem_flags_get
    if _newclass:flags = property(_lsf.resItem_flags_get, _lsf.resItem_flags_set)
    __swig_setmethods__["interval"] = _lsf.resItem_interval_set
    __swig_getmethods__["interval"] = _lsf.resItem_interval_get
    if _newclass:interval = property(_lsf.resItem_interval_get, _lsf.resItem_interval_set)
    def __init__(self, *args): 
        this = _lsf.new_resItem(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _lsf.delete_resItem
    __del__ = lambda self : None;
resItem_swigregister = _lsf.resItem_swigregister
resItem_swigregister(resItem)

class lsInfo(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, lsInfo, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, lsInfo, name)
    __repr__ = _swig_repr
    __swig_setmethods__["nRes"] = _lsf.lsInfo_nRes_set
    __swig_getmethods__["nRes"] = _lsf.lsInfo_nRes_get
    if _newclass:nRes = property(_lsf.lsInfo_nRes_get, _lsf.lsInfo_nRes_set)
    __swig_setmethods__["resTable"] = _lsf.lsInfo_resTable_set
    __swig_getmethods__["resTable"] = _lsf.lsInfo_resTable_get
    if _newclass:resTable = property(_lsf.lsInfo_resTable_get, _lsf.lsInfo_resTable_set)
    __swig_setmethods__["nTypes"] = _lsf.lsInfo_nTypes_set
    __swig_getmethods__["nTypes"] = _lsf.lsInfo_nTypes_get
    if _newclass:nTypes = property(_lsf.lsInfo_nTypes_get, _lsf.lsInfo_nTypes_set)
    __swig_setmethods__["hostTypes"] = _lsf.lsInfo_hostTypes_set
    __swig_getmethods__["hostTypes"] = _lsf.lsInfo_hostTypes_get
    if _newclass:hostTypes = property(_lsf.lsInfo_hostTypes_get, _lsf.lsInfo_hostTypes_set)
    __swig_setmethods__["nModels"] = _lsf.lsInfo_nModels_set
    __swig_getmethods__["nModels"] = _lsf.lsInfo_nModels_get
    if _newclass:nModels = property(_lsf.lsInfo_nModels_get, _lsf.lsInfo_nModels_set)
    __swig_setmethods__["hostModels"] = _lsf.lsInfo_hostModels_set
    __swig_getmethods__["hostModels"] = _lsf.lsInfo_hostModels_get
    if _newclass:hostModels = property(_lsf.lsInfo_hostModels_get, _lsf.lsInfo_hostModels_set)
    __swig_setmethods__["hostArchs"] = _lsf.lsInfo_hostArchs_set
    __swig_getmethods__["hostArchs"] = _lsf.lsInfo_hostArchs_get
    if _newclass:hostArchs = property(_lsf.lsInfo_hostArchs_get, _lsf.lsInfo_hostArchs_set)
    __swig_setmethods__["modelRefs"] = _lsf.lsInfo_modelRefs_set
    __swig_getmethods__["modelRefs"] = _lsf.lsInfo_modelRefs_get
    if _newclass:modelRefs = property(_lsf.lsInfo_modelRefs_get, _lsf.lsInfo_modelRefs_set)
    __swig_setmethods__["cpuFactor"] = _lsf.lsInfo_cpuFactor_set
    __swig_getmethods__["cpuFactor"] = _lsf.lsInfo_cpuFactor_get
    if _newclass:cpuFactor = property(_lsf.lsInfo_cpuFactor_get, _lsf.lsInfo_cpuFactor_set)
    __swig_setmethods__["numIndx"] = _lsf.lsInfo_numIndx_set
    __swig_getmethods__["numIndx"] = _lsf.lsInfo_numIndx_get
    if _newclass:numIndx = property(_lsf.lsInfo_numIndx_get, _lsf.lsInfo_numIndx_set)
    __swig_setmethods__["numUsrIndx"] = _lsf.lsInfo_numUsrIndx_set
    __swig_getmethods__["numUsrIndx"] = _lsf.lsInfo_numUsrIndx_get
    if _newclass:numUsrIndx = property(_lsf.lsInfo_numUsrIndx_get, _lsf.lsInfo_numUsrIndx_set)
    def __init__(self, *args): 
        this = _lsf.new_lsInfo(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _lsf.delete_lsInfo
    __del__ = lambda self : None;
lsInfo_swigregister = _lsf.lsInfo_swigregister
lsInfo_swigregister(lsInfo)

CLUST_STAT_OK = _lsf.CLUST_STAT_OK
CLUST_STAT_UNAVAIL = _lsf.CLUST_STAT_UNAVAIL
CLUST_STAT_RECV_FROM = _lsf.CLUST_STAT_RECV_FROM
CLUST_STAT_SEND_TO = _lsf.CLUST_STAT_SEND_TO
class clusterInfo(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, clusterInfo, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, clusterInfo, name)
    __repr__ = _swig_repr
    __swig_setmethods__["clusterName"] = _lsf.clusterInfo_clusterName_set
    __swig_getmethods__["clusterName"] = _lsf.clusterInfo_clusterName_get
    if _newclass:clusterName = property(_lsf.clusterInfo_clusterName_get, _lsf.clusterInfo_clusterName_set)
    __swig_setmethods__["status"] = _lsf.clusterInfo_status_set
    __swig_getmethods__["status"] = _lsf.clusterInfo_status_get
    if _newclass:status = property(_lsf.clusterInfo_status_get, _lsf.clusterInfo_status_set)
    __swig_setmethods__["masterName"] = _lsf.clusterInfo_masterName_set
    __swig_getmethods__["masterName"] = _lsf.clusterInfo_masterName_get
    if _newclass:masterName = property(_lsf.clusterInfo_masterName_get, _lsf.clusterInfo_masterName_set)
    __swig_setmethods__["managerName"] = _lsf.clusterInfo_managerName_set
    __swig_getmethods__["managerName"] = _lsf.clusterInfo_managerName_get
    if _newclass:managerName = property(_lsf.clusterInfo_managerName_get, _lsf.clusterInfo_managerName_set)
    __swig_setmethods__["managerId"] = _lsf.clusterInfo_managerId_set
    __swig_getmethods__["managerId"] = _lsf.clusterInfo_managerId_get
    if _newclass:managerId = property(_lsf.clusterInfo_managerId_get, _lsf.clusterInfo_managerId_set)
    __swig_setmethods__["numServers"] = _lsf.clusterInfo_numServers_set
    __swig_getmethods__["numServers"] = _lsf.clusterInfo_numServers_get
    if _newclass:numServers = property(_lsf.clusterInfo_numServers_get, _lsf.clusterInfo_numServers_set)
    __swig_setmethods__["numClients"] = _lsf.clusterInfo_numClients_set
    __swig_getmethods__["numClients"] = _lsf.clusterInfo_numClients_get
    if _newclass:numClients = property(_lsf.clusterInfo_numClients_get, _lsf.clusterInfo_numClients_set)
    __swig_setmethods__["nRes"] = _lsf.clusterInfo_nRes_set
    __swig_getmethods__["nRes"] = _lsf.clusterInfo_nRes_get
    if _newclass:nRes = property(_lsf.clusterInfo_nRes_get, _lsf.clusterInfo_nRes_set)
    __swig_setmethods__["resources"] = _lsf.clusterInfo_resources_set
    __swig_getmethods__["resources"] = _lsf.clusterInfo_resources_get
    if _newclass:resources = property(_lsf.clusterInfo_resources_get, _lsf.clusterInfo_resources_set)
    __swig_setmethods__["nTypes"] = _lsf.clusterInfo_nTypes_set
    __swig_getmethods__["nTypes"] = _lsf.clusterInfo_nTypes_get
    if _newclass:nTypes = property(_lsf.clusterInfo_nTypes_get, _lsf.clusterInfo_nTypes_set)
    __swig_setmethods__["hostTypes"] = _lsf.clusterInfo_hostTypes_set
    __swig_getmethods__["hostTypes"] = _lsf.clusterInfo_hostTypes_get
    if _newclass:hostTypes = property(_lsf.clusterInfo_hostTypes_get, _lsf.clusterInfo_hostTypes_set)
    __swig_setmethods__["nModels"] = _lsf.clusterInfo_nModels_set
    __swig_getmethods__["nModels"] = _lsf.clusterInfo_nModels_get
    if _newclass:nModels = property(_lsf.clusterInfo_nModels_get, _lsf.clusterInfo_nModels_set)
    __swig_setmethods__["hostModels"] = _lsf.clusterInfo_hostModels_set
    __swig_getmethods__["hostModels"] = _lsf.clusterInfo_hostModels_get
    if _newclass:hostModels = property(_lsf.clusterInfo_hostModels_get, _lsf.clusterInfo_hostModels_set)
    __swig_setmethods__["nAdmins"] = _lsf.clusterInfo_nAdmins_set
    __swig_getmethods__["nAdmins"] = _lsf.clusterInfo_nAdmins_get
    if _newclass:nAdmins = property(_lsf.clusterInfo_nAdmins_get, _lsf.clusterInfo_nAdmins_set)
    __swig_setmethods__["adminIds"] = _lsf.clusterInfo_adminIds_set
    __swig_getmethods__["adminIds"] = _lsf.clusterInfo_adminIds_get
    if _newclass:adminIds = property(_lsf.clusterInfo_adminIds_get, _lsf.clusterInfo_adminIds_set)
    __swig_setmethods__["admins"] = _lsf.clusterInfo_admins_set
    __swig_getmethods__["admins"] = _lsf.clusterInfo_admins_get
    if _newclass:admins = property(_lsf.clusterInfo_admins_get, _lsf.clusterInfo_admins_set)
    __swig_setmethods__["analyzerLicFlag"] = _lsf.clusterInfo_analyzerLicFlag_set
    __swig_getmethods__["analyzerLicFlag"] = _lsf.clusterInfo_analyzerLicFlag_get
    if _newclass:analyzerLicFlag = property(_lsf.clusterInfo_analyzerLicFlag_get, _lsf.clusterInfo_analyzerLicFlag_set)
    __swig_setmethods__["jsLicFlag"] = _lsf.clusterInfo_jsLicFlag_set
    __swig_getmethods__["jsLicFlag"] = _lsf.clusterInfo_jsLicFlag_get
    if _newclass:jsLicFlag = property(_lsf.clusterInfo_jsLicFlag_get, _lsf.clusterInfo_jsLicFlag_set)
    __swig_setmethods__["afterHoursWindow"] = _lsf.clusterInfo_afterHoursWindow_set
    __swig_getmethods__["afterHoursWindow"] = _lsf.clusterInfo_afterHoursWindow_get
    if _newclass:afterHoursWindow = property(_lsf.clusterInfo_afterHoursWindow_get, _lsf.clusterInfo_afterHoursWindow_set)
    __swig_setmethods__["preferAuthName"] = _lsf.clusterInfo_preferAuthName_set
    __swig_getmethods__["preferAuthName"] = _lsf.clusterInfo_preferAuthName_get
    if _newclass:preferAuthName = property(_lsf.clusterInfo_preferAuthName_get, _lsf.clusterInfo_preferAuthName_set)
    __swig_setmethods__["inUseAuthName"] = _lsf.clusterInfo_inUseAuthName_set
    __swig_getmethods__["inUseAuthName"] = _lsf.clusterInfo_inUseAuthName_get
    if _newclass:inUseAuthName = property(_lsf.clusterInfo_inUseAuthName_get, _lsf.clusterInfo_inUseAuthName_set)
    def __init__(self, *args): 
        this = _lsf.new_clusterInfo(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _lsf.delete_clusterInfo
    __del__ = lambda self : None;
clusterInfo_swigregister = _lsf.clusterInfo_swigregister
clusterInfo_swigregister(clusterInfo)

class hostInfo(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, hostInfo, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, hostInfo, name)
    __repr__ = _swig_repr
    __swig_setmethods__["hostName"] = _lsf.hostInfo_hostName_set
    __swig_getmethods__["hostName"] = _lsf.hostInfo_hostName_get
    if _newclass:hostName = property(_lsf.hostInfo_hostName_get, _lsf.hostInfo_hostName_set)
    __swig_setmethods__["hostType"] = _lsf.hostInfo_hostType_set
    __swig_getmethods__["hostType"] = _lsf.hostInfo_hostType_get
    if _newclass:hostType = property(_lsf.hostInfo_hostType_get, _lsf.hostInfo_hostType_set)
    __swig_setmethods__["hostModel"] = _lsf.hostInfo_hostModel_set
    __swig_getmethods__["hostModel"] = _lsf.hostInfo_hostModel_get
    if _newclass:hostModel = property(_lsf.hostInfo_hostModel_get, _lsf.hostInfo_hostModel_set)
    __swig_setmethods__["cpuFactor"] = _lsf.hostInfo_cpuFactor_set
    __swig_getmethods__["cpuFactor"] = _lsf.hostInfo_cpuFactor_get
    if _newclass:cpuFactor = property(_lsf.hostInfo_cpuFactor_get, _lsf.hostInfo_cpuFactor_set)
    __swig_setmethods__["maxCpus"] = _lsf.hostInfo_maxCpus_set
    __swig_getmethods__["maxCpus"] = _lsf.hostInfo_maxCpus_get
    if _newclass:maxCpus = property(_lsf.hostInfo_maxCpus_get, _lsf.hostInfo_maxCpus_set)
    __swig_setmethods__["maxMem"] = _lsf.hostInfo_maxMem_set
    __swig_getmethods__["maxMem"] = _lsf.hostInfo_maxMem_get
    if _newclass:maxMem = property(_lsf.hostInfo_maxMem_get, _lsf.hostInfo_maxMem_set)
    __swig_setmethods__["maxSwap"] = _lsf.hostInfo_maxSwap_set
    __swig_getmethods__["maxSwap"] = _lsf.hostInfo_maxSwap_get
    if _newclass:maxSwap = property(_lsf.hostInfo_maxSwap_get, _lsf.hostInfo_maxSwap_set)
    __swig_setmethods__["maxTmp"] = _lsf.hostInfo_maxTmp_set
    __swig_getmethods__["maxTmp"] = _lsf.hostInfo_maxTmp_get
    if _newclass:maxTmp = property(_lsf.hostInfo_maxTmp_get, _lsf.hostInfo_maxTmp_set)
    __swig_setmethods__["nDisks"] = _lsf.hostInfo_nDisks_set
    __swig_getmethods__["nDisks"] = _lsf.hostInfo_nDisks_get
    if _newclass:nDisks = property(_lsf.hostInfo_nDisks_get, _lsf.hostInfo_nDisks_set)
    __swig_setmethods__["nRes"] = _lsf.hostInfo_nRes_set
    __swig_getmethods__["nRes"] = _lsf.hostInfo_nRes_get
    if _newclass:nRes = property(_lsf.hostInfo_nRes_get, _lsf.hostInfo_nRes_set)
    __swig_setmethods__["resources"] = _lsf.hostInfo_resources_set
    __swig_getmethods__["resources"] = _lsf.hostInfo_resources_get
    if _newclass:resources = property(_lsf.hostInfo_resources_get, _lsf.hostInfo_resources_set)
    __swig_setmethods__["nDRes"] = _lsf.hostInfo_nDRes_set
    __swig_getmethods__["nDRes"] = _lsf.hostInfo_nDRes_get
    if _newclass:nDRes = property(_lsf.hostInfo_nDRes_get, _lsf.hostInfo_nDRes_set)
    __swig_setmethods__["DResources"] = _lsf.hostInfo_DResources_set
    __swig_getmethods__["DResources"] = _lsf.hostInfo_DResources_get
    if _newclass:DResources = property(_lsf.hostInfo_DResources_get, _lsf.hostInfo_DResources_set)
    __swig_setmethods__["windows"] = _lsf.hostInfo_windows_set
    __swig_getmethods__["windows"] = _lsf.hostInfo_windows_get
    if _newclass:windows = property(_lsf.hostInfo_windows_get, _lsf.hostInfo_windows_set)
    __swig_setmethods__["numIndx"] = _lsf.hostInfo_numIndx_set
    __swig_getmethods__["numIndx"] = _lsf.hostInfo_numIndx_get
    if _newclass:numIndx = property(_lsf.hostInfo_numIndx_get, _lsf.hostInfo_numIndx_set)
    __swig_setmethods__["busyThreshold"] = _lsf.hostInfo_busyThreshold_set
    __swig_getmethods__["busyThreshold"] = _lsf.hostInfo_busyThreshold_get
    if _newclass:busyThreshold = property(_lsf.hostInfo_busyThreshold_get, _lsf.hostInfo_busyThreshold_set)
    __swig_setmethods__["isServer"] = _lsf.hostInfo_isServer_set
    __swig_getmethods__["isServer"] = _lsf.hostInfo_isServer_get
    if _newclass:isServer = property(_lsf.hostInfo_isServer_get, _lsf.hostInfo_isServer_set)
    __swig_setmethods__["licensed"] = _lsf.hostInfo_licensed_set
    __swig_getmethods__["licensed"] = _lsf.hostInfo_licensed_get
    if _newclass:licensed = property(_lsf.hostInfo_licensed_get, _lsf.hostInfo_licensed_set)
    __swig_setmethods__["rexPriority"] = _lsf.hostInfo_rexPriority_set
    __swig_getmethods__["rexPriority"] = _lsf.hostInfo_rexPriority_get
    if _newclass:rexPriority = property(_lsf.hostInfo_rexPriority_get, _lsf.hostInfo_rexPriority_set)
    __swig_setmethods__["licFeaturesNeeded"] = _lsf.hostInfo_licFeaturesNeeded_set
    __swig_getmethods__["licFeaturesNeeded"] = _lsf.hostInfo_licFeaturesNeeded_get
    if _newclass:licFeaturesNeeded = property(_lsf.hostInfo_licFeaturesNeeded_get, _lsf.hostInfo_licFeaturesNeeded_set)
    __swig_setmethods__["licClass"] = _lsf.hostInfo_licClass_set
    __swig_getmethods__["licClass"] = _lsf.hostInfo_licClass_get
    if _newclass:licClass = property(_lsf.hostInfo_licClass_get, _lsf.hostInfo_licClass_set)
    __swig_setmethods__["cores"] = _lsf.hostInfo_cores_set
    __swig_getmethods__["cores"] = _lsf.hostInfo_cores_get
    if _newclass:cores = property(_lsf.hostInfo_cores_get, _lsf.hostInfo_cores_set)
    __swig_setmethods__["hostAddr"] = _lsf.hostInfo_hostAddr_set
    __swig_getmethods__["hostAddr"] = _lsf.hostInfo_hostAddr_get
    if _newclass:hostAddr = property(_lsf.hostInfo_hostAddr_get, _lsf.hostInfo_hostAddr_set)
    __swig_setmethods__["pprocs"] = _lsf.hostInfo_pprocs_set
    __swig_getmethods__["pprocs"] = _lsf.hostInfo_pprocs_get
    if _newclass:pprocs = property(_lsf.hostInfo_pprocs_get, _lsf.hostInfo_pprocs_set)
    __swig_setmethods__["cores_per_proc"] = _lsf.hostInfo_cores_per_proc_set
    __swig_getmethods__["cores_per_proc"] = _lsf.hostInfo_cores_per_proc_get
    if _newclass:cores_per_proc = property(_lsf.hostInfo_cores_per_proc_get, _lsf.hostInfo_cores_per_proc_set)
    __swig_setmethods__["threads_per_core"] = _lsf.hostInfo_threads_per_core_set
    __swig_getmethods__["threads_per_core"] = _lsf.hostInfo_threads_per_core_get
    if _newclass:threads_per_core = property(_lsf.hostInfo_threads_per_core_get, _lsf.hostInfo_threads_per_core_set)
    def __init__(self, *args): 
        this = _lsf.new_hostInfo(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _lsf.delete_hostInfo
    __del__ = lambda self : None;
hostInfo_swigregister = _lsf.hostInfo_swigregister
hostInfo_swigregister(hostInfo)
LSF_BASE_LIC = _lsf.LSF_BASE_LIC
LSF_BATCH_LIC_OBSOLETE = _lsf.LSF_BATCH_LIC_OBSOLETE
LSF_JS_SCHEDULER_LIC = _lsf.LSF_JS_SCHEDULER_LIC
LSF_JS_LIC = _lsf.LSF_JS_LIC
LSF_CLIENT_LIC = _lsf.LSF_CLIENT_LIC
LSF_MC_LIC = _lsf.LSF_MC_LIC
LSF_ANALYZER_SERVER_LIC = _lsf.LSF_ANALYZER_SERVER_LIC
LSF_MAKE_LIC = _lsf.LSF_MAKE_LIC
LSF_PARALLEL_LIC = _lsf.LSF_PARALLEL_LIC
LSF_FLOAT_CLIENT_LIC = _lsf.LSF_FLOAT_CLIENT_LIC
LSF_FTA_LIC = _lsf.LSF_FTA_LIC
LSF_AFTER_HOURS_LIC = _lsf.LSF_AFTER_HOURS_LIC
LSF_RESOURCE_PREEMPT_LIC = _lsf.LSF_RESOURCE_PREEMPT_LIC
LSF_BACCT_LIC = _lsf.LSF_BACCT_LIC
LSF_SCHED_FAIRSHARE_LIC = _lsf.LSF_SCHED_FAIRSHARE_LIC
LSF_SCHED_RESERVE_LIC = _lsf.LSF_SCHED_RESERVE_LIC
LSF_SCHED_PREEMPTION_LIC = _lsf.LSF_SCHED_PREEMPTION_LIC
LSF_SCHED_PARALLEL_LIC = _lsf.LSF_SCHED_PARALLEL_LIC
LSF_SCHED_ADVRSV_LIC = _lsf.LSF_SCHED_ADVRSV_LIC
LSF_API_CLIENT_LIC = _lsf.LSF_API_CLIENT_LIC
LSF_EMBEDDED_LIC = _lsf.LSF_EMBEDDED_LIC
LSF_MANAGER_LIC = _lsf.LSF_MANAGER_LIC
LSF_PCC_HPC_LIC = _lsf.LSF_PCC_HPC_LIC
sCLUSTERWARE_LIC = _lsf.sCLUSTERWARE_LIC
OTTAWA_MANAGER_LIC = _lsf.OTTAWA_MANAGER_LIC
SYMPHONY_MANAGER_ONLINE_LIC = _lsf.SYMPHONY_MANAGER_ONLINE_LIC
SYMPHONY_MANAGER_BATCH_LIC = _lsf.SYMPHONY_MANAGER_BATCH_LIC
SYMPHONY_SCHED_JOB_PRIORITY_LIC = _lsf.SYMPHONY_SCHED_JOB_PRIORITY_LIC
LSF_DUALCORE_X86_LIC = _lsf.LSF_DUALCORE_X86_LIC
LSF_SSCHED_LIC = _lsf.LSF_SSCHED_LIC
LSF_WORKGROUP_LIC = _lsf.LSF_WORKGROUP_LIC
LSF_NUM_LIC_TYPE = _lsf.LSF_NUM_LIC_TYPE
LSF_WG_NUM_LIC_TYPE = _lsf.LSF_WG_NUM_LIC_TYPE
LSF_NO_NEED_LIC = _lsf.LSF_NO_NEED_LIC
INET6_ADDRSTRLEN = _lsf.INET6_ADDRSTRLEN

class config_param(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, config_param, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, config_param, name)
    __repr__ = _swig_repr
    __swig_setmethods__["paramName"] = _lsf.config_param_paramName_set
    __swig_getmethods__["paramName"] = _lsf.config_param_paramName_get
    if _newclass:paramName = property(_lsf.config_param_paramName_get, _lsf.config_param_paramName_set)
    __swig_setmethods__["paramValue"] = _lsf.config_param_paramValue_set
    __swig_getmethods__["paramValue"] = _lsf.config_param_paramValue_get
    if _newclass:paramValue = property(_lsf.config_param_paramValue_get, _lsf.config_param_paramValue_set)
    def __init__(self, *args): 
        this = _lsf.new_config_param(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _lsf.delete_config_param
    __del__ = lambda self : None;
config_param_swigregister = _lsf.config_param_swigregister
config_param_swigregister(config_param)

class lsfRusage(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, lsfRusage, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, lsfRusage, name)
    __repr__ = _swig_repr
    __swig_setmethods__["ru_utime"] = _lsf.lsfRusage_ru_utime_set
    __swig_getmethods__["ru_utime"] = _lsf.lsfRusage_ru_utime_get
    if _newclass:ru_utime = property(_lsf.lsfRusage_ru_utime_get, _lsf.lsfRusage_ru_utime_set)
    __swig_setmethods__["ru_stime"] = _lsf.lsfRusage_ru_stime_set
    __swig_getmethods__["ru_stime"] = _lsf.lsfRusage_ru_stime_get
    if _newclass:ru_stime = property(_lsf.lsfRusage_ru_stime_get, _lsf.lsfRusage_ru_stime_set)
    __swig_setmethods__["ru_maxrss"] = _lsf.lsfRusage_ru_maxrss_set
    __swig_getmethods__["ru_maxrss"] = _lsf.lsfRusage_ru_maxrss_get
    if _newclass:ru_maxrss = property(_lsf.lsfRusage_ru_maxrss_get, _lsf.lsfRusage_ru_maxrss_set)
    __swig_setmethods__["ru_ixrss"] = _lsf.lsfRusage_ru_ixrss_set
    __swig_getmethods__["ru_ixrss"] = _lsf.lsfRusage_ru_ixrss_get
    if _newclass:ru_ixrss = property(_lsf.lsfRusage_ru_ixrss_get, _lsf.lsfRusage_ru_ixrss_set)
    __swig_setmethods__["ru_ismrss"] = _lsf.lsfRusage_ru_ismrss_set
    __swig_getmethods__["ru_ismrss"] = _lsf.lsfRusage_ru_ismrss_get
    if _newclass:ru_ismrss = property(_lsf.lsfRusage_ru_ismrss_get, _lsf.lsfRusage_ru_ismrss_set)
    __swig_setmethods__["ru_idrss"] = _lsf.lsfRusage_ru_idrss_set
    __swig_getmethods__["ru_idrss"] = _lsf.lsfRusage_ru_idrss_get
    if _newclass:ru_idrss = property(_lsf.lsfRusage_ru_idrss_get, _lsf.lsfRusage_ru_idrss_set)
    __swig_setmethods__["ru_isrss"] = _lsf.lsfRusage_ru_isrss_set
    __swig_getmethods__["ru_isrss"] = _lsf.lsfRusage_ru_isrss_get
    if _newclass:ru_isrss = property(_lsf.lsfRusage_ru_isrss_get, _lsf.lsfRusage_ru_isrss_set)
    __swig_setmethods__["ru_minflt"] = _lsf.lsfRusage_ru_minflt_set
    __swig_getmethods__["ru_minflt"] = _lsf.lsfRusage_ru_minflt_get
    if _newclass:ru_minflt = property(_lsf.lsfRusage_ru_minflt_get, _lsf.lsfRusage_ru_minflt_set)
    __swig_setmethods__["ru_majflt"] = _lsf.lsfRusage_ru_majflt_set
    __swig_getmethods__["ru_majflt"] = _lsf.lsfRusage_ru_majflt_get
    if _newclass:ru_majflt = property(_lsf.lsfRusage_ru_majflt_get, _lsf.lsfRusage_ru_majflt_set)
    __swig_setmethods__["ru_nswap"] = _lsf.lsfRusage_ru_nswap_set
    __swig_getmethods__["ru_nswap"] = _lsf.lsfRusage_ru_nswap_get
    if _newclass:ru_nswap = property(_lsf.lsfRusage_ru_nswap_get, _lsf.lsfRusage_ru_nswap_set)
    __swig_setmethods__["ru_inblock"] = _lsf.lsfRusage_ru_inblock_set
    __swig_getmethods__["ru_inblock"] = _lsf.lsfRusage_ru_inblock_get
    if _newclass:ru_inblock = property(_lsf.lsfRusage_ru_inblock_get, _lsf.lsfRusage_ru_inblock_set)
    __swig_setmethods__["ru_oublock"] = _lsf.lsfRusage_ru_oublock_set
    __swig_getmethods__["ru_oublock"] = _lsf.lsfRusage_ru_oublock_get
    if _newclass:ru_oublock = property(_lsf.lsfRusage_ru_oublock_get, _lsf.lsfRusage_ru_oublock_set)
    __swig_setmethods__["ru_ioch"] = _lsf.lsfRusage_ru_ioch_set
    __swig_getmethods__["ru_ioch"] = _lsf.lsfRusage_ru_ioch_get
    if _newclass:ru_ioch = property(_lsf.lsfRusage_ru_ioch_get, _lsf.lsfRusage_ru_ioch_set)
    __swig_setmethods__["ru_msgsnd"] = _lsf.lsfRusage_ru_msgsnd_set
    __swig_getmethods__["ru_msgsnd"] = _lsf.lsfRusage_ru_msgsnd_get
    if _newclass:ru_msgsnd = property(_lsf.lsfRusage_ru_msgsnd_get, _lsf.lsfRusage_ru_msgsnd_set)
    __swig_setmethods__["ru_msgrcv"] = _lsf.lsfRusage_ru_msgrcv_set
    __swig_getmethods__["ru_msgrcv"] = _lsf.lsfRusage_ru_msgrcv_get
    if _newclass:ru_msgrcv = property(_lsf.lsfRusage_ru_msgrcv_get, _lsf.lsfRusage_ru_msgrcv_set)
    __swig_setmethods__["ru_nsignals"] = _lsf.lsfRusage_ru_nsignals_set
    __swig_getmethods__["ru_nsignals"] = _lsf.lsfRusage_ru_nsignals_get
    if _newclass:ru_nsignals = property(_lsf.lsfRusage_ru_nsignals_get, _lsf.lsfRusage_ru_nsignals_set)
    __swig_setmethods__["ru_nvcsw"] = _lsf.lsfRusage_ru_nvcsw_set
    __swig_getmethods__["ru_nvcsw"] = _lsf.lsfRusage_ru_nvcsw_get
    if _newclass:ru_nvcsw = property(_lsf.lsfRusage_ru_nvcsw_get, _lsf.lsfRusage_ru_nvcsw_set)
    __swig_setmethods__["ru_nivcsw"] = _lsf.lsfRusage_ru_nivcsw_set
    __swig_getmethods__["ru_nivcsw"] = _lsf.lsfRusage_ru_nivcsw_get
    if _newclass:ru_nivcsw = property(_lsf.lsfRusage_ru_nivcsw_get, _lsf.lsfRusage_ru_nivcsw_set)
    __swig_setmethods__["ru_exutime"] = _lsf.lsfRusage_ru_exutime_set
    __swig_getmethods__["ru_exutime"] = _lsf.lsfRusage_ru_exutime_get
    if _newclass:ru_exutime = property(_lsf.lsfRusage_ru_exutime_get, _lsf.lsfRusage_ru_exutime_set)
    def __init__(self, *args): 
        this = _lsf.new_lsfRusage(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _lsf.delete_lsfRusage
    __del__ = lambda self : None;
lsfRusage_swigregister = _lsf.lsfRusage_swigregister
lsfRusage_swigregister(lsfRusage)

class lsfAcctRec(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, lsfAcctRec, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, lsfAcctRec, name)
    __repr__ = _swig_repr
    __swig_setmethods__["pid"] = _lsf.lsfAcctRec_pid_set
    __swig_getmethods__["pid"] = _lsf.lsfAcctRec_pid_get
    if _newclass:pid = property(_lsf.lsfAcctRec_pid_get, _lsf.lsfAcctRec_pid_set)
    __swig_setmethods__["username"] = _lsf.lsfAcctRec_username_set
    __swig_getmethods__["username"] = _lsf.lsfAcctRec_username_get
    if _newclass:username = property(_lsf.lsfAcctRec_username_get, _lsf.lsfAcctRec_username_set)
    __swig_setmethods__["exitStatus"] = _lsf.lsfAcctRec_exitStatus_set
    __swig_getmethods__["exitStatus"] = _lsf.lsfAcctRec_exitStatus_get
    if _newclass:exitStatus = property(_lsf.lsfAcctRec_exitStatus_get, _lsf.lsfAcctRec_exitStatus_set)
    __swig_setmethods__["dispTime"] = _lsf.lsfAcctRec_dispTime_set
    __swig_getmethods__["dispTime"] = _lsf.lsfAcctRec_dispTime_get
    if _newclass:dispTime = property(_lsf.lsfAcctRec_dispTime_get, _lsf.lsfAcctRec_dispTime_set)
    __swig_setmethods__["termTime"] = _lsf.lsfAcctRec_termTime_set
    __swig_getmethods__["termTime"] = _lsf.lsfAcctRec_termTime_get
    if _newclass:termTime = property(_lsf.lsfAcctRec_termTime_get, _lsf.lsfAcctRec_termTime_set)
    __swig_setmethods__["fromHost"] = _lsf.lsfAcctRec_fromHost_set
    __swig_getmethods__["fromHost"] = _lsf.lsfAcctRec_fromHost_get
    if _newclass:fromHost = property(_lsf.lsfAcctRec_fromHost_get, _lsf.lsfAcctRec_fromHost_set)
    __swig_setmethods__["execHost"] = _lsf.lsfAcctRec_execHost_set
    __swig_getmethods__["execHost"] = _lsf.lsfAcctRec_execHost_get
    if _newclass:execHost = property(_lsf.lsfAcctRec_execHost_get, _lsf.lsfAcctRec_execHost_set)
    __swig_setmethods__["cwd"] = _lsf.lsfAcctRec_cwd_set
    __swig_getmethods__["cwd"] = _lsf.lsfAcctRec_cwd_get
    if _newclass:cwd = property(_lsf.lsfAcctRec_cwd_get, _lsf.lsfAcctRec_cwd_set)
    __swig_setmethods__["cmdln"] = _lsf.lsfAcctRec_cmdln_set
    __swig_getmethods__["cmdln"] = _lsf.lsfAcctRec_cmdln_get
    if _newclass:cmdln = property(_lsf.lsfAcctRec_cmdln_get, _lsf.lsfAcctRec_cmdln_set)
    __swig_setmethods__["lsfRu"] = _lsf.lsfAcctRec_lsfRu_set
    __swig_getmethods__["lsfRu"] = _lsf.lsfAcctRec_lsfRu_get
    if _newclass:lsfRu = property(_lsf.lsfAcctRec_lsfRu_get, _lsf.lsfAcctRec_lsfRu_set)
    def __init__(self, *args): 
        this = _lsf.new_lsfAcctRec(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _lsf.delete_lsfAcctRec
    __del__ = lambda self : None;
lsfAcctRec_swigregister = _lsf.lsfAcctRec_swigregister
lsfAcctRec_swigregister(lsfAcctRec)

class confNode(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, confNode, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, confNode, name)
    __repr__ = _swig_repr
    __swig_setmethods__["leftPtr"] = _lsf.confNode_leftPtr_set
    __swig_getmethods__["leftPtr"] = _lsf.confNode_leftPtr_get
    if _newclass:leftPtr = property(_lsf.confNode_leftPtr_get, _lsf.confNode_leftPtr_set)
    __swig_setmethods__["rightPtr"] = _lsf.confNode_rightPtr_set
    __swig_getmethods__["rightPtr"] = _lsf.confNode_rightPtr_get
    if _newclass:rightPtr = property(_lsf.confNode_rightPtr_get, _lsf.confNode_rightPtr_set)
    __swig_setmethods__["fwPtr"] = _lsf.confNode_fwPtr_set
    __swig_getmethods__["fwPtr"] = _lsf.confNode_fwPtr_get
    if _newclass:fwPtr = property(_lsf.confNode_fwPtr_get, _lsf.confNode_fwPtr_set)
    __swig_setmethods__["cond"] = _lsf.confNode_cond_set
    __swig_getmethods__["cond"] = _lsf.confNode_cond_get
    if _newclass:cond = property(_lsf.confNode_cond_get, _lsf.confNode_cond_set)
    __swig_setmethods__["beginLineNum"] = _lsf.confNode_beginLineNum_set
    __swig_getmethods__["beginLineNum"] = _lsf.confNode_beginLineNum_get
    if _newclass:beginLineNum = property(_lsf.confNode_beginLineNum_get, _lsf.confNode_beginLineNum_set)
    __swig_setmethods__["numLines"] = _lsf.confNode_numLines_set
    __swig_getmethods__["numLines"] = _lsf.confNode_numLines_get
    if _newclass:numLines = property(_lsf.confNode_numLines_get, _lsf.confNode_numLines_set)
    __swig_setmethods__["lines"] = _lsf.confNode_lines_set
    __swig_getmethods__["lines"] = _lsf.confNode_lines_get
    if _newclass:lines = property(_lsf.confNode_lines_get, _lsf.confNode_lines_set)
    __swig_setmethods__["tag"] = _lsf.confNode_tag_set
    __swig_getmethods__["tag"] = _lsf.confNode_tag_get
    if _newclass:tag = property(_lsf.confNode_tag_get, _lsf.confNode_tag_set)
    def __init__(self, *args): 
        this = _lsf.new_confNode(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _lsf.delete_confNode
    __del__ = lambda self : None;
confNode_swigregister = _lsf.confNode_swigregister
confNode_swigregister(confNode)

class pStack(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, pStack, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, pStack, name)
    __repr__ = _swig_repr
    __swig_setmethods__["top"] = _lsf.pStack_top_set
    __swig_getmethods__["top"] = _lsf.pStack_top_get
    if _newclass:top = property(_lsf.pStack_top_get, _lsf.pStack_top_set)
    __swig_setmethods__["size"] = _lsf.pStack_size_set
    __swig_getmethods__["size"] = _lsf.pStack_size_get
    if _newclass:size = property(_lsf.pStack_size_get, _lsf.pStack_size_set)
    __swig_setmethods__["nodes"] = _lsf.pStack_nodes_set
    __swig_getmethods__["nodes"] = _lsf.pStack_nodes_get
    if _newclass:nodes = property(_lsf.pStack_nodes_get, _lsf.pStack_nodes_set)
    def __init__(self, *args): 
        this = _lsf.new_pStack(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _lsf.delete_pStack
    __del__ = lambda self : None;
pStack_swigregister = _lsf.pStack_swigregister
pStack_swigregister(pStack)

class confHandle(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, confHandle, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, confHandle, name)
    __repr__ = _swig_repr
    __swig_setmethods__["rootNode"] = _lsf.confHandle_rootNode_set
    __swig_getmethods__["rootNode"] = _lsf.confHandle_rootNode_get
    if _newclass:rootNode = property(_lsf.confHandle_rootNode_get, _lsf.confHandle_rootNode_set)
    __swig_setmethods__["fname"] = _lsf.confHandle_fname_set
    __swig_getmethods__["fname"] = _lsf.confHandle_fname_get
    if _newclass:fname = property(_lsf.confHandle_fname_get, _lsf.confHandle_fname_set)
    __swig_setmethods__["curNode"] = _lsf.confHandle_curNode_set
    __swig_getmethods__["curNode"] = _lsf.confHandle_curNode_get
    if _newclass:curNode = property(_lsf.confHandle_curNode_get, _lsf.confHandle_curNode_set)
    __swig_setmethods__["lineCount"] = _lsf.confHandle_lineCount_set
    __swig_getmethods__["lineCount"] = _lsf.confHandle_lineCount_get
    if _newclass:lineCount = property(_lsf.confHandle_lineCount_get, _lsf.confHandle_lineCount_set)
    __swig_setmethods__["ptrStack"] = _lsf.confHandle_ptrStack_set
    __swig_getmethods__["ptrStack"] = _lsf.confHandle_ptrStack_get
    if _newclass:ptrStack = property(_lsf.confHandle_ptrStack_get, _lsf.confHandle_ptrStack_set)
    def __init__(self, *args): 
        this = _lsf.new_confHandle(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _lsf.delete_confHandle
    __del__ = lambda self : None;
confHandle_swigregister = _lsf.confHandle_swigregister
confHandle_swigregister(confHandle)

class lsConf(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, lsConf, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, lsConf, name)
    __repr__ = _swig_repr
    __swig_setmethods__["confhandle"] = _lsf.lsConf_confhandle_set
    __swig_getmethods__["confhandle"] = _lsf.lsConf_confhandle_get
    if _newclass:confhandle = property(_lsf.lsConf_confhandle_get, _lsf.lsConf_confhandle_set)
    __swig_setmethods__["numConds"] = _lsf.lsConf_numConds_set
    __swig_getmethods__["numConds"] = _lsf.lsConf_numConds_get
    if _newclass:numConds = property(_lsf.lsConf_numConds_get, _lsf.lsConf_numConds_set)
    __swig_setmethods__["conds"] = _lsf.lsConf_conds_set
    __swig_getmethods__["conds"] = _lsf.lsConf_conds_get
    if _newclass:conds = property(_lsf.lsConf_conds_get, _lsf.lsConf_conds_set)
    __swig_setmethods__["values"] = _lsf.lsConf_values_set
    __swig_getmethods__["values"] = _lsf.lsConf_values_get
    if _newclass:values = property(_lsf.lsConf_values_get, _lsf.lsConf_values_set)
    def __init__(self, *args): 
        this = _lsf.new_lsConf(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _lsf.delete_lsConf
    __del__ = lambda self : None;
lsConf_swigregister = _lsf.lsConf_swigregister
lsConf_swigregister(lsConf)

class sharedConf(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, sharedConf, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, sharedConf, name)
    __repr__ = _swig_repr
    __swig_setmethods__["lsinfo"] = _lsf.sharedConf_lsinfo_set
    __swig_getmethods__["lsinfo"] = _lsf.sharedConf_lsinfo_get
    if _newclass:lsinfo = property(_lsf.sharedConf_lsinfo_get, _lsf.sharedConf_lsinfo_set)
    __swig_setmethods__["numCls"] = _lsf.sharedConf_numCls_set
    __swig_getmethods__["numCls"] = _lsf.sharedConf_numCls_get
    if _newclass:numCls = property(_lsf.sharedConf_numCls_get, _lsf.sharedConf_numCls_set)
    __swig_setmethods__["clusterNames"] = _lsf.sharedConf_clusterNames_set
    __swig_getmethods__["clusterNames"] = _lsf.sharedConf_clusterNames_get
    if _newclass:clusterNames = property(_lsf.sharedConf_clusterNames_get, _lsf.sharedConf_clusterNames_set)
    __swig_setmethods__["servers"] = _lsf.sharedConf_servers_set
    __swig_getmethods__["servers"] = _lsf.sharedConf_servers_get
    if _newclass:servers = property(_lsf.sharedConf_servers_get, _lsf.sharedConf_servers_set)
    def __init__(self, *args): 
        this = _lsf.new_sharedConf(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _lsf.delete_sharedConf
    __del__ = lambda self : None;
sharedConf_swigregister = _lsf.sharedConf_swigregister
sharedConf_swigregister(sharedConf)

class LS_SHARED_RESOURCE_INST_T(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, LS_SHARED_RESOURCE_INST_T, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, LS_SHARED_RESOURCE_INST_T, name)
    __repr__ = _swig_repr
    __swig_setmethods__["value"] = _lsf.LS_SHARED_RESOURCE_INST_T_value_set
    __swig_getmethods__["value"] = _lsf.LS_SHARED_RESOURCE_INST_T_value_get
    if _newclass:value = property(_lsf.LS_SHARED_RESOURCE_INST_T_value_get, _lsf.LS_SHARED_RESOURCE_INST_T_value_set)
    __swig_setmethods__["nHosts"] = _lsf.LS_SHARED_RESOURCE_INST_T_nHosts_set
    __swig_getmethods__["nHosts"] = _lsf.LS_SHARED_RESOURCE_INST_T_nHosts_get
    if _newclass:nHosts = property(_lsf.LS_SHARED_RESOURCE_INST_T_nHosts_get, _lsf.LS_SHARED_RESOURCE_INST_T_nHosts_set)
    __swig_setmethods__["hostList"] = _lsf.LS_SHARED_RESOURCE_INST_T_hostList_set
    __swig_getmethods__["hostList"] = _lsf.LS_SHARED_RESOURCE_INST_T_hostList_get
    if _newclass:hostList = property(_lsf.LS_SHARED_RESOURCE_INST_T_hostList_get, _lsf.LS_SHARED_RESOURCE_INST_T_hostList_set)
    def __init__(self, *args): 
        this = _lsf.new_LS_SHARED_RESOURCE_INST_T(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _lsf.delete_LS_SHARED_RESOURCE_INST_T
    __del__ = lambda self : None;
LS_SHARED_RESOURCE_INST_T_swigregister = _lsf.LS_SHARED_RESOURCE_INST_T_swigregister
LS_SHARED_RESOURCE_INST_T_swigregister(LS_SHARED_RESOURCE_INST_T)

class LS_SHARED_RESOURCE_INFO_T(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, LS_SHARED_RESOURCE_INFO_T, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, LS_SHARED_RESOURCE_INFO_T, name)
    __repr__ = _swig_repr
    __swig_setmethods__["resourceName"] = _lsf.LS_SHARED_RESOURCE_INFO_T_resourceName_set
    __swig_getmethods__["resourceName"] = _lsf.LS_SHARED_RESOURCE_INFO_T_resourceName_get
    if _newclass:resourceName = property(_lsf.LS_SHARED_RESOURCE_INFO_T_resourceName_get, _lsf.LS_SHARED_RESOURCE_INFO_T_resourceName_set)
    __swig_setmethods__["nInstances"] = _lsf.LS_SHARED_RESOURCE_INFO_T_nInstances_set
    __swig_getmethods__["nInstances"] = _lsf.LS_SHARED_RESOURCE_INFO_T_nInstances_get
    if _newclass:nInstances = property(_lsf.LS_SHARED_RESOURCE_INFO_T_nInstances_get, _lsf.LS_SHARED_RESOURCE_INFO_T_nInstances_set)
    __swig_setmethods__["instances"] = _lsf.LS_SHARED_RESOURCE_INFO_T_instances_set
    __swig_getmethods__["instances"] = _lsf.LS_SHARED_RESOURCE_INFO_T_instances_get
    if _newclass:instances = property(_lsf.LS_SHARED_RESOURCE_INFO_T_instances_get, _lsf.LS_SHARED_RESOURCE_INFO_T_instances_set)
    def __init__(self, *args): 
        this = _lsf.new_LS_SHARED_RESOURCE_INFO_T(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _lsf.delete_LS_SHARED_RESOURCE_INFO_T
    __del__ = lambda self : None;
LS_SHARED_RESOURCE_INFO_T_swigregister = _lsf.LS_SHARED_RESOURCE_INFO_T_swigregister
LS_SHARED_RESOURCE_INFO_T_swigregister(LS_SHARED_RESOURCE_INFO_T)

class clusterConf(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, clusterConf, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, clusterConf, name)
    __repr__ = _swig_repr
    __swig_setmethods__["clinfo"] = _lsf.clusterConf_clinfo_set
    __swig_getmethods__["clinfo"] = _lsf.clusterConf_clinfo_get
    if _newclass:clinfo = property(_lsf.clusterConf_clinfo_get, _lsf.clusterConf_clinfo_set)
    __swig_setmethods__["numHosts"] = _lsf.clusterConf_numHosts_set
    __swig_getmethods__["numHosts"] = _lsf.clusterConf_numHosts_get
    if _newclass:numHosts = property(_lsf.clusterConf_numHosts_get, _lsf.clusterConf_numHosts_set)
    __swig_setmethods__["hosts"] = _lsf.clusterConf_hosts_set
    __swig_getmethods__["hosts"] = _lsf.clusterConf_hosts_get
    if _newclass:hosts = property(_lsf.clusterConf_hosts_get, _lsf.clusterConf_hosts_set)
    __swig_setmethods__["defaultFeatures"] = _lsf.clusterConf_defaultFeatures_set
    __swig_getmethods__["defaultFeatures"] = _lsf.clusterConf_defaultFeatures_get
    if _newclass:defaultFeatures = property(_lsf.clusterConf_defaultFeatures_get, _lsf.clusterConf_defaultFeatures_set)
    __swig_setmethods__["numShareRes"] = _lsf.clusterConf_numShareRes_set
    __swig_getmethods__["numShareRes"] = _lsf.clusterConf_numShareRes_get
    if _newclass:numShareRes = property(_lsf.clusterConf_numShareRes_get, _lsf.clusterConf_numShareRes_set)
    __swig_setmethods__["shareRes"] = _lsf.clusterConf_shareRes_set
    __swig_getmethods__["shareRes"] = _lsf.clusterConf_shareRes_get
    if _newclass:shareRes = property(_lsf.clusterConf_shareRes_get, _lsf.clusterConf_shareRes_set)
    def __init__(self, *args): 
        this = _lsf.new_clusterConf(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _lsf.delete_clusterConf
    __del__ = lambda self : None;
clusterConf_swigregister = _lsf.clusterConf_swigregister
clusterConf_swigregister(clusterConf)

class pidInfo(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, pidInfo, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, pidInfo, name)
    __repr__ = _swig_repr
    __swig_setmethods__["pid"] = _lsf.pidInfo_pid_set
    __swig_getmethods__["pid"] = _lsf.pidInfo_pid_get
    if _newclass:pid = property(_lsf.pidInfo_pid_get, _lsf.pidInfo_pid_set)
    __swig_setmethods__["ppid"] = _lsf.pidInfo_ppid_set
    __swig_getmethods__["ppid"] = _lsf.pidInfo_ppid_get
    if _newclass:ppid = property(_lsf.pidInfo_ppid_get, _lsf.pidInfo_ppid_set)
    __swig_setmethods__["pgid"] = _lsf.pidInfo_pgid_set
    __swig_getmethods__["pgid"] = _lsf.pidInfo_pgid_get
    if _newclass:pgid = property(_lsf.pidInfo_pgid_get, _lsf.pidInfo_pgid_set)
    __swig_setmethods__["jobid"] = _lsf.pidInfo_jobid_set
    __swig_getmethods__["jobid"] = _lsf.pidInfo_jobid_get
    if _newclass:jobid = property(_lsf.pidInfo_jobid_get, _lsf.pidInfo_jobid_set)
    def __init__(self, *args): 
        this = _lsf.new_pidInfo(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _lsf.delete_pidInfo
    __del__ = lambda self : None;
pidInfo_swigregister = _lsf.pidInfo_swigregister
pidInfo_swigregister(pidInfo)

class jRusage(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, jRusage, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, jRusage, name)
    __repr__ = _swig_repr
    __swig_setmethods__["mem"] = _lsf.jRusage_mem_set
    __swig_getmethods__["mem"] = _lsf.jRusage_mem_get
    if _newclass:mem = property(_lsf.jRusage_mem_get, _lsf.jRusage_mem_set)
    __swig_setmethods__["swap"] = _lsf.jRusage_swap_set
    __swig_getmethods__["swap"] = _lsf.jRusage_swap_get
    if _newclass:swap = property(_lsf.jRusage_swap_get, _lsf.jRusage_swap_set)
    __swig_setmethods__["utime"] = _lsf.jRusage_utime_set
    __swig_getmethods__["utime"] = _lsf.jRusage_utime_get
    if _newclass:utime = property(_lsf.jRusage_utime_get, _lsf.jRusage_utime_set)
    __swig_setmethods__["stime"] = _lsf.jRusage_stime_set
    __swig_getmethods__["stime"] = _lsf.jRusage_stime_get
    if _newclass:stime = property(_lsf.jRusage_stime_get, _lsf.jRusage_stime_set)
    __swig_setmethods__["npids"] = _lsf.jRusage_npids_set
    __swig_getmethods__["npids"] = _lsf.jRusage_npids_get
    if _newclass:npids = property(_lsf.jRusage_npids_get, _lsf.jRusage_npids_set)
    __swig_setmethods__["pidInfo"] = _lsf.jRusage_pidInfo_set
    __swig_getmethods__["pidInfo"] = _lsf.jRusage_pidInfo_get
    if _newclass:pidInfo = property(_lsf.jRusage_pidInfo_get, _lsf.jRusage_pidInfo_set)
    __swig_setmethods__["npgids"] = _lsf.jRusage_npgids_set
    __swig_getmethods__["npgids"] = _lsf.jRusage_npgids_get
    if _newclass:npgids = property(_lsf.jRusage_npgids_get, _lsf.jRusage_npgids_set)
    __swig_setmethods__["pgid"] = _lsf.jRusage_pgid_set
    __swig_getmethods__["pgid"] = _lsf.jRusage_pgid_get
    if _newclass:pgid = property(_lsf.jRusage_pgid_get, _lsf.jRusage_pgid_set)
    __swig_setmethods__["nthreads"] = _lsf.jRusage_nthreads_set
    __swig_getmethods__["nthreads"] = _lsf.jRusage_nthreads_get
    if _newclass:nthreads = property(_lsf.jRusage_nthreads_get, _lsf.jRusage_nthreads_set)
    def __init__(self, *args): 
        this = _lsf.new_jRusage(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _lsf.delete_jRusage
    __del__ = lambda self : None;
jRusage_swigregister = _lsf.jRusage_swigregister
jRusage_swigregister(jRusage)

NUM_SUBS = _lsf.NUM_SUBS
LEN_SUBS = _lsf.LEN_SUBS
NUM_CLASS_TYPE = _lsf.NUM_CLASS_TYPE
class licUsage(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, licUsage, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, licUsage, name)
    __repr__ = _swig_repr
    __swig_setmethods__["licDisplayMask"] = _lsf.licUsage_licDisplayMask_set
    __swig_getmethods__["licDisplayMask"] = _lsf.licUsage_licDisplayMask_get
    if _newclass:licDisplayMask = property(_lsf.licUsage_licDisplayMask_get, _lsf.licUsage_licDisplayMask_set)
    __swig_setmethods__["usingDemoLicense"] = _lsf.licUsage_usingDemoLicense_set
    __swig_getmethods__["usingDemoLicense"] = _lsf.licUsage_usingDemoLicense_get
    if _newclass:usingDemoLicense = property(_lsf.licUsage_usingDemoLicense_get, _lsf.licUsage_usingDemoLicense_set)
    __swig_setmethods__["total"] = _lsf.licUsage_total_set
    __swig_getmethods__["total"] = _lsf.licUsage_total_get
    if _newclass:total = property(_lsf.licUsage_total_get, _lsf.licUsage_total_set)
    __swig_setmethods__["inUse"] = _lsf.licUsage_inUse_set
    __swig_getmethods__["inUse"] = _lsf.licUsage_inUse_get
    if _newclass:inUse = property(_lsf.licUsage_inUse_get, _lsf.licUsage_inUse_set)
    def __init__(self, *args): 
        this = _lsf.new_licUsage(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _lsf.delete_licUsage
    __del__ = lambda self : None;
licUsage_swigregister = _lsf.licUsage_swigregister
licUsage_swigregister(licUsage)

class hostClassInfo(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, hostClassInfo, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, hostClassInfo, name)
    __repr__ = _swig_repr
    __swig_setmethods__["numHosts"] = _lsf.hostClassInfo_numHosts_set
    __swig_getmethods__["numHosts"] = _lsf.hostClassInfo_numHosts_get
    if _newclass:numHosts = property(_lsf.hostClassInfo_numHosts_get, _lsf.hostClassInfo_numHosts_set)
    __swig_setmethods__["numCpus"] = _lsf.hostClassInfo_numCpus_set
    __swig_getmethods__["numCpus"] = _lsf.hostClassInfo_numCpus_get
    if _newclass:numCpus = property(_lsf.hostClassInfo_numCpus_get, _lsf.hostClassInfo_numCpus_set)
    __swig_setmethods__["numCores"] = _lsf.hostClassInfo_numCores_set
    __swig_getmethods__["numCores"] = _lsf.hostClassInfo_numCores_get
    if _newclass:numCores = property(_lsf.hostClassInfo_numCores_get, _lsf.hostClassInfo_numCores_set)
    def __init__(self, *args): 
        this = _lsf.new_hostClassInfo(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _lsf.delete_hostClassInfo
    __del__ = lambda self : None;
hostClassInfo_swigregister = _lsf.hostClassInfo_swigregister
hostClassInfo_swigregister(hostClassInfo)

class lsfLicUsage(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, lsfLicUsage, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, lsfLicUsage, name)
    __repr__ = _swig_repr
    __swig_setmethods__["licUsage"] = _lsf.lsfLicUsage_licUsage_set
    __swig_getmethods__["licUsage"] = _lsf.lsfLicUsage_licUsage_get
    if _newclass:licUsage = property(_lsf.lsfLicUsage_licUsage_get, _lsf.lsfLicUsage_licUsage_set)
    __swig_setmethods__["hostInfo"] = _lsf.lsfLicUsage_hostInfo_set
    __swig_getmethods__["hostInfo"] = _lsf.lsfLicUsage_hostInfo_get
    if _newclass:hostInfo = property(_lsf.lsfLicUsage_hostInfo_get, _lsf.lsfLicUsage_hostInfo_set)
    __swig_setmethods__["substitution"] = _lsf.lsfLicUsage_substitution_set
    __swig_getmethods__["substitution"] = _lsf.lsfLicUsage_substitution_get
    if _newclass:substitution = property(_lsf.lsfLicUsage_substitution_get, _lsf.lsfLicUsage_substitution_set)
    __swig_setmethods__["cluster"] = _lsf.lsfLicUsage_cluster_set
    __swig_getmethods__["cluster"] = _lsf.lsfLicUsage_cluster_get
    if _newclass:cluster = property(_lsf.lsfLicUsage_cluster_get, _lsf.lsfLicUsage_cluster_set)
    def __init__(self, *args): 
        this = _lsf.new_lsfLicUsage(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _lsf.delete_lsfLicUsage
    __del__ = lambda self : None;
lsfLicUsage_swigregister = _lsf.lsfLicUsage_swigregister
lsfLicUsage_swigregister(lsfLicUsage)

class limHostAnnReq(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, limHostAnnReq, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, limHostAnnReq, name)
    __repr__ = _swig_repr
    __swig_setmethods__["nhosts"] = _lsf.limHostAnnReq_nhosts_set
    __swig_getmethods__["nhosts"] = _lsf.limHostAnnReq_nhosts_get
    if _newclass:nhosts = property(_lsf.limHostAnnReq_nhosts_get, _lsf.limHostAnnReq_nhosts_set)
    __swig_setmethods__["hostnames"] = _lsf.limHostAnnReq_hostnames_set
    __swig_getmethods__["hostnames"] = _lsf.limHostAnnReq_hostnames_get
    if _newclass:hostnames = property(_lsf.limHostAnnReq_hostnames_get, _lsf.limHostAnnReq_hostnames_set)
    __swig_setmethods__["count"] = _lsf.limHostAnnReq_count_set
    __swig_getmethods__["count"] = _lsf.limHostAnnReq_count_get
    if _newclass:count = property(_lsf.limHostAnnReq_count_get, _lsf.limHostAnnReq_count_set)
    def __init__(self, *args): 
        this = _lsf.new_limHostAnnReq(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _lsf.delete_limHostAnnReq
    __del__ = lambda self : None;
limHostAnnReq_swigregister = _lsf.limHostAnnReq_swigregister
limHostAnnReq_swigregister(limHostAnnReq)

class param_entry(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, param_entry, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, param_entry, name)
    __repr__ = _swig_repr
    __swig_setmethods__["flags"] = _lsf.param_entry_flags_set
    __swig_getmethods__["flags"] = _lsf.param_entry_flags_get
    if _newclass:flags = property(_lsf.param_entry_flags_get, _lsf.param_entry_flags_set)
    __swig_setmethods__["key"] = _lsf.param_entry_key_set
    __swig_getmethods__["key"] = _lsf.param_entry_key_get
    if _newclass:key = property(_lsf.param_entry_key_get, _lsf.param_entry_key_set)
    __swig_setmethods__["value"] = _lsf.param_entry_value_set
    __swig_getmethods__["value"] = _lsf.param_entry_value_get
    if _newclass:value = property(_lsf.param_entry_value_get, _lsf.param_entry_value_set)
    __swig_setmethods__["default_value"] = _lsf.param_entry_default_value_set
    __swig_getmethods__["default_value"] = _lsf.param_entry_default_value_get
    if _newclass:default_value = property(_lsf.param_entry_default_value_get, _lsf.param_entry_default_value_set)
    def __init__(self, *args): 
        this = _lsf.new_param_entry(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _lsf.delete_param_entry
    __del__ = lambda self : None;
param_entry_swigregister = _lsf.param_entry_swigregister
param_entry_swigregister(param_entry)
HAS_PARAM_VALUE = _lsf.HAS_PARAM_VALUE
HAS_PARAM_DEFAULT = _lsf.HAS_PARAM_DEFAULT

class PKVP(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, PKVP, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, PKVP, name)
    __repr__ = _swig_repr
    __swig_setmethods__["num_params"] = _lsf.PKVP_num_params_set
    __swig_getmethods__["num_params"] = _lsf.PKVP_num_params_get
    if _newclass:num_params = property(_lsf.PKVP_num_params_get, _lsf.PKVP_num_params_set)
    __swig_setmethods__["daemon_time"] = _lsf.PKVP_daemon_time_set
    __swig_getmethods__["daemon_time"] = _lsf.PKVP_daemon_time_get
    if _newclass:daemon_time = property(_lsf.PKVP_daemon_time_get, _lsf.PKVP_daemon_time_set)
    __swig_setmethods__["param"] = _lsf.PKVP_param_set
    __swig_getmethods__["param"] = _lsf.PKVP_param_get
    if _newclass:param = property(_lsf.PKVP_param_get, _lsf.PKVP_param_set)
    def __init__(self, *args): 
        this = _lsf.new_PKVP(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _lsf.delete_PKVP
    __del__ = lambda self : None;
PKVP_swigregister = _lsf.PKVP_swigregister
PKVP_swigregister(PKVP)

class hRusage(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, hRusage, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, hRusage, name)
    __repr__ = _swig_repr
    __swig_setmethods__["name"] = _lsf.hRusage_name_set
    __swig_getmethods__["name"] = _lsf.hRusage_name_get
    if _newclass:name = property(_lsf.hRusage_name_get, _lsf.hRusage_name_set)
    __swig_setmethods__["mem"] = _lsf.hRusage_mem_set
    __swig_getmethods__["mem"] = _lsf.hRusage_mem_get
    if _newclass:mem = property(_lsf.hRusage_mem_get, _lsf.hRusage_mem_set)
    __swig_setmethods__["swap"] = _lsf.hRusage_swap_set
    __swig_getmethods__["swap"] = _lsf.hRusage_swap_get
    if _newclass:swap = property(_lsf.hRusage_swap_get, _lsf.hRusage_swap_set)
    __swig_setmethods__["utime"] = _lsf.hRusage_utime_set
    __swig_getmethods__["utime"] = _lsf.hRusage_utime_get
    if _newclass:utime = property(_lsf.hRusage_utime_get, _lsf.hRusage_utime_set)
    __swig_setmethods__["stime"] = _lsf.hRusage_stime_set
    __swig_getmethods__["stime"] = _lsf.hRusage_stime_get
    if _newclass:stime = property(_lsf.hRusage_stime_get, _lsf.hRusage_stime_set)
    __swig_setmethods__["hostExtendInfoPKVPs"] = _lsf.hRusage_hostExtendInfoPKVPs_set
    __swig_getmethods__["hostExtendInfoPKVPs"] = _lsf.hRusage_hostExtendInfoPKVPs_get
    if _newclass:hostExtendInfoPKVPs = property(_lsf.hRusage_hostExtendInfoPKVPs_get, _lsf.hRusage_hostExtendInfoPKVPs_set)
    def __init__(self, *args): 
        this = _lsf.new_hRusage(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _lsf.delete_hRusage
    __del__ = lambda self : None;
hRusage_swigregister = _lsf.hRusage_swigregister
hRusage_swigregister(hRusage)

LSE_NO_ERR = _lsf.LSE_NO_ERR
LSE_BAD_XDR = _lsf.LSE_BAD_XDR
LSE_MSG_SYS = _lsf.LSE_MSG_SYS
LSE_BAD_ARGS = _lsf.LSE_BAD_ARGS
LSE_MASTR_UNKNW = _lsf.LSE_MASTR_UNKNW
LSE_LIM_DOWN = _lsf.LSE_LIM_DOWN
LSE_PROTOC_LIM = _lsf.LSE_PROTOC_LIM
LSE_SOCK_SYS = _lsf.LSE_SOCK_SYS
LSE_ACCEPT_SYS = _lsf.LSE_ACCEPT_SYS
LSE_BAD_TASKF = _lsf.LSE_BAD_TASKF
LSE_NO_HOST = _lsf.LSE_NO_HOST
LSE_NO_ELHOST = _lsf.LSE_NO_ELHOST
LSE_TIME_OUT = _lsf.LSE_TIME_OUT
LSE_NIOS_DOWN = _lsf.LSE_NIOS_DOWN
LSE_LIM_DENIED = _lsf.LSE_LIM_DENIED
LSE_LIM_IGNORE = _lsf.LSE_LIM_IGNORE
LSE_LIM_BADHOST = _lsf.LSE_LIM_BADHOST
LSE_LIM_ALOCKED = _lsf.LSE_LIM_ALOCKED
LSE_LIM_NLOCKED = _lsf.LSE_LIM_NLOCKED
LSE_LIM_BADMOD = _lsf.LSE_LIM_BADMOD
LSE_SIG_SYS = _lsf.LSE_SIG_SYS
LSE_BAD_EXP = _lsf.LSE_BAD_EXP
LSE_NORCHILD = _lsf.LSE_NORCHILD
LSE_MALLOC = _lsf.LSE_MALLOC
LSE_LSFCONF = _lsf.LSE_LSFCONF
LSE_BAD_ENV = _lsf.LSE_BAD_ENV
LSE_LIM_NREG = _lsf.LSE_LIM_NREG
LSE_RES_NREG = _lsf.LSE_RES_NREG
LSE_RES_NOMORECONN = _lsf.LSE_RES_NOMORECONN
LSE_BADUSER = _lsf.LSE_BADUSER
LSE_RES_ROOTSECURE = _lsf.LSE_RES_ROOTSECURE
LSE_RES_DENIED = _lsf.LSE_RES_DENIED
LSE_BAD_OPCODE = _lsf.LSE_BAD_OPCODE
LSE_PROTOC_RES = _lsf.LSE_PROTOC_RES
LSE_RES_CALLBACK = _lsf.LSE_RES_CALLBACK
LSE_RES_NOMEM = _lsf.LSE_RES_NOMEM
LSE_RES_FATAL = _lsf.LSE_RES_FATAL
LSE_RES_PTY = _lsf.LSE_RES_PTY
LSE_RES_SOCK = _lsf.LSE_RES_SOCK
LSE_RES_FORK = _lsf.LSE_RES_FORK
LSE_NOMORE_SOCK = _lsf.LSE_NOMORE_SOCK
LSE_WDIR = _lsf.LSE_WDIR
LSE_LOSTCON = _lsf.LSE_LOSTCON
LSE_RES_INVCHILD = _lsf.LSE_RES_INVCHILD
LSE_RES_KILL = _lsf.LSE_RES_KILL
LSE_PTYMODE = _lsf.LSE_PTYMODE
LSE_BAD_HOST = _lsf.LSE_BAD_HOST
LSE_PROTOC_NIOS = _lsf.LSE_PROTOC_NIOS
LSE_WAIT_SYS = _lsf.LSE_WAIT_SYS
LSE_SETPARAM = _lsf.LSE_SETPARAM
LSE_RPIDLISTLEN = _lsf.LSE_RPIDLISTLEN
LSE_BAD_CLUSTER = _lsf.LSE_BAD_CLUSTER
LSE_RES_VERSION = _lsf.LSE_RES_VERSION
LSE_EXECV_SYS = _lsf.LSE_EXECV_SYS
LSE_RES_DIR = _lsf.LSE_RES_DIR
LSE_RES_DIRW = _lsf.LSE_RES_DIRW
LSE_BAD_SERVID = _lsf.LSE_BAD_SERVID
LSE_NLSF_HOST = _lsf.LSE_NLSF_HOST
LSE_UNKWN_RESNAME = _lsf.LSE_UNKWN_RESNAME
LSE_UNKWN_RESVALUE = _lsf.LSE_UNKWN_RESVALUE
LSE_TASKEXIST = _lsf.LSE_TASKEXIST
LSE_BAD_TID = _lsf.LSE_BAD_TID
LSE_TOOMANYTASK = _lsf.LSE_TOOMANYTASK
LSE_LIMIT_SYS = _lsf.LSE_LIMIT_SYS
LSE_BAD_NAMELIST = _lsf.LSE_BAD_NAMELIST
LSE_NO_LICENSE = _lsf.LSE_NO_LICENSE
LSE_LIM_NOMEM = _lsf.LSE_LIM_NOMEM
LSE_NIO_INIT = _lsf.LSE_NIO_INIT
LSE_CONF_SYNTAX = _lsf.LSE_CONF_SYNTAX
LSE_FILE_SYS = _lsf.LSE_FILE_SYS
LSE_CONN_SYS = _lsf.LSE_CONN_SYS
LSE_SELECT_SYS = _lsf.LSE_SELECT_SYS
LSE_EOF = _lsf.LSE_EOF
LSE_ACCT_FORMAT = _lsf.LSE_ACCT_FORMAT
LSE_BAD_TIME = _lsf.LSE_BAD_TIME
LSE_FORK = _lsf.LSE_FORK
LSE_PIPE = _lsf.LSE_PIPE
LSE_ESUB = _lsf.LSE_ESUB
LSE_DCE_EXEC = _lsf.LSE_DCE_EXEC
LSE_EAUTH = _lsf.LSE_EAUTH
LSE_NO_FILE = _lsf.LSE_NO_FILE
LSE_NO_CHAN = _lsf.LSE_NO_CHAN
LSE_BAD_CHAN = _lsf.LSE_BAD_CHAN
LSE_INTERNAL = _lsf.LSE_INTERNAL
LSE_PROTOCOL = _lsf.LSE_PROTOCOL
LSE_THRD_SYS = _lsf.LSE_THRD_SYS
LSE_MISC_SYS = _lsf.LSE_MISC_SYS
LSE_LOGON_FAIL = _lsf.LSE_LOGON_FAIL
LSE_RES_RUSAGE = _lsf.LSE_RES_RUSAGE
LSE_NO_RESOURCE = _lsf.LSE_NO_RESOURCE
LSE_BAD_RESOURCE = _lsf.LSE_BAD_RESOURCE
LSE_RES_PARENT = _lsf.LSE_RES_PARENT
LSE_NO_PASSWD = _lsf.LSE_NO_PASSWD
LSE_SUDOERS_CONF = _lsf.LSE_SUDOERS_CONF
LSE_SUDOERS_ROOT = _lsf.LSE_SUDOERS_ROOT
LSE_I18N_SETLC = _lsf.LSE_I18N_SETLC
LSE_I18N_CATOPEN = _lsf.LSE_I18N_CATOPEN
LSE_I18N_NOMEM = _lsf.LSE_I18N_NOMEM
LSE_NO_MEM = _lsf.LSE_NO_MEM
LSE_REGISTRY_SYS = _lsf.LSE_REGISTRY_SYS
LSE_FILE_CLOSE = _lsf.LSE_FILE_CLOSE
LSE_LIMCONF_NOTREADY = _lsf.LSE_LIMCONF_NOTREADY
LSE_MASTER_LIM_DOWN = _lsf.LSE_MASTER_LIM_DOWN
LSE_MLS_INVALID = _lsf.LSE_MLS_INVALID
LSE_MLS_CLEARANCE = _lsf.LSE_MLS_CLEARANCE
LSE_MLS_RHOST = _lsf.LSE_MLS_RHOST
LSE_MLS_DOMINATE = _lsf.LSE_MLS_DOMINATE
LSE_NO_CAL = _lsf.LSE_NO_CAL
LSE_NO_NETWORK = _lsf.LSE_NO_NETWORK
LSE_GETCONF_FAILED = _lsf.LSE_GETCONF_FAILED
LSE_TSSINIT = _lsf.LSE_TSSINIT
LSE_DYNM_DENIED = _lsf.LSE_DYNM_DENIED
LSE_LIC_OVERUSE = _lsf.LSE_LIC_OVERUSE
LSE_EGOCONF = _lsf.LSE_EGOCONF
LSE_BAD_EGO_ENV = _lsf.LSE_BAD_EGO_ENV
LSE_EGO_CONF_SYNTAX = _lsf.LSE_EGO_CONF_SYNTAX
LSE_EGO_GETCONF_FAILED = _lsf.LSE_EGO_GETCONF_FAILED
LSE_NS_LOOKUP = _lsf.LSE_NS_LOOKUP
LSE_BAD_PASSWD = _lsf.LSE_BAD_PASSWD
LSE_UNKWN_USER = _lsf.LSE_UNKWN_USER
LSE_NOT_WINHOST = _lsf.LSE_NOT_WINHOST
LSE_NOT_MASTERCAND = _lsf.LSE_NOT_MASTERCAND
LSE_HOST_UNAUTH = _lsf.LSE_HOST_UNAUTH
LSE_UNRESOLVALBE_HOST = _lsf.LSE_UNRESOLVALBE_HOST
LSE_RESOURCE_NOT_CONSUMABLE = _lsf.LSE_RESOURCE_NOT_CONSUMABLE
LSE_SHUTDOWN = _lsf.LSE_SHUTDOWN
LSE_BAD_SYNTAX = _lsf.LSE_BAD_SYNTAX
LSE_LIVE_PERSIST = _lsf.LSE_LIVE_PERSIST
LSE_LIVE_FAIL = _lsf.LSE_LIVE_FAIL
LSE_NERR = _lsf.LSE_NERR
class LS_TIMEVAL_T(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, LS_TIMEVAL_T, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, LS_TIMEVAL_T, name)
    __repr__ = _swig_repr
    __swig_setmethods__["rtime"] = _lsf.LS_TIMEVAL_T_rtime_set
    __swig_getmethods__["rtime"] = _lsf.LS_TIMEVAL_T_rtime_get
    if _newclass:rtime = property(_lsf.LS_TIMEVAL_T_rtime_get, _lsf.LS_TIMEVAL_T_rtime_set)
    __swig_setmethods__["utime"] = _lsf.LS_TIMEVAL_T_utime_set
    __swig_getmethods__["utime"] = _lsf.LS_TIMEVAL_T_utime_get
    if _newclass:utime = property(_lsf.LS_TIMEVAL_T_utime_get, _lsf.LS_TIMEVAL_T_utime_set)
    __swig_setmethods__["stime"] = _lsf.LS_TIMEVAL_T_stime_set
    __swig_getmethods__["stime"] = _lsf.LS_TIMEVAL_T_stime_get
    if _newclass:stime = property(_lsf.LS_TIMEVAL_T_stime_get, _lsf.LS_TIMEVAL_T_stime_set)
    def __init__(self, *args): 
        this = _lsf.new_LS_TIMEVAL_T(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _lsf.delete_LS_TIMEVAL_T
    __del__ = lambda self : None;
LS_TIMEVAL_T_swigregister = _lsf.LS_TIMEVAL_T_swigregister
LS_TIMEVAL_T_swigregister(LS_TIMEVAL_T)

LC_SCHED = _lsf.LC_SCHED
LC_EXEC = _lsf.LC_EXEC
LC_TRACE = _lsf.LC_TRACE
LC_COMM = _lsf.LC_COMM
LC_XDR = _lsf.LC_XDR
LC_CHKPNT = _lsf.LC_CHKPNT
LC_LICENCE = _lsf.LC_LICENCE
LC_LICENSE = _lsf.LC_LICENSE
LC_FILE = _lsf.LC_FILE
LC_AFS = _lsf.LC_AFS
LC_AUTH = _lsf.LC_AUTH
LC_HANG = _lsf.LC_HANG
LC_MULTI = _lsf.LC_MULTI
LC_SIGNAL = _lsf.LC_SIGNAL
LC_DCE = _lsf.LC_DCE
LC_PIM = _lsf.LC_PIM
LC_MEMORY = _lsf.LC_MEMORY
LC_SYS = _lsf.LC_SYS
LC_JLIMIT = _lsf.LC_JLIMIT
LC_FAIR = _lsf.LC_FAIR
LC_PREEMPT = _lsf.LC_PREEMPT
LC_PEND = _lsf.LC_PEND
LC_EEVENTD = _lsf.LC_EEVENTD
LC_LOADINDX = _lsf.LC_LOADINDX
LC_RESOURCE = _lsf.LC_RESOURCE
LC_JGRP = _lsf.LC_JGRP
LC_JARRAY = _lsf.LC_JARRAY
LC_MPI = _lsf.LC_MPI
LC_ELIM = _lsf.LC_ELIM
LC_M_LOG = _lsf.LC_M_LOG
LC_PERFM = _lsf.LC_PERFM
LC_DLOG = _lsf.LC_DLOG
LC_HPC = _lsf.LC_HPC
LC_LICSCHED = _lsf.LC_LICSCHED
LC_XDRVERSION = _lsf.LC_XDRVERSION
LC_FLEX = _lsf.LC_FLEX
LC_ADVRSV = _lsf.LC_ADVRSV
LC_RESREQ = _lsf.LC_RESREQ
LC2_SCHED = _lsf.LC2_SCHED
LC2_EXEC = _lsf.LC2_EXEC
LC2_TRACE = _lsf.LC2_TRACE
LC2_COMM = _lsf.LC2_COMM
LC2_XDR = _lsf.LC2_XDR
LC2_CHKPNT = _lsf.LC2_CHKPNT
LC2_LICENCE = _lsf.LC2_LICENCE
LC2_LICENSE = _lsf.LC2_LICENSE
LC2_FILE = _lsf.LC2_FILE
LC2_AFS = _lsf.LC2_AFS
LC2_AUTH = _lsf.LC2_AUTH
LC2_HANG = _lsf.LC2_HANG
LC2_MULTI = _lsf.LC2_MULTI
LC2_SIGNAL = _lsf.LC2_SIGNAL
LC2_DCE = _lsf.LC2_DCE
LC2_PIM = _lsf.LC2_PIM
LC2_MEMORY = _lsf.LC2_MEMORY
LC2_SYS = _lsf.LC2_SYS
LC2_JLIMIT = _lsf.LC2_JLIMIT
LC2_FAIR = _lsf.LC2_FAIR
LC2_PREEMPT = _lsf.LC2_PREEMPT
LC2_PEND = _lsf.LC2_PEND
LC2_EEVENTD = _lsf.LC2_EEVENTD
LC2_LOADINDX = _lsf.LC2_LOADINDX
LC2_RESOURCE = _lsf.LC2_RESOURCE
LC2_JGRP = _lsf.LC2_JGRP
LC2_JARRAY = _lsf.LC2_JARRAY
LC2_MPI = _lsf.LC2_MPI
LC2_ELIM = _lsf.LC2_ELIM
LC2_M_LOG = _lsf.LC2_M_LOG
LC2_PERFM = _lsf.LC2_PERFM
LC2_DLOG = _lsf.LC2_DLOG
LC2_HPC = _lsf.LC2_HPC
LC2_LICSCHED = _lsf.LC2_LICSCHED
LC2_XDRVERSION = _lsf.LC2_XDRVERSION
LC2_FLEX = _lsf.LC2_FLEX
LC2_ADVRSV = _lsf.LC2_ADVRSV
LC2_RESREQ = _lsf.LC2_RESREQ
LC2_USER1 = _lsf.LC2_USER1
LC2_USER2 = _lsf.LC2_USER2
LC2_SCHMOD_DEFAULT = _lsf.LC2_SCHMOD_DEFAULT
LC2_SCHMOD_FCFS = _lsf.LC2_SCHMOD_FCFS
LC2_SCHMOD_FAIRSHARE = _lsf.LC2_SCHMOD_FAIRSHARE
LC2_SCHMOD_LIMIT = _lsf.LC2_SCHMOD_LIMIT
LC2_SCHMOD_PARALLEL = _lsf.LC2_SCHMOD_PARALLEL
LC2_SCHMOD_RESERVE = _lsf.LC2_SCHMOD_RESERVE
LC2_SCHMOD_MC = _lsf.LC2_SCHMOD_MC
LC2_SCHMOD_PREEMPTION = _lsf.LC2_SCHMOD_PREEMPTION
LC2_SCHMOD_ADVRSV = _lsf.LC2_SCHMOD_ADVRSV
LC2_SCHMOD_PS = _lsf.LC2_SCHMOD_PS
LC2_SCHMOD_APS = _lsf.LC2_SCHMOD_APS
LC2_SCHMOD_CPUSET = _lsf.LC2_SCHMOD_CPUSET
LC2_GUARANTEE = _lsf.LC2_GUARANTEE
LC2_INTERNAL_TEST = _lsf.LC2_INTERNAL_TEST
LC2_LIVECONF = _lsf.LC2_LIVECONF
LC2_PERFTIME = _lsf.LC2_PERFTIME
LSF_EVENT_LIM_DOWN = _lsf.LSF_EVENT_LIM_DOWN
LSF_EVENT_RES_DOWN = _lsf.LSF_EVENT_RES_DOWN
LSF_EVENT_SBD_DOWN = _lsf.LSF_EVENT_SBD_DOWN
LSF_EVENT_HOST_UNLIC = _lsf.LSF_EVENT_HOST_UNLIC
LSF_EVENT_MASTER_ELECT = _lsf.LSF_EVENT_MASTER_ELECT
LSF_EVENT_MASTER_RESIGN = _lsf.LSF_EVENT_MASTER_RESIGN
LSF_EVENT_MBD_UP = _lsf.LSF_EVENT_MBD_UP
LSF_EVENT_MBD_DOWN = _lsf.LSF_EVENT_MBD_DOWN
LSF_EVENT_MBD_RECONFIG = _lsf.LSF_EVENT_MBD_RECONFIG
LSF_EVENT_WORKDIR_FULL = _lsf.LSF_EVENT_WORKDIR_FULL
LSF_EVENT_HOST_OPENED = _lsf.LSF_EVENT_HOST_OPENED
LSF_EVENT_HOST_CLOSED = _lsf.LSF_EVENT_HOST_CLOSED
LSF_EVENT_QUEUE_OPENED = _lsf.LSF_EVENT_QUEUE_OPENED
LSF_EVENT_QUEUE_CLOSED = _lsf.LSF_EVENT_QUEUE_CLOSED
LSF_EVENT_SCH_DOWN = _lsf.LSF_EVENT_SCH_DOWN
LSF_EVENT_LIC_OVERUSE = _lsf.LSF_EVENT_LIC_OVERUSE
LSF_NIOS_REQUEUE = _lsf.LSF_NIOS_REQUEUE
ls_readconfenv = _lsf.ls_readconfenv
ls_placereq = _lsf.ls_placereq
ls_placeofhosts = _lsf.ls_placeofhosts
ls_load = _lsf.ls_load
ls_loadofhosts = _lsf.ls_loadofhosts
ls_loadinfo = _lsf.ls_loadinfo
ls_loadadj = _lsf.ls_loadadj
ls_eligible = _lsf.ls_eligible
ls_resreq = _lsf.ls_resreq
ls_insertrtask = _lsf.ls_insertrtask
ls_insertltask = _lsf.ls_insertltask
ls_deletertask = _lsf.ls_deletertask
ls_deleteltask = _lsf.ls_deleteltask
ls_listrtask = _lsf.ls_listrtask
ls_listltask = _lsf.ls_listltask
ls_findmyconnections = _lsf.ls_findmyconnections
ls_isconnected = _lsf.ls_isconnected
ls_getclustername = _lsf.ls_getclustername
ls_clusterinfo = _lsf.ls_clusterinfo
ls_sharedresourceinfo = _lsf.ls_sharedresourceinfo
ls_getmastername = _lsf.ls_getmastername
ls_getmyhostname = _lsf.ls_getmyhostname
ls_getmyhostname2 = _lsf.ls_getmyhostname2
ls_gethostinfo = _lsf.ls_gethostinfo
ls_getISVmode = _lsf.ls_getISVmode
ls_isshutdown = _lsf.ls_isshutdown
ls_isPartialLicensingEnabled = _lsf.ls_isPartialLicensingEnabled
ls_getLicenseUsage = _lsf.ls_getLicenseUsage
ls_info = _lsf.ls_info
ls_indexnames = _lsf.ls_indexnames
ls_isclustername = _lsf.ls_isclustername
ls_gethosttype = _lsf.ls_gethosttype
ls_getmodelfactor = _lsf.ls_getmodelfactor
ls_gethostfactor = _lsf.ls_gethostfactor
ls_gethostmodel = _lsf.ls_gethostmodel
ls_lockhost = _lsf.ls_lockhost
ls_unlockhost = _lsf.ls_unlockhost
ls_limcontrol = _lsf.ls_limcontrol
ls_remtty = _lsf.ls_remtty
ls_loctty = _lsf.ls_loctty
ls_sysmsg = _lsf.ls_sysmsg
ls_perror = _lsf.ls_perror
ls_getconf = _lsf.ls_getconf
ls_freeconf = _lsf.ls_freeconf
ls_readshared = _lsf.ls_readshared
ls_readcluster = _lsf.ls_readcluster
ls_readcluster_ex = _lsf.ls_readcluster_ex
_ls_initdebug = _lsf._ls_initdebug
ls_syslog = _lsf.ls_syslog
ls_errlog = _lsf.ls_errlog
ls_fdbusy = _lsf.ls_fdbusy
ls_getmnthost = _lsf.ls_getmnthost
ls_servavail = _lsf.ls_servavail
ls_getpriority = _lsf.ls_getpriority
ls_setpriority = _lsf.ls_setpriority
ls_ruunix2lsf = _lsf.ls_ruunix2lsf
ls_rulsf2unix = _lsf.ls_rulsf2unix
cleanLsfRusage = _lsf.cleanLsfRusage
cleanRusage = _lsf.cleanRusage
ls_postevent = _lsf.ls_postevent
ls_postmultievent = _lsf.ls_postmultievent
ls_limhostann = _lsf.ls_limhostann
class extResInfo(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, extResInfo, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, extResInfo, name)
    __repr__ = _swig_repr
    __swig_setmethods__["name"] = _lsf.extResInfo_name_set
    __swig_getmethods__["name"] = _lsf.extResInfo_name_get
    if _newclass:name = property(_lsf.extResInfo_name_get, _lsf.extResInfo_name_set)
    __swig_setmethods__["type"] = _lsf.extResInfo_type_set
    __swig_getmethods__["type"] = _lsf.extResInfo_type_get
    if _newclass:type = property(_lsf.extResInfo_type_get, _lsf.extResInfo_type_set)
    __swig_setmethods__["interval"] = _lsf.extResInfo_interval_set
    __swig_getmethods__["interval"] = _lsf.extResInfo_interval_get
    if _newclass:interval = property(_lsf.extResInfo_interval_get, _lsf.extResInfo_interval_set)
    __swig_setmethods__["increasing"] = _lsf.extResInfo_increasing_set
    __swig_getmethods__["increasing"] = _lsf.extResInfo_increasing_get
    if _newclass:increasing = property(_lsf.extResInfo_increasing_get, _lsf.extResInfo_increasing_set)
    __swig_setmethods__["des"] = _lsf.extResInfo_des_set
    __swig_getmethods__["des"] = _lsf.extResInfo_des_get
    if _newclass:des = property(_lsf.extResInfo_des_get, _lsf.extResInfo_des_set)
    def __init__(self, *args): 
        this = _lsf.new_extResInfo(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _lsf.delete_extResInfo
    __del__ = lambda self : None;
extResInfo_swigregister = _lsf.extResInfo_swigregister
extResInfo_swigregister(extResInfo)

MAXFULLFILENAMELEN = _lsf.MAXFULLFILENAMELEN
MAXFULLPATHNAMELEN = _lsf.MAXFULLPATHNAMELEN
MAXFULLMSGSIZE = _lsf.MAXFULLMSGSIZE
UNKNOWN_AUTO_DETECT = _lsf.UNKNOWN_AUTO_DETECT
LiC_ACTION_ADDMEMBER = _lsf.LiC_ACTION_ADDMEMBER
LiC_ACTION_RMMEMBER = _lsf.LiC_ACTION_RMMEMBER
LiC_ACTION_UPDATE = _lsf.LiC_ACTION_UPDATE
LiC_ACTION_CREATE = _lsf.LiC_ACTION_CREATE
LiC_ACTION_DELETE = _lsf.LiC_ACTION_DELETE
LiC_ACTION_ENFORCEDELETE = _lsf.LiC_ACTION_ENFORCEDELETE
LiC_ACTION_DISABLE = _lsf.LiC_ACTION_DISABLE
LiC_ACTION_END = _lsf.LiC_ACTION_END
LiC_OBJECT_USER = _lsf.LiC_OBJECT_USER
LiC_OBJECT_USERGROUP = _lsf.LiC_OBJECT_USERGROUP
LiC_OBJECT_HOST = _lsf.LiC_OBJECT_HOST
LiC_OBJECT_HOSTGROUP = _lsf.LiC_OBJECT_HOSTGROUP
LiC_OBJECT_HOSTPARTITION = _lsf.LiC_OBJECT_HOSTPARTITION
LiC_OBJECT_QUEUE = _lsf.LiC_OBJECT_QUEUE
LiC_OBJECT_LIMIT = _lsf.LiC_OBJECT_LIMIT
LiC_OBJECT_APPLICATION = _lsf.LiC_OBJECT_APPLICATION
LiC_OBJECT_COMPUTEUNIT = _lsf.LiC_OBJECT_COMPUTEUNIT
LiC_OBJECT_GUARPOOL = _lsf.LiC_OBJECT_GUARPOOL
LiC_OBJECT_SERVICECLASS = _lsf.LiC_OBJECT_SERVICECLASS
LiC_OBJECT_ADVRSV = _lsf.LiC_OBJECT_ADVRSV
LiC_OBJECT_RESOURCEMAP = _lsf.LiC_OBJECT_RESOURCEMAP
LiC_OBJECT_RESOURCERSV = _lsf.LiC_OBJECT_RESOURCERSV
LiC_OBJECT_BASE_HOST = _lsf.LiC_OBJECT_BASE_HOST
LiC_OBJECT_END = _lsf.LiC_OBJECT_END
class LiveConfReq(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, LiveConfReq, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, LiveConfReq, name)
    __repr__ = _swig_repr
    __swig_setmethods__["actions"] = _lsf.LiveConfReq_actions_set
    __swig_getmethods__["actions"] = _lsf.LiveConfReq_actions_get
    if _newclass:actions = property(_lsf.LiveConfReq_actions_get, _lsf.LiveConfReq_actions_set)
    __swig_setmethods__["object_type"] = _lsf.LiveConfReq_object_type_set
    __swig_getmethods__["object_type"] = _lsf.LiveConfReq_object_type_get
    if _newclass:object_type = property(_lsf.LiveConfReq_object_type_get, _lsf.LiveConfReq_object_type_set)
    __swig_setmethods__["identity"] = _lsf.LiveConfReq_identity_set
    __swig_getmethods__["identity"] = _lsf.LiveConfReq_identity_get
    if _newclass:identity = property(_lsf.LiveConfReq_identity_get, _lsf.LiveConfReq_identity_set)
    __swig_setmethods__["key_value"] = _lsf.LiveConfReq_key_value_set
    __swig_getmethods__["key_value"] = _lsf.LiveConfReq_key_value_get
    if _newclass:key_value = property(_lsf.LiveConfReq_key_value_get, _lsf.LiveConfReq_key_value_set)
    __swig_setmethods__["comments"] = _lsf.LiveConfReq_comments_set
    __swig_getmethods__["comments"] = _lsf.LiveConfReq_comments_get
    if _newclass:comments = property(_lsf.LiveConfReq_comments_get, _lsf.LiveConfReq_comments_set)
    __swig_setmethods__["seq"] = _lsf.LiveConfReq_seq_set
    __swig_getmethods__["seq"] = _lsf.LiveConfReq_seq_get
    if _newclass:seq = property(_lsf.LiveConfReq_seq_get, _lsf.LiveConfReq_seq_set)
    def __init__(self, *args): 
        this = _lsf.new_LiveConfReq(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _lsf.delete_LiveConfReq
    __del__ = lambda self : None;
LiveConfReq_swigregister = _lsf.LiveConfReq_swigregister
LiveConfReq_swigregister(LiveConfReq)

LiC_REMOVE_ACTIVE_REQ = _lsf.LiC_REMOVE_ACTIVE_REQ
LSF_VERSION = _lsf.LSF_VERSION
LSF_CURRENT_VERSION = _lsf.LSF_CURRENT_VERSION
LSF_PRODUCT_COPYRIGHT_STR = _lsf.LSF_PRODUCT_COPYRIGHT_STR
LSF_NAME_STR = _lsf.LSF_NAME_STR
LSF_IDENTIFIER_STR = _lsf.LSF_IDENTIFIER_STR
LSF_PRODUCT_NAME_STR = _lsf.LSF_PRODUCT_NAME_STR
LSF_PRODUCT_COMMENT_STR = _lsf.LSF_PRODUCT_COMMENT_STR
LSF_PRODUCT_BUILD_STR = _lsf.LSF_PRODUCT_BUILD_STR
LSF_PRODUCT_MAJOR_VERSION = _lsf.LSF_PRODUCT_MAJOR_VERSION
LSF_PRODUCT_MINOR_VERSION = _lsf.LSF_PRODUCT_MINOR_VERSION
LSF_PRODUCT_MAINTAIN_VERSION = _lsf.LSF_PRODUCT_MAINTAIN_VERSION
LSF_PRODUCT_MAJOR_VERSION_STR = _lsf.LSF_PRODUCT_MAJOR_VERSION_STR
LSF_PRODUCT_MINOR_VERSION_STR = _lsf.LSF_PRODUCT_MINOR_VERSION_STR
LSF_PRODUCT_MAINTAIN_VERSION_STR = _lsf.LSF_PRODUCT_MAINTAIN_VERSION_STR
LSF_PRODUCT_VERSION_STR = _lsf.LSF_PRODUCT_VERSION_STR
LSF_FILE_VERSION_STR = _lsf.LSF_FILE_VERSION_STR
WIN_VERSION_NUMBER = _lsf.WIN_VERSION_NUMBER
_VERSION_STR_LSID_ = _lsf._VERSION_STR_LSID_
NIO_STDIN_ON = _lsf.NIO_STDIN_ON
NIO_STDIN_OFF = _lsf.NIO_STDIN_OFF
NIO_TAGSTDOUT_ON = _lsf.NIO_TAGSTDOUT_ON
NIO_TAGSTDOUT_OFF = _lsf.NIO_TAGSTDOUT_OFF
NIO_TASK_STDINON = _lsf.NIO_TASK_STDINON
NIO_TASK_STDINOFF = _lsf.NIO_TASK_STDINOFF
NIO_TASK_ALL = _lsf.NIO_TASK_ALL
NIO_TASK_CONNECTED = _lsf.NIO_TASK_CONNECTED
NIO_STATUS = _lsf.NIO_STATUS
NIO_STDOUT = _lsf.NIO_STDOUT
NIO_EOF = _lsf.NIO_EOF
NIO_IOERR = _lsf.NIO_IOERR
NIO_REQUEUE = _lsf.NIO_REQUEUE
NIO_STDERR = _lsf.NIO_STDERR
class nioEvent(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, nioEvent, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, nioEvent, name)
    __repr__ = _swig_repr
    __swig_setmethods__["tid"] = _lsf.nioEvent_tid_set
    __swig_getmethods__["tid"] = _lsf.nioEvent_tid_get
    if _newclass:tid = property(_lsf.nioEvent_tid_get, _lsf.nioEvent_tid_set)
    __swig_setmethods__["type"] = _lsf.nioEvent_type_set
    __swig_getmethods__["type"] = _lsf.nioEvent_type_get
    if _newclass:type = property(_lsf.nioEvent_type_get, _lsf.nioEvent_type_set)
    __swig_setmethods__["status"] = _lsf.nioEvent_status_set
    __swig_getmethods__["status"] = _lsf.nioEvent_status_get
    if _newclass:status = property(_lsf.nioEvent_status_get, _lsf.nioEvent_status_set)
    def __init__(self, *args): 
        this = _lsf.new_nioEvent(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _lsf.delete_nioEvent
    __del__ = lambda self : None;
nioEvent_swigregister = _lsf.nioEvent_swigregister
nioEvent_swigregister(nioEvent)

class nioInfo(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, nioInfo, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, nioInfo, name)
    __repr__ = _swig_repr
    __swig_setmethods__["num"] = _lsf.nioInfo_num_set
    __swig_getmethods__["num"] = _lsf.nioInfo_num_get
    if _newclass:num = property(_lsf.nioInfo_num_get, _lsf.nioInfo_num_set)
    __swig_setmethods__["ioTask"] = _lsf.nioInfo_ioTask_set
    __swig_getmethods__["ioTask"] = _lsf.nioInfo_ioTask_get
    if _newclass:ioTask = property(_lsf.nioInfo_ioTask_get, _lsf.nioInfo_ioTask_set)
    def __init__(self, *args): 
        this = _lsf.new_nioInfo(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _lsf.delete_nioInfo
    __del__ = lambda self : None;
nioInfo_swigregister = _lsf.nioInfo_swigregister
nioInfo_swigregister(nioInfo)

ls_initdebug = _lsf.ls_initdebug
ls_initrex = _lsf.ls_initrex
ls_donerex = _lsf.ls_donerex
ls_niossync = _lsf.ls_niossync
ls_setstdin = _lsf.ls_setstdin
ls_getstdin = _lsf.ls_getstdin
ls_setstdout = _lsf.ls_setstdout
ls_stdinmode = _lsf.ls_stdinmode
ls_stoprex = _lsf.ls_stoprex
ls_chdir = _lsf.ls_chdir
ls_connect = _lsf.ls_connect
ls_rkill = _lsf.ls_rkill
ls_rsetenv = _lsf.ls_rsetenv
ls_rsetenv_async = _lsf.ls_rsetenv_async
ls_rescontrol = _lsf.ls_rescontrol
ls_getacctrec = _lsf.ls_getacctrec
ls_getacctrec_ext = _lsf.ls_getacctrec_ext
ls_putacctrec = _lsf.ls_putacctrec
ls_putacctrec_ext = _lsf.ls_putacctrec_ext
ls_rexecv = _lsf.ls_rexecv
ls_rexecve = _lsf.ls_rexecve
ls_rexecv2 = _lsf.ls_rexecv2
ls_startserver = _lsf.ls_startserver
ls_rtask = _lsf.ls_rtask
ls_rtaske = _lsf.ls_rtaske
ls_rtask2 = _lsf.ls_rtask2
ls_rwait = _lsf.ls_rwait
ls_rwaittid = _lsf.ls_rwaittid
ls_conntaskport = _lsf.ls_conntaskport
ls_ropen = _lsf.ls_ropen
ls_rclose = _lsf.ls_rclose
ls_rwrite = _lsf.ls_rwrite
ls_rread = _lsf.ls_rread
ls_rlseek = _lsf.ls_rlseek
ls_runlink = _lsf.ls_runlink
ls_rfstat = _lsf.ls_rfstat
ls_rstat = _lsf.ls_rstat
ls_rgetmnthost = _lsf.ls_rgetmnthost
ls_rfcontrol = _lsf.ls_rfcontrol
ls_rfterminate = _lsf.ls_rfterminate
class ls_task_params_t(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, ls_task_params_t, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, ls_task_params_t, name)
    __repr__ = _swig_repr
    __swig_setmethods__["cmdline"] = _lsf.ls_task_params_t_cmdline_set
    __swig_getmethods__["cmdline"] = _lsf.ls_task_params_t_cmdline_get
    if _newclass:cmdline = property(_lsf.ls_task_params_t_cmdline_get, _lsf.ls_task_params_t_cmdline_set)
    __swig_setmethods__["node"] = _lsf.ls_task_params_t_node_set
    __swig_getmethods__["node"] = _lsf.ls_task_params_t_node_get
    if _newclass:node = property(_lsf.ls_task_params_t_node_get, _lsf.ls_task_params_t_node_set)
    __swig_setmethods__["env"] = _lsf.ls_task_params_t_env_set
    __swig_getmethods__["env"] = _lsf.ls_task_params_t_env_get
    if _newclass:env = property(_lsf.ls_task_params_t_env_get, _lsf.ls_task_params_t_env_set)
    def __init__(self, *args): 
        this = _lsf.new_ls_task_params_t(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _lsf.delete_ls_task_params_t
    __del__ = lambda self : None;
ls_task_params_t_swigregister = _lsf.ls_task_params_t_swigregister
ls_task_params_t_swigregister(ls_task_params_t)

class ls_task_t(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, ls_task_t, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, ls_task_t, name)
    __repr__ = _swig_repr
    __swig_setmethods__["params"] = _lsf.ls_task_t_params_set
    __swig_getmethods__["params"] = _lsf.ls_task_t_params_get
    if _newclass:params = property(_lsf.ls_task_t_params_get, _lsf.ls_task_t_params_set)
    __swig_setmethods__["pid"] = _lsf.ls_task_t_pid_set
    __swig_getmethods__["pid"] = _lsf.ls_task_t_pid_get
    if _newclass:pid = property(_lsf.ls_task_t_pid_get, _lsf.ls_task_t_pid_set)
    __swig_setmethods__["taskId"] = _lsf.ls_task_t_taskId_set
    __swig_getmethods__["taskId"] = _lsf.ls_task_t_taskId_get
    if _newclass:taskId = property(_lsf.ls_task_t_taskId_get, _lsf.ls_task_t_taskId_set)
    def __init__(self, *args): 
        this = _lsf.new_ls_task_t(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _lsf.delete_ls_task_t
    __del__ = lambda self : None;
ls_task_t_swigregister = _lsf.ls_task_t_swigregister
ls_task_t_swigregister(ls_task_t)

class rmi_buffer_t(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, rmi_buffer_t, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, rmi_buffer_t, name)
    __repr__ = _swig_repr
    __swig_setmethods__["invoker_url"] = _lsf.rmi_buffer_t_invoker_url_set
    __swig_getmethods__["invoker_url"] = _lsf.rmi_buffer_t_invoker_url_get
    if _newclass:invoker_url = property(_lsf.rmi_buffer_t_invoker_url_get, _lsf.rmi_buffer_t_invoker_url_set)
    __swig_setmethods__["storage"] = _lsf.rmi_buffer_t_storage_set
    __swig_getmethods__["storage"] = _lsf.rmi_buffer_t_storage_get
    if _newclass:storage = property(_lsf.rmi_buffer_t_storage_get, _lsf.rmi_buffer_t_storage_set)
    __swig_setmethods__["size"] = _lsf.rmi_buffer_t_size_set
    __swig_getmethods__["size"] = _lsf.rmi_buffer_t_size_get
    if _newclass:size = property(_lsf.rmi_buffer_t_size_get, _lsf.rmi_buffer_t_size_set)
    def __init__(self, *args): 
        this = _lsf.new_rmi_buffer_t(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _lsf.delete_rmi_buffer_t
    __del__ = lambda self : None;
rmi_buffer_t_swigregister = _lsf.rmi_buffer_t_swigregister
rmi_buffer_t_swigregister(rmi_buffer_t)

class rmi_handler_t(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, rmi_handler_t, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, rmi_handler_t, name)
    __repr__ = _swig_repr
    __swig_setmethods__["handler_name"] = _lsf.rmi_handler_t_handler_name_set
    __swig_getmethods__["handler_name"] = _lsf.rmi_handler_t_handler_name_get
    if _newclass:handler_name = property(_lsf.rmi_handler_t_handler_name_get, _lsf.rmi_handler_t_handler_name_set)
    __swig_setmethods__["handler"] = _lsf.rmi_handler_t_handler_set
    __swig_getmethods__["handler"] = _lsf.rmi_handler_t_handler_get
    if _newclass:handler = property(_lsf.rmi_handler_t_handler_get, _lsf.rmi_handler_t_handler_set)
    __swig_setmethods__["desc"] = _lsf.rmi_handler_t_desc_set
    __swig_getmethods__["desc"] = _lsf.rmi_handler_t_desc_get
    if _newclass:desc = property(_lsf.rmi_handler_t_desc_get, _lsf.rmi_handler_t_desc_set)
    def __init__(self, *args): 
        this = _lsf.new_rmi_handler_t(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _lsf.delete_rmi_handler_t
    __del__ = lambda self : None;
rmi_handler_t_swigregister = _lsf.rmi_handler_t_swigregister
rmi_handler_t_swigregister(rmi_handler_t)

DEF_MAXJOBS_PER_PACK = _lsf.DEF_MAXJOBS_PER_PACK
_PATH_NULL = _lsf._PATH_NULL
LSB_EVENT_VERSION3_0 = _lsf.LSB_EVENT_VERSION3_0
LSB_EVENT_VERSION3_1 = _lsf.LSB_EVENT_VERSION3_1
LSB_EVENT_VERSION3_2 = _lsf.LSB_EVENT_VERSION3_2
LSB_EVENT_VERSION4_0 = _lsf.LSB_EVENT_VERSION4_0
LSB_EVENT_VERSION4_1 = _lsf.LSB_EVENT_VERSION4_1
LSB_EVENT_VERSION4_2 = _lsf.LSB_EVENT_VERSION4_2
LSB_EVENT_VERSION5_0 = _lsf.LSB_EVENT_VERSION5_0
LSB_EVENT_VERSION5_1 = _lsf.LSB_EVENT_VERSION5_1
LSB_EVENT_VERSION6_0 = _lsf.LSB_EVENT_VERSION6_0
LSB_EVENT_VERSION6_1 = _lsf.LSB_EVENT_VERSION6_1
LSB_EVENT_VERSION6_2 = _lsf.LSB_EVENT_VERSION6_2
LSB_EVENT_VERSION7_0 = _lsf.LSB_EVENT_VERSION7_0
LSB_EVENT_VERSION7_0_1 = _lsf.LSB_EVENT_VERSION7_0_1
LSB_EVENT_VERSION7_0_2 = _lsf.LSB_EVENT_VERSION7_0_2
LSB_EVENT_VERSION7_0_3 = _lsf.LSB_EVENT_VERSION7_0_3
LSB_EVENT_VERSION7_0_4 = _lsf.LSB_EVENT_VERSION7_0_4
LSB_EVENT_VERSION7_0_5 = _lsf.LSB_EVENT_VERSION7_0_5
LSB_EVENT_VERSION7_0_6 = _lsf.LSB_EVENT_VERSION7_0_6
LSB_EVENT_VERSION8_0 = _lsf.LSB_EVENT_VERSION8_0
THIS_VERSION = _lsf.THIS_VERSION
MAX_VERSION_LEN = _lsf.MAX_VERSION_LEN
MAX_HPART_USERS = _lsf.MAX_HPART_USERS
MAX_CHARLEN = _lsf.MAX_CHARLEN
MAX_LSB_NAME_LEN = _lsf.MAX_LSB_NAME_LEN
MAX_LSB_UG_NAME_LEN = _lsf.MAX_LSB_UG_NAME_LEN
MAX_LSB_HG_NAME_LEN = _lsf.MAX_LSB_HG_NAME_LEN
MAX_LSB_UG_HIERDEPTH = _lsf.MAX_LSB_UG_HIERDEPTH
MAX_CMD_DESC_LEN = _lsf.MAX_CMD_DESC_LEN
MAX_CALENDARS = _lsf.MAX_CALENDARS
MAX_USER_EQUIVALENT = _lsf.MAX_USER_EQUIVALENT
MAX_USER_MAPPING = _lsf.MAX_USER_MAPPING
MAXDESCLEN = _lsf.MAXDESCLEN
MAX_GROUPS = _lsf.MAX_GROUPS
FILENAMEPADDING = _lsf.FILENAMEPADDING
DEFAULT_MSG_DESC = _lsf.DEFAULT_MSG_DESC
MSGSIZE = _lsf.MSGSIZE
HOST_STAT_OK = _lsf.HOST_STAT_OK
HOST_STAT_BUSY = _lsf.HOST_STAT_BUSY
HOST_STAT_WIND = _lsf.HOST_STAT_WIND
HOST_STAT_DISABLED = _lsf.HOST_STAT_DISABLED
HOST_STAT_LOCKED = _lsf.HOST_STAT_LOCKED
HOST_STAT_FULL = _lsf.HOST_STAT_FULL
HOST_STAT_UNREACH = _lsf.HOST_STAT_UNREACH
HOST_STAT_UNAVAIL = _lsf.HOST_STAT_UNAVAIL
HOST_STAT_UNLICENSED = _lsf.HOST_STAT_UNLICENSED
HOST_STAT_NO_LIM = _lsf.HOST_STAT_NO_LIM
HOST_STAT_EXCLUSIVE = _lsf.HOST_STAT_EXCLUSIVE
HOST_STAT_LOCKED_MASTER = _lsf.HOST_STAT_LOCKED_MASTER
HOST_STAT_REMOTE_DISABLED = _lsf.HOST_STAT_REMOTE_DISABLED
HOST_STAT_LEASE_INACTIVE = _lsf.HOST_STAT_LEASE_INACTIVE
HOST_STAT_DISABLED_RES = _lsf.HOST_STAT_DISABLED_RES
HOST_STAT_DISABLED_RMS = _lsf.HOST_STAT_DISABLED_RMS
HOST_STAT_LOCKED_EGO = _lsf.HOST_STAT_LOCKED_EGO
HOST_CLOSED_BY_ADMIN = _lsf.HOST_CLOSED_BY_ADMIN
HOST_STAT_CU_EXCLUSIVE = _lsf.HOST_STAT_CU_EXCLUSIVE
HOST_STAT_EXPIRED = _lsf.HOST_STAT_EXPIRED
HOST_BUSY_NOT = _lsf.HOST_BUSY_NOT
HOST_BUSY_R15S = _lsf.HOST_BUSY_R15S
HOST_BUSY_R1M = _lsf.HOST_BUSY_R1M
HOST_BUSY_R15M = _lsf.HOST_BUSY_R15M
HOST_BUSY_UT = _lsf.HOST_BUSY_UT
HOST_BUSY_PG = _lsf.HOST_BUSY_PG
HOST_BUSY_IO = _lsf.HOST_BUSY_IO
HOST_BUSY_LS = _lsf.HOST_BUSY_LS
HOST_BUSY_IT = _lsf.HOST_BUSY_IT
HOST_BUSY_TMP = _lsf.HOST_BUSY_TMP
HOST_BUSY_SWP = _lsf.HOST_BUSY_SWP
HOST_BUSY_MEM = _lsf.HOST_BUSY_MEM
QUEUE_STAT_OPEN = _lsf.QUEUE_STAT_OPEN
QUEUE_STAT_ACTIVE = _lsf.QUEUE_STAT_ACTIVE
QUEUE_STAT_RUN = _lsf.QUEUE_STAT_RUN
QUEUE_STAT_NOPERM = _lsf.QUEUE_STAT_NOPERM
QUEUE_STAT_DISC = _lsf.QUEUE_STAT_DISC
QUEUE_STAT_RUNWIN_CLOSE = _lsf.QUEUE_STAT_RUNWIN_CLOSE
QUEUE_STAT_FAIRSHARE_DEFAULT = _lsf.QUEUE_STAT_FAIRSHARE_DEFAULT
Q_ATTRIB_EXCLUSIVE = _lsf.Q_ATTRIB_EXCLUSIVE
Q_ATTRIB_DEFAULT = _lsf.Q_ATTRIB_DEFAULT
Q_ATTRIB_FAIRSHARE = _lsf.Q_ATTRIB_FAIRSHARE
Q_ATTRIB_PREEMPTIVE = _lsf.Q_ATTRIB_PREEMPTIVE
Q_ATTRIB_NQS = _lsf.Q_ATTRIB_NQS
Q_ATTRIB_RECEIVE = _lsf.Q_ATTRIB_RECEIVE
Q_ATTRIB_PREEMPTABLE = _lsf.Q_ATTRIB_PREEMPTABLE
Q_ATTRIB_BACKFILL = _lsf.Q_ATTRIB_BACKFILL
Q_ATTRIB_HOST_PREFER = _lsf.Q_ATTRIB_HOST_PREFER
Q_ATTRIB_NONPREEMPTIVE = _lsf.Q_ATTRIB_NONPREEMPTIVE
Q_ATTRIB_NONPREEMPTABLE = _lsf.Q_ATTRIB_NONPREEMPTABLE
Q_ATTRIB_NO_INTERACTIVE = _lsf.Q_ATTRIB_NO_INTERACTIVE
Q_ATTRIB_ONLY_INTERACTIVE = _lsf.Q_ATTRIB_ONLY_INTERACTIVE
Q_ATTRIB_NO_HOST_TYPE = _lsf.Q_ATTRIB_NO_HOST_TYPE
Q_ATTRIB_IGNORE_DEADLINE = _lsf.Q_ATTRIB_IGNORE_DEADLINE
Q_ATTRIB_CHKPNT = _lsf.Q_ATTRIB_CHKPNT
Q_ATTRIB_RERUNNABLE = _lsf.Q_ATTRIB_RERUNNABLE
Q_ATTRIB_EXCL_RMTJOB = _lsf.Q_ATTRIB_EXCL_RMTJOB
Q_ATTRIB_MC_FAST_SCHEDULE = _lsf.Q_ATTRIB_MC_FAST_SCHEDULE
Q_ATTRIB_ENQUE_INTERACTIVE_AHEAD = _lsf.Q_ATTRIB_ENQUE_INTERACTIVE_AHEAD
Q_MC_FLAG = _lsf.Q_MC_FLAG
Q_ATTRIB_LEASE_LOCAL = _lsf.Q_ATTRIB_LEASE_LOCAL
Q_ATTRIB_LEASE_ONLY = _lsf.Q_ATTRIB_LEASE_ONLY
Q_ATTRIB_RMT_BATCH_LOCAL = _lsf.Q_ATTRIB_RMT_BATCH_LOCAL
Q_ATTRIB_RMT_BATCH_ONLY = _lsf.Q_ATTRIB_RMT_BATCH_ONLY
Q_ATTRIB_RESOURCE_RESERVE = _lsf.Q_ATTRIB_RESOURCE_RESERVE
Q_ATTRIB_FS_DISPATCH_ORDER_QUEUE = _lsf.Q_ATTRIB_FS_DISPATCH_ORDER_QUEUE
Q_ATTRIB_BATCH = _lsf.Q_ATTRIB_BATCH
Q_ATTRIB_ONLINE = _lsf.Q_ATTRIB_ONLINE
Q_ATTRIB_INTERRUPTIBLE_BACKFILL = _lsf.Q_ATTRIB_INTERRUPTIBLE_BACKFILL
Q_ATTRIB_APS = _lsf.Q_ATTRIB_APS
Q_ATTRIB_NO_HIGHER_RESERVE = _lsf.Q_ATTRIB_NO_HIGHER_RESERVE
Q_ATTRIB_NO_HOST_VALID = _lsf.Q_ATTRIB_NO_HOST_VALID
Q_ATTRIB2_IGN_GUAR = _lsf.Q_ATTRIB2_IGN_GUAR
MASTER_NULL = _lsf.MASTER_NULL
MASTER_RESIGN = _lsf.MASTER_RESIGN
MASTER_RECONFIG = _lsf.MASTER_RECONFIG
MASTER_FATAL = _lsf.MASTER_FATAL
MASTER_MEM = _lsf.MASTER_MEM
MASTER_CONF = _lsf.MASTER_CONF
MASTER_EVENT = _lsf.MASTER_EVENT
MASTER_DISABLE = _lsf.MASTER_DISABLE
MBD_USER_CMD = _lsf.MBD_USER_CMD
MBD_NON_USER_CMD = _lsf.MBD_NON_USER_CMD
JOB_STAT_NULL = _lsf.JOB_STAT_NULL
JOB_STAT_PEND = _lsf.JOB_STAT_PEND
JOB_STAT_PSUSP = _lsf.JOB_STAT_PSUSP
JOB_STAT_RUN = _lsf.JOB_STAT_RUN
JOB_STAT_SSUSP = _lsf.JOB_STAT_SSUSP
JOB_STAT_USUSP = _lsf.JOB_STAT_USUSP
JOB_STAT_EXIT = _lsf.JOB_STAT_EXIT
JOB_STAT_DONE = _lsf.JOB_STAT_DONE
JOB_STAT_PDONE = _lsf.JOB_STAT_PDONE
JOB_STAT_PERR = _lsf.JOB_STAT_PERR
JOB_STAT_WAIT = _lsf.JOB_STAT_WAIT
JOB_STAT_RUNKWN = _lsf.JOB_STAT_RUNKWN
JOB_STAT_UNKWN = _lsf.JOB_STAT_UNKWN
EVENT_JOB_NEW = _lsf.EVENT_JOB_NEW
EVENT_JOB_START = _lsf.EVENT_JOB_START
EVENT_JOB_STATUS = _lsf.EVENT_JOB_STATUS
EVENT_JOB_SWITCH = _lsf.EVENT_JOB_SWITCH
EVENT_JOB_MOVE = _lsf.EVENT_JOB_MOVE
EVENT_QUEUE_CTRL = _lsf.EVENT_QUEUE_CTRL
EVENT_HOST_CTRL = _lsf.EVENT_HOST_CTRL
EVENT_MBD_DIE = _lsf.EVENT_MBD_DIE
EVENT_MBD_UNFULFILL = _lsf.EVENT_MBD_UNFULFILL
EVENT_JOB_FINISH = _lsf.EVENT_JOB_FINISH
EVENT_LOAD_INDEX = _lsf.EVENT_LOAD_INDEX
EVENT_CHKPNT = _lsf.EVENT_CHKPNT
EVENT_MIG = _lsf.EVENT_MIG
EVENT_PRE_EXEC_START = _lsf.EVENT_PRE_EXEC_START
EVENT_MBD_START = _lsf.EVENT_MBD_START
EVENT_JOB_ROUTE = _lsf.EVENT_JOB_ROUTE
EVENT_JOB_MODIFY = _lsf.EVENT_JOB_MODIFY
EVENT_JOB_SIGNAL = _lsf.EVENT_JOB_SIGNAL
EVENT_CAL_NEW = _lsf.EVENT_CAL_NEW
EVENT_CAL_MODIFY = _lsf.EVENT_CAL_MODIFY
EVENT_CAL_DELETE = _lsf.EVENT_CAL_DELETE
EVENT_JOB_FORWARD = _lsf.EVENT_JOB_FORWARD
EVENT_JOB_ACCEPT = _lsf.EVENT_JOB_ACCEPT
EVENT_STATUS_ACK = _lsf.EVENT_STATUS_ACK
EVENT_JOB_EXECUTE = _lsf.EVENT_JOB_EXECUTE
EVENT_JOB_MSG = _lsf.EVENT_JOB_MSG
EVENT_JOB_MSG_ACK = _lsf.EVENT_JOB_MSG_ACK
EVENT_JOB_REQUEUE = _lsf.EVENT_JOB_REQUEUE
EVENT_JOB_OCCUPY_REQ = _lsf.EVENT_JOB_OCCUPY_REQ
EVENT_JOB_VACATED = _lsf.EVENT_JOB_VACATED
EVENT_JOB_SIGACT = _lsf.EVENT_JOB_SIGACT
EVENT_SBD_JOB_STATUS = _lsf.EVENT_SBD_JOB_STATUS
EVENT_JOB_START_ACCEPT = _lsf.EVENT_JOB_START_ACCEPT
EVENT_CAL_UNDELETE = _lsf.EVENT_CAL_UNDELETE
EVENT_JOB_CLEAN = _lsf.EVENT_JOB_CLEAN
EVENT_JOB_EXCEPTION = _lsf.EVENT_JOB_EXCEPTION
EVENT_JGRP_ADD = _lsf.EVENT_JGRP_ADD
EVENT_JGRP_MOD = _lsf.EVENT_JGRP_MOD
EVENT_JGRP_CTRL = _lsf.EVENT_JGRP_CTRL
EVENT_JOB_FORCE = _lsf.EVENT_JOB_FORCE
EVENT_LOG_SWITCH = _lsf.EVENT_LOG_SWITCH
EVENT_JOB_MODIFY2 = _lsf.EVENT_JOB_MODIFY2
EVENT_JGRP_STATUS = _lsf.EVENT_JGRP_STATUS
EVENT_JOB_ATTR_SET = _lsf.EVENT_JOB_ATTR_SET
EVENT_JOB_EXT_MSG = _lsf.EVENT_JOB_EXT_MSG
EVENT_JOB_ATTA_DATA = _lsf.EVENT_JOB_ATTA_DATA
EVENT_JOB_CHUNK = _lsf.EVENT_JOB_CHUNK
EVENT_SBD_UNREPORTED_STATUS = _lsf.EVENT_SBD_UNREPORTED_STATUS
EVENT_ADRSV_FINISH = _lsf.EVENT_ADRSV_FINISH
EVENT_HGHOST_CTRL = _lsf.EVENT_HGHOST_CTRL
EVENT_CPUPROFILE_STATUS = _lsf.EVENT_CPUPROFILE_STATUS
EVENT_DATA_LOGGING = _lsf.EVENT_DATA_LOGGING
EVENT_JOB_RUN_RUSAGE = _lsf.EVENT_JOB_RUN_RUSAGE
EVENT_END_OF_STREAM = _lsf.EVENT_END_OF_STREAM
EVENT_SLA_RECOMPUTE = _lsf.EVENT_SLA_RECOMPUTE
EVENT_METRIC_LOG = _lsf.EVENT_METRIC_LOG
EVENT_TASK_FINISH = _lsf.EVENT_TASK_FINISH
EVENT_JOB_RESIZE_NOTIFY_START = _lsf.EVENT_JOB_RESIZE_NOTIFY_START
EVENT_JOB_RESIZE_NOTIFY_ACCEPT = _lsf.EVENT_JOB_RESIZE_NOTIFY_ACCEPT
EVENT_JOB_RESIZE_NOTIFY_DONE = _lsf.EVENT_JOB_RESIZE_NOTIFY_DONE
EVENT_JOB_RESIZE_RELEASE = _lsf.EVENT_JOB_RESIZE_RELEASE
EVENT_JOB_RESIZE_CANCEL = _lsf.EVENT_JOB_RESIZE_CANCEL
EVENT_JOB_RESIZE = _lsf.EVENT_JOB_RESIZE
EVENT_JOB_ARRAY_ELEMENT = _lsf.EVENT_JOB_ARRAY_ELEMENT
EVENT_MBD_SIM_STATUS = _lsf.EVENT_MBD_SIM_STATUS
EVENT_JOB_FINISH2 = _lsf.EVENT_JOB_FINISH2
EVENT_JOB_STARTLIMIT = _lsf.EVENT_JOB_STARTLIMIT
EVENT_JOB_STATUS2 = _lsf.EVENT_JOB_STATUS2
EVENT_JOB_PENDING_REASONS = _lsf.EVENT_JOB_PENDING_REASONS
NUM_EVENT_TYPES = _lsf.NUM_EVENT_TYPES
EVENT_JOB_RELATED = _lsf.EVENT_JOB_RELATED
EVENT_NON_JOB_RELATED = _lsf.EVENT_NON_JOB_RELATED
PEND_JOB_REASON = _lsf.PEND_JOB_REASON
PEND_JOB_NEW = _lsf.PEND_JOB_NEW
PEND_JOB_START_TIME = _lsf.PEND_JOB_START_TIME
PEND_JOB_DEPEND = _lsf.PEND_JOB_DEPEND
PEND_JOB_DEP_INVALID = _lsf.PEND_JOB_DEP_INVALID
PEND_JOB_MIG = _lsf.PEND_JOB_MIG
PEND_JOB_PRE_EXEC = _lsf.PEND_JOB_PRE_EXEC
PEND_JOB_NO_FILE = _lsf.PEND_JOB_NO_FILE
PEND_JOB_ENV = _lsf.PEND_JOB_ENV
PEND_JOB_PATHS = _lsf.PEND_JOB_PATHS
PEND_JOB_OPEN_FILES = _lsf.PEND_JOB_OPEN_FILES
PEND_JOB_EXEC_INIT = _lsf.PEND_JOB_EXEC_INIT
PEND_JOB_RESTART_FILE = _lsf.PEND_JOB_RESTART_FILE
PEND_JOB_DELAY_SCHED = _lsf.PEND_JOB_DELAY_SCHED
PEND_JOB_SWITCH = _lsf.PEND_JOB_SWITCH
PEND_JOB_DEP_REJECT = _lsf.PEND_JOB_DEP_REJECT
PEND_JOB_JS_DISABLED = _lsf.PEND_JOB_JS_DISABLED
PEND_JOB_NO_PASSWD = _lsf.PEND_JOB_NO_PASSWD
PEND_JOB_LOGON_FAIL = _lsf.PEND_JOB_LOGON_FAIL
PEND_JOB_MODIFY = _lsf.PEND_JOB_MODIFY
PEND_JOB_TIME_INVALID = _lsf.PEND_JOB_TIME_INVALID
PEND_TIME_EXPIRED = _lsf.PEND_TIME_EXPIRED
PEND_JOB_REQUEUED = _lsf.PEND_JOB_REQUEUED
PEND_WAIT_NEXT = _lsf.PEND_WAIT_NEXT
PEND_JGRP_HOLD = _lsf.PEND_JGRP_HOLD
PEND_JGRP_INACT = _lsf.PEND_JGRP_INACT
PEND_JGRP_WAIT = _lsf.PEND_JGRP_WAIT
PEND_JOB_RCLUS_UNREACH = _lsf.PEND_JOB_RCLUS_UNREACH
PEND_JOB_QUE_REJECT = _lsf.PEND_JOB_QUE_REJECT
PEND_JOB_RSCHED_START = _lsf.PEND_JOB_RSCHED_START
PEND_JOB_RSCHED_ALLOC = _lsf.PEND_JOB_RSCHED_ALLOC
PEND_JOB_FORWARDED = _lsf.PEND_JOB_FORWARDED
PEND_JOB_RMT_ZOMBIE = _lsf.PEND_JOB_RMT_ZOMBIE
PEND_JOB_ENFUGRP = _lsf.PEND_JOB_ENFUGRP
PEND_SYS_UNABLE = _lsf.PEND_SYS_UNABLE
PEND_JGRP_RELEASE = _lsf.PEND_JGRP_RELEASE
PEND_HAS_RUN = _lsf.PEND_HAS_RUN
PEND_JOB_ARRAY_JLIMIT = _lsf.PEND_JOB_ARRAY_JLIMIT
PEND_CHKPNT_DIR = _lsf.PEND_CHKPNT_DIR
PEND_CHUNK_FAIL = _lsf.PEND_CHUNK_FAIL
PEND_JOB_SLA_MET = _lsf.PEND_JOB_SLA_MET
PEND_JOB_APP_NOEXIST = _lsf.PEND_JOB_APP_NOEXIST
PEND_APP_PROCLIMIT = _lsf.PEND_APP_PROCLIMIT
PEND_EGO_NO_HOSTS = _lsf.PEND_EGO_NO_HOSTS
PEND_JGRP_JLIMIT = _lsf.PEND_JGRP_JLIMIT
PEND_PREEXEC_LIMIT = _lsf.PEND_PREEXEC_LIMIT
PEND_REQUEUE_LIMIT = _lsf.PEND_REQUEUE_LIMIT
PEND_BAD_RESREQ = _lsf.PEND_BAD_RESREQ
PEND_RSV_INACTIVE = _lsf.PEND_RSV_INACTIVE
PEND_WAITING_RESUME = _lsf.PEND_WAITING_RESUME
PEND_SLOT_COMPOUND = _lsf.PEND_SLOT_COMPOUND
PEND_QUE_INACT = _lsf.PEND_QUE_INACT
PEND_QUE_WINDOW = _lsf.PEND_QUE_WINDOW
PEND_QUE_JOB_LIMIT = _lsf.PEND_QUE_JOB_LIMIT
PEND_QUE_USR_JLIMIT = _lsf.PEND_QUE_USR_JLIMIT
PEND_QUE_USR_PJLIMIT = _lsf.PEND_QUE_USR_PJLIMIT
PEND_QUE_PRE_FAIL = _lsf.PEND_QUE_PRE_FAIL
PEND_NQS_RETRY = _lsf.PEND_NQS_RETRY
PEND_NQS_REASONS = _lsf.PEND_NQS_REASONS
PEND_NQS_FUN_OFF = _lsf.PEND_NQS_FUN_OFF
PEND_SYS_NOT_READY = _lsf.PEND_SYS_NOT_READY
PEND_SBD_JOB_REQUEUE = _lsf.PEND_SBD_JOB_REQUEUE
PEND_JOB_SPREAD_TASK = _lsf.PEND_JOB_SPREAD_TASK
PEND_QUE_SPREAD_TASK = _lsf.PEND_QUE_SPREAD_TASK
PEND_QUE_PJOB_LIMIT = _lsf.PEND_QUE_PJOB_LIMIT
PEND_QUE_WINDOW_WILL_CLOSE = _lsf.PEND_QUE_WINDOW_WILL_CLOSE
PEND_QUE_PROCLIMIT = _lsf.PEND_QUE_PROCLIMIT
PEND_SBD_PLUGIN = _lsf.PEND_SBD_PLUGIN
PEND_WAIT_SIGN_LEASE = _lsf.PEND_WAIT_SIGN_LEASE
PEND_WAIT_SLOT_SHARE = _lsf.PEND_WAIT_SLOT_SHARE
PEND_USER_JOB_LIMIT = _lsf.PEND_USER_JOB_LIMIT
PEND_UGRP_JOB_LIMIT = _lsf.PEND_UGRP_JOB_LIMIT
PEND_USER_PJOB_LIMIT = _lsf.PEND_USER_PJOB_LIMIT
PEND_UGRP_PJOB_LIMIT = _lsf.PEND_UGRP_PJOB_LIMIT
PEND_USER_RESUME = _lsf.PEND_USER_RESUME
PEND_USER_STOP = _lsf.PEND_USER_STOP
PEND_NO_MAPPING = _lsf.PEND_NO_MAPPING
PEND_RMT_PERMISSION = _lsf.PEND_RMT_PERMISSION
PEND_ADMIN_STOP = _lsf.PEND_ADMIN_STOP
PEND_MLS_INVALID = _lsf.PEND_MLS_INVALID
PEND_MLS_CLEARANCE = _lsf.PEND_MLS_CLEARANCE
PEND_MLS_RHOST = _lsf.PEND_MLS_RHOST
PEND_MLS_DOMINATE = _lsf.PEND_MLS_DOMINATE
PEND_MLS_FATAL = _lsf.PEND_MLS_FATAL
PEND_INTERNAL_STOP = _lsf.PEND_INTERNAL_STOP
PEND_HOST_RES_REQ = _lsf.PEND_HOST_RES_REQ
PEND_HOST_NONEXCLUSIVE = _lsf.PEND_HOST_NONEXCLUSIVE
PEND_HOST_JOB_SSUSP = _lsf.PEND_HOST_JOB_SSUSP
PEND_HOST_PART_PRIO = _lsf.PEND_HOST_PART_PRIO
PEND_SBD_GETPID = _lsf.PEND_SBD_GETPID
PEND_SBD_LOCK = _lsf.PEND_SBD_LOCK
PEND_SBD_ZOMBIE = _lsf.PEND_SBD_ZOMBIE
PEND_SBD_ROOT = _lsf.PEND_SBD_ROOT
PEND_HOST_WIN_WILL_CLOSE = _lsf.PEND_HOST_WIN_WILL_CLOSE
PEND_HOST_MISS_DEADLINE = _lsf.PEND_HOST_MISS_DEADLINE
PEND_FIRST_HOST_INELIGIBLE = _lsf.PEND_FIRST_HOST_INELIGIBLE
PEND_HOST_EXCLUSIVE_RESERVE = _lsf.PEND_HOST_EXCLUSIVE_RESERVE
PEND_FIRST_HOST_REUSE = _lsf.PEND_FIRST_HOST_REUSE
PEND_HOST_DISABLED = _lsf.PEND_HOST_DISABLED
PEND_HOST_LOCKED = _lsf.PEND_HOST_LOCKED
PEND_HOST_LESS_SLOTS = _lsf.PEND_HOST_LESS_SLOTS
PEND_HOST_WINDOW = _lsf.PEND_HOST_WINDOW
PEND_HOST_JOB_LIMIT = _lsf.PEND_HOST_JOB_LIMIT
PEND_QUE_PROC_JLIMIT = _lsf.PEND_QUE_PROC_JLIMIT
PEND_QUE_HOST_JLIMIT = _lsf.PEND_QUE_HOST_JLIMIT
PEND_USER_PROC_JLIMIT = _lsf.PEND_USER_PROC_JLIMIT
PEND_HOST_USR_JLIMIT = _lsf.PEND_HOST_USR_JLIMIT
PEND_HOST_QUE_MEMB = _lsf.PEND_HOST_QUE_MEMB
PEND_HOST_USR_SPEC = _lsf.PEND_HOST_USR_SPEC
PEND_HOST_PART_USER = _lsf.PEND_HOST_PART_USER
PEND_HOST_NO_USER = _lsf.PEND_HOST_NO_USER
PEND_HOST_ACCPT_ONE = _lsf.PEND_HOST_ACCPT_ONE
PEND_LOAD_UNAVAIL = _lsf.PEND_LOAD_UNAVAIL
PEND_HOST_NO_LIM = _lsf.PEND_HOST_NO_LIM
PEND_HOST_UNLICENSED = _lsf.PEND_HOST_UNLICENSED
PEND_HOST_QUE_RESREQ = _lsf.PEND_HOST_QUE_RESREQ
PEND_HOST_SCHED_TYPE = _lsf.PEND_HOST_SCHED_TYPE
PEND_JOB_NO_SPAN = _lsf.PEND_JOB_NO_SPAN
PEND_QUE_NO_SPAN = _lsf.PEND_QUE_NO_SPAN
PEND_HOST_EXCLUSIVE = _lsf.PEND_HOST_EXCLUSIVE
PEND_HOST_JS_DISABLED = _lsf.PEND_HOST_JS_DISABLED
PEND_UGRP_PROC_JLIMIT = _lsf.PEND_UGRP_PROC_JLIMIT
PEND_BAD_HOST = _lsf.PEND_BAD_HOST
PEND_QUEUE_HOST = _lsf.PEND_QUEUE_HOST
PEND_HOST_LOCKED_MASTER = _lsf.PEND_HOST_LOCKED_MASTER
PEND_HOST_LESS_RSVSLOTS = _lsf.PEND_HOST_LESS_RSVSLOTS
PEND_HOST_LESS_DURATION = _lsf.PEND_HOST_LESS_DURATION
PEND_HOST_NO_RSVID = _lsf.PEND_HOST_NO_RSVID
PEND_HOST_LEASE_INACTIVE = _lsf.PEND_HOST_LEASE_INACTIVE
PEND_HOST_ADRSV_ACTIVE = _lsf.PEND_HOST_ADRSV_ACTIVE
PEND_QUE_RSVID_NOMATCH = _lsf.PEND_QUE_RSVID_NOMATCH
PEND_HOST_GENERAL = _lsf.PEND_HOST_GENERAL
PEND_HOST_RSV = _lsf.PEND_HOST_RSV
PEND_HOST_NOT_CU = _lsf.PEND_HOST_NOT_CU
PEND_HOST_CU_EXCL = _lsf.PEND_HOST_CU_EXCL
PEND_HOST_CU_OCCUPIED = _lsf.PEND_HOST_CU_OCCUPIED
PEND_HOST_USABLE_CU = _lsf.PEND_HOST_USABLE_CU
PEND_JOB_FIRST_CU = _lsf.PEND_JOB_FIRST_CU
PEND_HOST_CU_EXCL_RSV = _lsf.PEND_HOST_CU_EXCL_RSV
PEND_JOB_CU_MAXCUS = _lsf.PEND_JOB_CU_MAXCUS
PEND_JOB_CU_BALANCE = _lsf.PEND_JOB_CU_BALANCE
PEND_CU_TOPLIB_HOST = _lsf.PEND_CU_TOPLIB_HOST
PEND_HOST_PREEXEC_FAIL = _lsf.PEND_HOST_PREEXEC_FAIL
PEND_SBD_UNREACH = _lsf.PEND_SBD_UNREACH
PEND_SBD_JOB_QUOTA = _lsf.PEND_SBD_JOB_QUOTA
PEND_JOB_START_FAIL = _lsf.PEND_JOB_START_FAIL
PEND_JOB_START_UNKNWN = _lsf.PEND_JOB_START_UNKNWN
PEND_SBD_NO_MEM = _lsf.PEND_SBD_NO_MEM
PEND_SBD_NO_PROCESS = _lsf.PEND_SBD_NO_PROCESS
PEND_SBD_SOCKETPAIR = _lsf.PEND_SBD_SOCKETPAIR
PEND_SBD_JOB_ACCEPT = _lsf.PEND_SBD_JOB_ACCEPT
PEND_LEASE_JOB_REMOTE_DISPATCH = _lsf.PEND_LEASE_JOB_REMOTE_DISPATCH
PEND_JOB_RESTART_FAIL = _lsf.PEND_JOB_RESTART_FAIL
PEND_HOST_LOAD = _lsf.PEND_HOST_LOAD
PEND_HOST_QUE_RUSAGE = _lsf.PEND_HOST_QUE_RUSAGE
PEND_HOST_JOB_RUSAGE = _lsf.PEND_HOST_JOB_RUSAGE
PEND_RMT_JOB_FORGOTTEN = _lsf.PEND_RMT_JOB_FORGOTTEN
PEND_RMT_IMPT_JOBBKLG = _lsf.PEND_RMT_IMPT_JOBBKLG
PEND_RMT_MAX_RSCHED_TIME = _lsf.PEND_RMT_MAX_RSCHED_TIME
PEND_RMT_MAX_PREEXEC_RETRY = _lsf.PEND_RMT_MAX_PREEXEC_RETRY
PEND_RMT_QUEUE_CLOSED = _lsf.PEND_RMT_QUEUE_CLOSED
PEND_RMT_QUEUE_INACTIVE = _lsf.PEND_RMT_QUEUE_INACTIVE
PEND_RMT_QUEUE_CONGESTED = _lsf.PEND_RMT_QUEUE_CONGESTED
PEND_RMT_QUEUE_DISCONNECT = _lsf.PEND_RMT_QUEUE_DISCONNECT
PEND_RMT_QUEUE_NOPERMISSION = _lsf.PEND_RMT_QUEUE_NOPERMISSION
PEND_RMT_BAD_TIME = _lsf.PEND_RMT_BAD_TIME
PEND_RMT_PERMISSIONS = _lsf.PEND_RMT_PERMISSIONS
PEND_RMT_PROC_NUM = _lsf.PEND_RMT_PROC_NUM
PEND_RMT_QUEUE_USE = _lsf.PEND_RMT_QUEUE_USE
PEND_RMT_NO_INTERACTIVE = _lsf.PEND_RMT_NO_INTERACTIVE
PEND_RMT_ONLY_INTERACTIVE = _lsf.PEND_RMT_ONLY_INTERACTIVE
PEND_RMT_PROC_LESS = _lsf.PEND_RMT_PROC_LESS
PEND_RMT_OVER_LIMIT = _lsf.PEND_RMT_OVER_LIMIT
PEND_RMT_BAD_RESREQ = _lsf.PEND_RMT_BAD_RESREQ
PEND_RMT_CREATE_JOB = _lsf.PEND_RMT_CREATE_JOB
PEND_RMT_RERUN = _lsf.PEND_RMT_RERUN
PEND_RMT_EXIT_REQUEUE = _lsf.PEND_RMT_EXIT_REQUEUE
PEND_RMT_REQUEUE = _lsf.PEND_RMT_REQUEUE
PEND_RMT_JOB_FORWARDING = _lsf.PEND_RMT_JOB_FORWARDING
PEND_RMT_QUEUE_INVALID = _lsf.PEND_RMT_QUEUE_INVALID
PEND_RMT_QUEUE_NO_EXCLUSIVE = _lsf.PEND_RMT_QUEUE_NO_EXCLUSIVE
PEND_RMT_UGROUP_MEMBER = _lsf.PEND_RMT_UGROUP_MEMBER
PEND_RMT_INTERACTIVE_RERUN = _lsf.PEND_RMT_INTERACTIVE_RERUN
PEND_RMT_JOB_START_FAIL = _lsf.PEND_RMT_JOB_START_FAIL
PEND_RMT_FORWARD_FAIL_UGROUP_MEMBER = _lsf.PEND_RMT_FORWARD_FAIL_UGROUP_MEMBER
PEND_RMT_HOST_NO_RSVID = _lsf.PEND_RMT_HOST_NO_RSVID
PEND_RMT_APP_NULL = _lsf.PEND_RMT_APP_NULL
PEND_RMT_BAD_RUNLIMIT = _lsf.PEND_RMT_BAD_RUNLIMIT
PEND_RMT_OVER_QUEUE_LIMIT = _lsf.PEND_RMT_OVER_QUEUE_LIMIT
PEND_RMT_WHEN_NO_SLOTS = _lsf.PEND_RMT_WHEN_NO_SLOTS
PEND_GENERAL_LIMIT_USER = _lsf.PEND_GENERAL_LIMIT_USER
PEND_GENERAL_LIMIT_QUEUE = _lsf.PEND_GENERAL_LIMIT_QUEUE
PEND_GENERAL_LIMIT_PROJECT = _lsf.PEND_GENERAL_LIMIT_PROJECT
PEND_GENERAL_LIMIT_CLUSTER = _lsf.PEND_GENERAL_LIMIT_CLUSTER
PEND_GENERAL_LIMIT_HOST = _lsf.PEND_GENERAL_LIMIT_HOST
PEND_GENERAL_LIMIT_JOBS_USER = _lsf.PEND_GENERAL_LIMIT_JOBS_USER
PEND_GENERAL_LIMIT_JOBS_QUEUE = _lsf.PEND_GENERAL_LIMIT_JOBS_QUEUE
PEND_GENERAL_LIMIT_JOBS_PROJECT = _lsf.PEND_GENERAL_LIMIT_JOBS_PROJECT
PEND_GENERAL_LIMIT_JOBS_CLUSTER = _lsf.PEND_GENERAL_LIMIT_JOBS_CLUSTER
PEND_GENERAL_LIMIT_JOBS_HOST = _lsf.PEND_GENERAL_LIMIT_JOBS_HOST
PEND_GENERAL_LIMIT_JOBS_LIC_PROJECT = _lsf.PEND_GENERAL_LIMIT_JOBS_LIC_PROJECT
PEND_RMS_PLUGIN_INTERNAL = _lsf.PEND_RMS_PLUGIN_INTERNAL
PEND_RMS_PLUGIN_RLA_COMM = _lsf.PEND_RMS_PLUGIN_RLA_COMM
PEND_RMS_NOT_AVAILABLE = _lsf.PEND_RMS_NOT_AVAILABLE
PEND_RMS_FAIL_TOPOLOGY = _lsf.PEND_RMS_FAIL_TOPOLOGY
PEND_RMS_FAIL_ALLOC = _lsf.PEND_RMS_FAIL_ALLOC
PEND_RMS_SPECIAL_NO_PREEMPT_BACKFILL = _lsf.PEND_RMS_SPECIAL_NO_PREEMPT_BACKFILL
PEND_RMS_SPECIAL_NO_RESERVE = _lsf.PEND_RMS_SPECIAL_NO_RESERVE
PEND_RMS_RLA_INTERNAL = _lsf.PEND_RMS_RLA_INTERNAL
PEND_RMS_NO_SLOTS_SPECIAL = _lsf.PEND_RMS_NO_SLOTS_SPECIAL
PEND_RMS_RLA_NO_SUCH_USER = _lsf.PEND_RMS_RLA_NO_SUCH_USER
PEND_RMS_RLA_NO_SUCH_HOST = _lsf.PEND_RMS_RLA_NO_SUCH_HOST
PEND_RMS_CHUNKJOB = _lsf.PEND_RMS_CHUNKJOB
PEND_RLA_PROTOMISMATCH = _lsf.PEND_RLA_PROTOMISMATCH
PEND_RMS_BAD_TOPOLOGY = _lsf.PEND_RMS_BAD_TOPOLOGY
PEND_RMS_RESREQ_MCONT = _lsf.PEND_RMS_RESREQ_MCONT
PEND_RMS_RESREQ_PTILE = _lsf.PEND_RMS_RESREQ_PTILE
PEND_RMS_RESREQ_NODES = _lsf.PEND_RMS_RESREQ_NODES
PEND_RMS_RESREQ_BASE = _lsf.PEND_RMS_RESREQ_BASE
PEND_RMS_RESREQ_RAILS = _lsf.PEND_RMS_RESREQ_RAILS
PEND_RMS_RESREQ_RAILMASK = _lsf.PEND_RMS_RESREQ_RAILMASK
PEND_MAUI_UNREACH = _lsf.PEND_MAUI_UNREACH
PEND_MAUI_FORWARD = _lsf.PEND_MAUI_FORWARD
PEND_MAUI_REASON = _lsf.PEND_MAUI_REASON
PEND_CPUSET_ATTACH = _lsf.PEND_CPUSET_ATTACH
PEND_CPUSET_NOT_CPUSETHOST = _lsf.PEND_CPUSET_NOT_CPUSETHOST
PEND_CPUSET_TOPD_INIT = _lsf.PEND_CPUSET_TOPD_INIT
PEND_CPUSET_TOPD_TIME_OUT = _lsf.PEND_CPUSET_TOPD_TIME_OUT
PEND_CPUSET_TOPD_FAIL_ALLOC = _lsf.PEND_CPUSET_TOPD_FAIL_ALLOC
PEND_CPUSET_TOPD_BAD_REQUEST = _lsf.PEND_CPUSET_TOPD_BAD_REQUEST
PEND_CPUSET_TOPD_INTERNAL = _lsf.PEND_CPUSET_TOPD_INTERNAL
PEND_CPUSET_TOPD_SYSAPI_ERR = _lsf.PEND_CPUSET_TOPD_SYSAPI_ERR
PEND_CPUSET_TOPD_NOSUCH_NAME = _lsf.PEND_CPUSET_TOPD_NOSUCH_NAME
PEND_CPUSET_TOPD_JOB_EXIST = _lsf.PEND_CPUSET_TOPD_JOB_EXIST
PEND_CPUSET_TOPD_NO_MEMORY = _lsf.PEND_CPUSET_TOPD_NO_MEMORY
PEND_CPUSET_TOPD_INVALID_USER = _lsf.PEND_CPUSET_TOPD_INVALID_USER
PEND_CPUSET_TOPD_PERM_DENY = _lsf.PEND_CPUSET_TOPD_PERM_DENY
PEND_CPUSET_TOPD_UNREACH = _lsf.PEND_CPUSET_TOPD_UNREACH
PEND_CPUSET_TOPD_COMM_ERR = _lsf.PEND_CPUSET_TOPD_COMM_ERR
PEND_CPUSET_PLUGIN_INTERNAL = _lsf.PEND_CPUSET_PLUGIN_INTERNAL
PEND_CPUSET_CHUNKJOB = _lsf.PEND_CPUSET_CHUNKJOB
PEND_CPUSET_CPULIST = _lsf.PEND_CPUSET_CPULIST
PEND_CPUSET_MAXRADIUS = _lsf.PEND_CPUSET_MAXRADIUS
PEND_NODE_ALLOC_FAIL = _lsf.PEND_NODE_ALLOC_FAIL
PEND_RMSRID_UNAVAIL = _lsf.PEND_RMSRID_UNAVAIL
PEND_NO_FREE_CPUS = _lsf.PEND_NO_FREE_CPUS
PEND_TOPOLOGY_UNKNOWN = _lsf.PEND_TOPOLOGY_UNKNOWN
PEND_BAD_TOPOLOGY = _lsf.PEND_BAD_TOPOLOGY
PEND_RLA_COMM = _lsf.PEND_RLA_COMM
PEND_RLA_NO_SUCH_USER = _lsf.PEND_RLA_NO_SUCH_USER
PEND_RLA_INTERNAL = _lsf.PEND_RLA_INTERNAL
PEND_RLA_NO_SUCH_HOST = _lsf.PEND_RLA_NO_SUCH_HOST
PEND_RESREQ_TOOFEWSLOTS = _lsf.PEND_RESREQ_TOOFEWSLOTS
PEND_PSET_PLUGIN_INTERNAL = _lsf.PEND_PSET_PLUGIN_INTERNAL
PEND_PSET_RESREQ_PTILE = _lsf.PEND_PSET_RESREQ_PTILE
PEND_PSET_RESREQ_CELLS = _lsf.PEND_PSET_RESREQ_CELLS
PEND_PSET_CHUNKJOB = _lsf.PEND_PSET_CHUNKJOB
PEND_PSET_NOTSUPPORT = _lsf.PEND_PSET_NOTSUPPORT
PEND_PSET_BIND_FAIL = _lsf.PEND_PSET_BIND_FAIL
PEND_PSET_RESREQ_CELLLIST = _lsf.PEND_PSET_RESREQ_CELLLIST
PEND_SLURM_PLUGIN_INTERNAL = _lsf.PEND_SLURM_PLUGIN_INTERNAL
PEND_SLURM_RESREQ_NODES = _lsf.PEND_SLURM_RESREQ_NODES
PEND_SLURM_RESREQ_NODE_ATTR = _lsf.PEND_SLURM_RESREQ_NODE_ATTR
PEND_SLURM_RESREQ_EXCLUDE = _lsf.PEND_SLURM_RESREQ_EXCLUDE
PEND_SLURM_RESREQ_NODELIST = _lsf.PEND_SLURM_RESREQ_NODELIST
PEND_SLURM_RESREQ_CONTIGUOUS = _lsf.PEND_SLURM_RESREQ_CONTIGUOUS
PEND_SLURM_ALLOC_UNAVAIL = _lsf.PEND_SLURM_ALLOC_UNAVAIL
PEND_SLURM_RESREQ_BAD_CONSTRAINT = _lsf.PEND_SLURM_RESREQ_BAD_CONSTRAINT
PEND_CRAYX1_SSP = _lsf.PEND_CRAYX1_SSP
PEND_CRAYX1_MSP = _lsf.PEND_CRAYX1_MSP
PEND_CRAYX1_PASS_LIMIT = _lsf.PEND_CRAYX1_PASS_LIMIT
PEND_CRAYXT3_ASSIGN_FAIL = _lsf.PEND_CRAYXT3_ASSIGN_FAIL
PEND_BLUEGENE_PLUGIN_INTERNAL = _lsf.PEND_BLUEGENE_PLUGIN_INTERNAL
PEND_BLUEGENE_ALLOC_UNAVAIL = _lsf.PEND_BLUEGENE_ALLOC_UNAVAIL
PEND_BLUEGENE_NOFREEMIDPLANES = _lsf.PEND_BLUEGENE_NOFREEMIDPLANES
PEND_BLUEGENE_NOFREEQUARTERS = _lsf.PEND_BLUEGENE_NOFREEQUARTERS
PEND_BLUEGENE_NOFREENODECARDS = _lsf.PEND_BLUEGENE_NOFREENODECARDS
PEND_RESIZE_FIRSTHOSTUNAVAIL = _lsf.PEND_RESIZE_FIRSTHOSTUNAVAIL
PEND_RESIZE_MASTERSUSP = _lsf.PEND_RESIZE_MASTERSUSP
PEND_RESIZE_MASTER_SAME = _lsf.PEND_RESIZE_MASTER_SAME
PEND_RESIZE_SPAN_PTILE = _lsf.PEND_RESIZE_SPAN_PTILE
PEND_RESIZE_SPAN_HOSTS = _lsf.PEND_RESIZE_SPAN_HOSTS
PEND_RESIZE_LEASE_HOST = _lsf.PEND_RESIZE_LEASE_HOST
PEND_PS_PLUGIN_INTERNAL = _lsf.PEND_PS_PLUGIN_INTERNAL
PEND_PS_MBD_SYNC = _lsf.PEND_PS_MBD_SYNC
PEND_COMPOUND_RESREQ_OLD_LEASE_HOST = _lsf.PEND_COMPOUND_RESREQ_OLD_LEASE_HOST
PEND_COMPOUND_RESREQ_TOPLIB_HOST = _lsf.PEND_COMPOUND_RESREQ_TOPLIB_HOST
PEND_MULTIPHASE_RESREQ_OLD_LEASE_HOST = _lsf.PEND_MULTIPHASE_RESREQ_OLD_LEASE_HOST
PEND_QUEUE_SLOT_POOL_LIMIT = _lsf.PEND_QUEUE_SLOT_POOL_LIMIT
PEND_GUARANTEE_RSRC = _lsf.PEND_GUARANTEE_RSRC
PEND_GUARANTEE_SLOTS = _lsf.PEND_GUARANTEE_SLOTS
PEND_GUARANTEE_HOSTS = _lsf.PEND_GUARANTEE_HOSTS
PEND_GUARANTEE_SLOTS_PER_HOST = _lsf.PEND_GUARANTEE_SLOTS_PER_HOST
PEND_GUARANTEE_NONSLA = _lsf.PEND_GUARANTEE_NONSLA
PEND_GUARANTEE_SLOTS_LIMIT = _lsf.PEND_GUARANTEE_SLOTS_LIMIT
PEND_GENERAL_LIMIT_LIC_PROJECT = _lsf.PEND_GENERAL_LIMIT_LIC_PROJECT
PEND_GENERAL_LIMIT_LIC_PROJECT_END = _lsf.PEND_GENERAL_LIMIT_LIC_PROJECT_END
PEND_PREEMPT_DELAY = _lsf.PEND_PREEMPT_DELAY
PEND_GLB_MIXED_MODE = _lsf.PEND_GLB_MIXED_MODE
PEND_EXTSCHED_REASON = _lsf.PEND_EXTSCHED_REASON
PEND_RES_DEFAULT_SIZE = _lsf.PEND_RES_DEFAULT_SIZE
PEND_RES_EXTEND_SIZE = _lsf.PEND_RES_EXTEND_SIZE
PEND_RESERVED_REASON_END = _lsf.PEND_RESERVED_REASON_END
PEND_CUSTOMER_MIN = _lsf.PEND_CUSTOMER_MIN
PEND_CUSTOMER_MAX = _lsf.PEND_CUSTOMER_MAX
PEND_MAX_REASONS = _lsf.PEND_MAX_REASONS
SUSP_USER_REASON = _lsf.SUSP_USER_REASON
SUSP_USER_RESUME = _lsf.SUSP_USER_RESUME
SUSP_USER_STOP = _lsf.SUSP_USER_STOP
SUSP_QUEUE_REASON = _lsf.SUSP_QUEUE_REASON
SUSP_QUEUE_WINDOW = _lsf.SUSP_QUEUE_WINDOW
SUSP_RESCHED_PREEMPT = _lsf.SUSP_RESCHED_PREEMPT
SUSP_HOST_LOCK = _lsf.SUSP_HOST_LOCK
SUSP_LOAD_REASON = _lsf.SUSP_LOAD_REASON
SUSP_MBD_PREEMPT = _lsf.SUSP_MBD_PREEMPT
SUSP_SBD_PREEMPT = _lsf.SUSP_SBD_PREEMPT
SUSP_QUE_STOP_COND = _lsf.SUSP_QUE_STOP_COND
SUSP_QUE_RESUME_COND = _lsf.SUSP_QUE_RESUME_COND
SUSP_PG_IT = _lsf.SUSP_PG_IT
SUSP_REASON_RESET = _lsf.SUSP_REASON_RESET
SUSP_LOAD_UNAVAIL = _lsf.SUSP_LOAD_UNAVAIL
SUSP_ADMIN_STOP = _lsf.SUSP_ADMIN_STOP
SUSP_RES_RESERVE = _lsf.SUSP_RES_RESERVE
SUSP_MBD_LOCK = _lsf.SUSP_MBD_LOCK
SUSP_RES_LIMIT = _lsf.SUSP_RES_LIMIT
SUSP_SBD_STARTUP = _lsf.SUSP_SBD_STARTUP
SUSP_HOST_LOCK_MASTER = _lsf.SUSP_HOST_LOCK_MASTER
SUSP_HOST_RSVACTIVE = _lsf.SUSP_HOST_RSVACTIVE
SUSP_DETAILED_SUBREASON = _lsf.SUSP_DETAILED_SUBREASON
SUSP_GLB_LICENSE_PREEMPT = _lsf.SUSP_GLB_LICENSE_PREEMPT
SUSP_CRAYX1_POSTED = _lsf.SUSP_CRAYX1_POSTED
SUSP_ADVRSV_EXPIRED = _lsf.SUSP_ADVRSV_EXPIRED
SUSP_STOP_RELEASE_JOB_SLOT = _lsf.SUSP_STOP_RELEASE_JOB_SLOT
RELEASING_SLOT = _lsf.RELEASING_SLOT
RELEASED_SLOT = _lsf.RELEASED_SLOT
SUB_REASON_RUNLIMIT = _lsf.SUB_REASON_RUNLIMIT
SUB_REASON_DEADLINE = _lsf.SUB_REASON_DEADLINE
SUB_REASON_PROCESSLIMIT = _lsf.SUB_REASON_PROCESSLIMIT
SUB_REASON_CPULIMIT = _lsf.SUB_REASON_CPULIMIT
SUB_REASON_MEMLIMIT = _lsf.SUB_REASON_MEMLIMIT
SUB_REASON_THREADLIMIT = _lsf.SUB_REASON_THREADLIMIT
SUB_REASON_SWAPLIMIT = _lsf.SUB_REASON_SWAPLIMIT
SUB_REASON_CRAYX1_ACCOUNTID = _lsf.SUB_REASON_CRAYX1_ACCOUNTID
SUB_REASON_CRAYX1_ATTRIBUTE = _lsf.SUB_REASON_CRAYX1_ATTRIBUTE
SUB_REASON_CRAYX1_BLOCKED = _lsf.SUB_REASON_CRAYX1_BLOCKED
SUB_REASON_CRAYX1_RESTART = _lsf.SUB_REASON_CRAYX1_RESTART
SUB_REASON_CRAYX1_DEPTH = _lsf.SUB_REASON_CRAYX1_DEPTH
SUB_REASON_CRAYX1_GID = _lsf.SUB_REASON_CRAYX1_GID
SUB_REASON_CRAYX1_GASID = _lsf.SUB_REASON_CRAYX1_GASID
SUB_REASON_CRAYX1_HARDLABEL = _lsf.SUB_REASON_CRAYX1_HARDLABEL
SUB_REASON_CRAYX1_LIMIT = _lsf.SUB_REASON_CRAYX1_LIMIT
SUB_REASON_CRAYX1_MEMORY = _lsf.SUB_REASON_CRAYX1_MEMORY
SUB_REASON_CRAYX1_SOFTLABEL = _lsf.SUB_REASON_CRAYX1_SOFTLABEL
SUB_REASON_CRAYX1_SIZE = _lsf.SUB_REASON_CRAYX1_SIZE
SUB_REASON_CRAYX1_TIME = _lsf.SUB_REASON_CRAYX1_TIME
SUB_REASON_CRAYX1_UID = _lsf.SUB_REASON_CRAYX1_UID
SUB_REASON_CRAYX1_WIDTH = _lsf.SUB_REASON_CRAYX1_WIDTH
EXIT_NORMAL = _lsf.EXIT_NORMAL
EXIT_RESTART = _lsf.EXIT_RESTART
EXIT_ZOMBIE = _lsf.EXIT_ZOMBIE
FINISH_PEND = _lsf.FINISH_PEND
EXIT_KILL_ZOMBIE = _lsf.EXIT_KILL_ZOMBIE
EXIT_ZOMBIE_JOB = _lsf.EXIT_ZOMBIE_JOB
EXIT_RERUN = _lsf.EXIT_RERUN
EXIT_NO_MAPPING = _lsf.EXIT_NO_MAPPING
EXIT_REMOTE_PERMISSION = _lsf.EXIT_REMOTE_PERMISSION
EXIT_INIT_ENVIRON = _lsf.EXIT_INIT_ENVIRON
EXIT_PRE_EXEC = _lsf.EXIT_PRE_EXEC
EXIT_REQUEUE = _lsf.EXIT_REQUEUE
EXIT_REMOVE = _lsf.EXIT_REMOVE
EXIT_VALUE_REQUEUE = _lsf.EXIT_VALUE_REQUEUE
EXIT_CANCEL = _lsf.EXIT_CANCEL
EXIT_MED_KILLED = _lsf.EXIT_MED_KILLED
EXIT_REMOTE_LEASE_JOB = _lsf.EXIT_REMOTE_LEASE_JOB
EXIT_CWD_NOTEXIST = _lsf.EXIT_CWD_NOTEXIST
LSB_MODE_BATCH = _lsf.LSB_MODE_BATCH
LSB_MODE_JS = _lsf.LSB_MODE_JS
LSBE_NO_ERROR = _lsf.LSBE_NO_ERROR
LSBE_NO_JOB = _lsf.LSBE_NO_JOB
LSBE_NOT_STARTED = _lsf.LSBE_NOT_STARTED
LSBE_JOB_STARTED = _lsf.LSBE_JOB_STARTED
LSBE_JOB_FINISH = _lsf.LSBE_JOB_FINISH
LSBE_STOP_JOB = _lsf.LSBE_STOP_JOB
LSBE_DEPEND_SYNTAX = _lsf.LSBE_DEPEND_SYNTAX
LSBE_EXCLUSIVE = _lsf.LSBE_EXCLUSIVE
LSBE_ROOT = _lsf.LSBE_ROOT
LSBE_MIGRATION = _lsf.LSBE_MIGRATION
LSBE_J_UNCHKPNTABLE = _lsf.LSBE_J_UNCHKPNTABLE
LSBE_NO_OUTPUT = _lsf.LSBE_NO_OUTPUT
LSBE_NO_JOBID = _lsf.LSBE_NO_JOBID
LSBE_ONLY_INTERACTIVE = _lsf.LSBE_ONLY_INTERACTIVE
LSBE_NO_INTERACTIVE = _lsf.LSBE_NO_INTERACTIVE
LSBE_NO_USER = _lsf.LSBE_NO_USER
LSBE_BAD_USER = _lsf.LSBE_BAD_USER
LSBE_PERMISSION = _lsf.LSBE_PERMISSION
LSBE_BAD_QUEUE = _lsf.LSBE_BAD_QUEUE
LSBE_QUEUE_NAME = _lsf.LSBE_QUEUE_NAME
LSBE_QUEUE_CLOSED = _lsf.LSBE_QUEUE_CLOSED
LSBE_QUEUE_WINDOW = _lsf.LSBE_QUEUE_WINDOW
LSBE_QUEUE_USE = _lsf.LSBE_QUEUE_USE
LSBE_BAD_HOST = _lsf.LSBE_BAD_HOST
LSBE_PROC_NUM = _lsf.LSBE_PROC_NUM
LSBE_NO_HPART = _lsf.LSBE_NO_HPART
LSBE_BAD_HPART = _lsf.LSBE_BAD_HPART
LSBE_NO_GROUP = _lsf.LSBE_NO_GROUP
LSBE_BAD_GROUP = _lsf.LSBE_BAD_GROUP
LSBE_QUEUE_HOST = _lsf.LSBE_QUEUE_HOST
LSBE_UJOB_LIMIT = _lsf.LSBE_UJOB_LIMIT
LSBE_NO_HOST = _lsf.LSBE_NO_HOST
LSBE_BAD_CHKLOG = _lsf.LSBE_BAD_CHKLOG
LSBE_PJOB_LIMIT = _lsf.LSBE_PJOB_LIMIT
LSBE_NOLSF_HOST = _lsf.LSBE_NOLSF_HOST
LSBE_BAD_ARG = _lsf.LSBE_BAD_ARG
LSBE_BAD_TIME = _lsf.LSBE_BAD_TIME
LSBE_START_TIME = _lsf.LSBE_START_TIME
LSBE_BAD_LIMIT = _lsf.LSBE_BAD_LIMIT
LSBE_OVER_LIMIT = _lsf.LSBE_OVER_LIMIT
LSBE_BAD_CMD = _lsf.LSBE_BAD_CMD
LSBE_BAD_SIGNAL = _lsf.LSBE_BAD_SIGNAL
LSBE_BAD_JOB = _lsf.LSBE_BAD_JOB
LSBE_QJOB_LIMIT = _lsf.LSBE_QJOB_LIMIT
LSBE_BAD_TERM = _lsf.LSBE_BAD_TERM
LSBE_UNKNOWN_EVENT = _lsf.LSBE_UNKNOWN_EVENT
LSBE_EVENT_FORMAT = _lsf.LSBE_EVENT_FORMAT
LSBE_EOF = _lsf.LSBE_EOF
LSBE_MBATCHD = _lsf.LSBE_MBATCHD
LSBE_SBATCHD = _lsf.LSBE_SBATCHD
LSBE_LSBLIB = _lsf.LSBE_LSBLIB
LSBE_LSLIB = _lsf.LSBE_LSLIB
LSBE_SYS_CALL = _lsf.LSBE_SYS_CALL
LSBE_NO_MEM = _lsf.LSBE_NO_MEM
LSBE_SERVICE = _lsf.LSBE_SERVICE
LSBE_NO_ENV = _lsf.LSBE_NO_ENV
LSBE_CHKPNT_CALL = _lsf.LSBE_CHKPNT_CALL
LSBE_NO_FORK = _lsf.LSBE_NO_FORK
LSBE_PROTOCOL = _lsf.LSBE_PROTOCOL
LSBE_XDR = _lsf.LSBE_XDR
LSBE_PORT = _lsf.LSBE_PORT
LSBE_TIME_OUT = _lsf.LSBE_TIME_OUT
LSBE_CONN_TIMEOUT = _lsf.LSBE_CONN_TIMEOUT
LSBE_CONN_REFUSED = _lsf.LSBE_CONN_REFUSED
LSBE_CONN_EXIST = _lsf.LSBE_CONN_EXIST
LSBE_CONN_NONEXIST = _lsf.LSBE_CONN_NONEXIST
LSBE_SBD_UNREACH = _lsf.LSBE_SBD_UNREACH
LSBE_OP_RETRY = _lsf.LSBE_OP_RETRY
LSBE_USER_JLIMIT = _lsf.LSBE_USER_JLIMIT
LSBE_NQS_BAD_PAR = _lsf.LSBE_NQS_BAD_PAR
LSBE_NO_LICENSE = _lsf.LSBE_NO_LICENSE
LSBE_BAD_CALENDAR = _lsf.LSBE_BAD_CALENDAR
LSBE_NOMATCH_CALENDAR = _lsf.LSBE_NOMATCH_CALENDAR
LSBE_NO_CALENDAR = _lsf.LSBE_NO_CALENDAR
LSBE_BAD_TIMEEVENT = _lsf.LSBE_BAD_TIMEEVENT
LSBE_CAL_EXIST = _lsf.LSBE_CAL_EXIST
LSBE_CAL_DISABLED = _lsf.LSBE_CAL_DISABLED
LSBE_JOB_MODIFY = _lsf.LSBE_JOB_MODIFY
LSBE_JOB_MODIFY_ONCE = _lsf.LSBE_JOB_MODIFY_ONCE
LSBE_J_UNREPETITIVE = _lsf.LSBE_J_UNREPETITIVE
LSBE_BAD_CLUSTER = _lsf.LSBE_BAD_CLUSTER
LSBE_PEND_CAL_JOB = _lsf.LSBE_PEND_CAL_JOB
LSBE_RUN_CAL_JOB = _lsf.LSBE_RUN_CAL_JOB
LSBE_JOB_MODIFY_USED = _lsf.LSBE_JOB_MODIFY_USED
LSBE_AFS_TOKENS = _lsf.LSBE_AFS_TOKENS
LSBE_BAD_EVENT = _lsf.LSBE_BAD_EVENT
LSBE_NOMATCH_EVENT = _lsf.LSBE_NOMATCH_EVENT
LSBE_NO_EVENT = _lsf.LSBE_NO_EVENT
LSBE_HJOB_LIMIT = _lsf.LSBE_HJOB_LIMIT
LSBE_MSG_DELIVERED = _lsf.LSBE_MSG_DELIVERED
LSBE_NO_JOBMSG = _lsf.LSBE_NO_JOBMSG
LSBE_MSG_RETRY = _lsf.LSBE_MSG_RETRY
LSBE_BAD_RESREQ = _lsf.LSBE_BAD_RESREQ
LSBE_NO_ENOUGH_HOST = _lsf.LSBE_NO_ENOUGH_HOST
LSBE_CONF_FATAL = _lsf.LSBE_CONF_FATAL
LSBE_CONF_WARNING = _lsf.LSBE_CONF_WARNING
LSBE_CAL_MODIFY = _lsf.LSBE_CAL_MODIFY
LSBE_JOB_CAL_MODIFY = _lsf.LSBE_JOB_CAL_MODIFY
LSBE_HP_FAIRSHARE_DEF = _lsf.LSBE_HP_FAIRSHARE_DEF
LSBE_NO_RESOURCE = _lsf.LSBE_NO_RESOURCE
LSBE_BAD_RESOURCE = _lsf.LSBE_BAD_RESOURCE
LSBE_INTERACTIVE_CAL = _lsf.LSBE_INTERACTIVE_CAL
LSBE_INTERACTIVE_RERUN = _lsf.LSBE_INTERACTIVE_RERUN
LSBE_PTY_INFILE = _lsf.LSBE_PTY_INFILE
LSBE_JS_DISABLED = _lsf.LSBE_JS_DISABLED
LSBE_BAD_SUBMISSION_HOST = _lsf.LSBE_BAD_SUBMISSION_HOST
LSBE_LOCK_JOB = _lsf.LSBE_LOCK_JOB
LSBE_UGROUP_MEMBER = _lsf.LSBE_UGROUP_MEMBER
LSBE_UNSUPPORTED_MC = _lsf.LSBE_UNSUPPORTED_MC
LSBE_PERMISSION_MC = _lsf.LSBE_PERMISSION_MC
LSBE_SYSCAL_EXIST = _lsf.LSBE_SYSCAL_EXIST
LSBE_OVER_RUSAGE = _lsf.LSBE_OVER_RUSAGE
LSBE_BAD_HOST_SPEC = _lsf.LSBE_BAD_HOST_SPEC
LSBE_SYNTAX_CALENDAR = _lsf.LSBE_SYNTAX_CALENDAR
LSBE_CAL_USED = _lsf.LSBE_CAL_USED
LSBE_CAL_CYC = _lsf.LSBE_CAL_CYC
LSBE_BAD_UGROUP = _lsf.LSBE_BAD_UGROUP
LSBE_ESUB_ABORT = _lsf.LSBE_ESUB_ABORT
LSBE_EXCEPT_SYNTAX = _lsf.LSBE_EXCEPT_SYNTAX
LSBE_EXCEPT_COND = _lsf.LSBE_EXCEPT_COND
LSBE_EXCEPT_ACTION = _lsf.LSBE_EXCEPT_ACTION
LSBE_JOB_DEP = _lsf.LSBE_JOB_DEP
LSBE_JGRP_EXIST = _lsf.LSBE_JGRP_EXIST
LSBE_JGRP_NULL = _lsf.LSBE_JGRP_NULL
LSBE_JGRP_HASJOB = _lsf.LSBE_JGRP_HASJOB
LSBE_JGRP_CTRL_UNKWN = _lsf.LSBE_JGRP_CTRL_UNKWN
LSBE_JGRP_BAD = _lsf.LSBE_JGRP_BAD
LSBE_JOB_ARRAY = _lsf.LSBE_JOB_ARRAY
LSBE_JOB_SUSP = _lsf.LSBE_JOB_SUSP
LSBE_JOB_FORW = _lsf.LSBE_JOB_FORW
LSBE_JGRP_HOLD = _lsf.LSBE_JGRP_HOLD
LSBE_BAD_IDX = _lsf.LSBE_BAD_IDX
LSBE_BIG_IDX = _lsf.LSBE_BIG_IDX
LSBE_ARRAY_NULL = _lsf.LSBE_ARRAY_NULL
LSBE_CAL_VOID = _lsf.LSBE_CAL_VOID
LSBE_JOB_EXIST = _lsf.LSBE_JOB_EXIST
LSBE_JOB_ELEMENT = _lsf.LSBE_JOB_ELEMENT
LSBE_BAD_JOBID = _lsf.LSBE_BAD_JOBID
LSBE_MOD_JOB_NAME = _lsf.LSBE_MOD_JOB_NAME
LSBE_BAD_FRAME = _lsf.LSBE_BAD_FRAME
LSBE_FRAME_BIG_IDX = _lsf.LSBE_FRAME_BIG_IDX
LSBE_FRAME_BAD_IDX = _lsf.LSBE_FRAME_BAD_IDX
LSBE_PREMATURE = _lsf.LSBE_PREMATURE
LSBE_BAD_PROJECT_GROUP = _lsf.LSBE_BAD_PROJECT_GROUP
LSBE_NO_HOST_GROUP = _lsf.LSBE_NO_HOST_GROUP
LSBE_NO_USER_GROUP = _lsf.LSBE_NO_USER_GROUP
LSBE_INDEX_FORMAT = _lsf.LSBE_INDEX_FORMAT
LSBE_SP_SRC_NOT_SEEN = _lsf.LSBE_SP_SRC_NOT_SEEN
LSBE_SP_FAILED_HOSTS_LIM = _lsf.LSBE_SP_FAILED_HOSTS_LIM
LSBE_SP_COPY_FAILED = _lsf.LSBE_SP_COPY_FAILED
LSBE_SP_FORK_FAILED = _lsf.LSBE_SP_FORK_FAILED
LSBE_SP_CHILD_DIES = _lsf.LSBE_SP_CHILD_DIES
LSBE_SP_CHILD_FAILED = _lsf.LSBE_SP_CHILD_FAILED
LSBE_SP_FIND_HOST_FAILED = _lsf.LSBE_SP_FIND_HOST_FAILED
LSBE_SP_SPOOLDIR_FAILED = _lsf.LSBE_SP_SPOOLDIR_FAILED
LSBE_SP_DELETE_FAILED = _lsf.LSBE_SP_DELETE_FAILED
LSBE_BAD_USER_PRIORITY = _lsf.LSBE_BAD_USER_PRIORITY
LSBE_NO_JOB_PRIORITY = _lsf.LSBE_NO_JOB_PRIORITY
LSBE_JOB_REQUEUED = _lsf.LSBE_JOB_REQUEUED
LSBE_JOB_REQUEUE_REMOTE = _lsf.LSBE_JOB_REQUEUE_REMOTE
LSBE_NQS_NO_ARRJOB = _lsf.LSBE_NQS_NO_ARRJOB
LSBE_BAD_EXT_MSGID = _lsf.LSBE_BAD_EXT_MSGID
LSBE_NO_IFREG = _lsf.LSBE_NO_IFREG
LSBE_BAD_ATTA_DIR = _lsf.LSBE_BAD_ATTA_DIR
LSBE_COPY_DATA = _lsf.LSBE_COPY_DATA
LSBE_JOB_ATTA_LIMIT = _lsf.LSBE_JOB_ATTA_LIMIT
LSBE_CHUNK_JOB = _lsf.LSBE_CHUNK_JOB
LSBE_DLOGD_ISCONN = _lsf.LSBE_DLOGD_ISCONN
LSBE_MULTI_FIRST_HOST = _lsf.LSBE_MULTI_FIRST_HOST
LSBE_HG_FIRST_HOST = _lsf.LSBE_HG_FIRST_HOST
LSBE_HP_FIRST_HOST = _lsf.LSBE_HP_FIRST_HOST
LSBE_OTHERS_FIRST_HOST = _lsf.LSBE_OTHERS_FIRST_HOST
LSBE_MC_HOST = _lsf.LSBE_MC_HOST
LSBE_MC_REPETITIVE = _lsf.LSBE_MC_REPETITIVE
LSBE_MC_CHKPNT = _lsf.LSBE_MC_CHKPNT
LSBE_MC_EXCEPTION = _lsf.LSBE_MC_EXCEPTION
LSBE_MC_TIMEEVENT = _lsf.LSBE_MC_TIMEEVENT
LSBE_PROC_LESS = _lsf.LSBE_PROC_LESS
LSBE_MOD_MIX_OPTS = _lsf.LSBE_MOD_MIX_OPTS
LSBE_MOD_REMOTE = _lsf.LSBE_MOD_REMOTE
LSBE_MOD_CPULIMIT = _lsf.LSBE_MOD_CPULIMIT
LSBE_MOD_MEMLIMIT = _lsf.LSBE_MOD_MEMLIMIT
LSBE_MOD_ERRFILE = _lsf.LSBE_MOD_ERRFILE
LSBE_LOCKED_MASTER = _lsf.LSBE_LOCKED_MASTER
LSBE_WARNING_INVALID_TIME_PERIOD = _lsf.LSBE_WARNING_INVALID_TIME_PERIOD
LSBE_WARNING_MISSING = _lsf.LSBE_WARNING_MISSING
LSBE_DEP_ARRAY_SIZE = _lsf.LSBE_DEP_ARRAY_SIZE
LSBE_FEWER_PROCS = _lsf.LSBE_FEWER_PROCS
LSBE_BAD_RSVID = _lsf.LSBE_BAD_RSVID
LSBE_NO_RSVID = _lsf.LSBE_NO_RSVID
LSBE_NO_EXPORT_HOST = _lsf.LSBE_NO_EXPORT_HOST
LSBE_REMOTE_HOST_CONTROL = _lsf.LSBE_REMOTE_HOST_CONTROL
LSBE_REMOTE_CLOSED = _lsf.LSBE_REMOTE_CLOSED
LSBE_USER_SUSPENDED = _lsf.LSBE_USER_SUSPENDED
LSBE_ADMIN_SUSPENDED = _lsf.LSBE_ADMIN_SUSPENDED
LSBE_NOT_LOCAL_HOST = _lsf.LSBE_NOT_LOCAL_HOST
LSBE_LEASE_INACTIVE = _lsf.LSBE_LEASE_INACTIVE
LSBE_QUEUE_ADRSV = _lsf.LSBE_QUEUE_ADRSV
LSBE_HOST_NOT_EXPORTED = _lsf.LSBE_HOST_NOT_EXPORTED
LSBE_HOST_ADRSV = _lsf.LSBE_HOST_ADRSV
LSBE_MC_CONN_NONEXIST = _lsf.LSBE_MC_CONN_NONEXIST
LSBE_RL_BREAK = _lsf.LSBE_RL_BREAK
LSBE_LSF2TP_PREEMPT = _lsf.LSBE_LSF2TP_PREEMPT
LSBE_LSF2TP_RESERVE = _lsf.LSBE_LSF2TP_RESERVE
LSBE_LSF2TP_BACKFILL = _lsf.LSBE_LSF2TP_BACKFILL
LSBE_RSV_POLICY_NAME_BAD = _lsf.LSBE_RSV_POLICY_NAME_BAD
LSBE_RSV_POLICY_PERMISSION_DENIED = _lsf.LSBE_RSV_POLICY_PERMISSION_DENIED
LSBE_RSV_POLICY_USER = _lsf.LSBE_RSV_POLICY_USER
LSBE_RSV_POLICY_HOST = _lsf.LSBE_RSV_POLICY_HOST
LSBE_RSV_POLICY_TIMEWINDOW = _lsf.LSBE_RSV_POLICY_TIMEWINDOW
LSBE_RSV_POLICY_DISABLED = _lsf.LSBE_RSV_POLICY_DISABLED
LSBE_LIM_NO_GENERAL_LIMIT = _lsf.LSBE_LIM_NO_GENERAL_LIMIT
LSBE_LIM_NO_RSRC_USAGE = _lsf.LSBE_LIM_NO_RSRC_USAGE
LSBE_LIM_CONVERT_ERROR = _lsf.LSBE_LIM_CONVERT_ERROR
LSBE_RSV_NO_HOST = _lsf.LSBE_RSV_NO_HOST
LSBE_MOD_JGRP_ARRAY = _lsf.LSBE_MOD_JGRP_ARRAY
LSBE_MOD_MIX = _lsf.LSBE_MOD_MIX
LSBE_SLA_NULL = _lsf.LSBE_SLA_NULL
LSBE_MOD_JGRP_SLA = _lsf.LSBE_MOD_JGRP_SLA
LSBE_SLA_MEMBER = _lsf.LSBE_SLA_MEMBER
LSBE_NO_EXCEPTIONAL_HOST = _lsf.LSBE_NO_EXCEPTIONAL_HOST
LSBE_WARNING_INVALID_ACTION = _lsf.LSBE_WARNING_INVALID_ACTION
LSBE_EXTSCHED_SYNTAX = _lsf.LSBE_EXTSCHED_SYNTAX
LSBE_SLA_RMT_ONLY_QUEUE = _lsf.LSBE_SLA_RMT_ONLY_QUEUE
LSBE_MOD_SLA_ARRAY = _lsf.LSBE_MOD_SLA_ARRAY
LSBE_MOD_SLA_JGRP = _lsf.LSBE_MOD_SLA_JGRP
LSBE_MAX_PEND = _lsf.LSBE_MAX_PEND
LSBE_CONCURRENT = _lsf.LSBE_CONCURRENT
LSBE_FEATURE_NULL = _lsf.LSBE_FEATURE_NULL
LSBE_DYNGRP_MEMBER = _lsf.LSBE_DYNGRP_MEMBER
LSBE_BAD_DYN_HOST = _lsf.LSBE_BAD_DYN_HOST
LSBE_NO_GRP_MEMBER = _lsf.LSBE_NO_GRP_MEMBER
LSBE_JOB_INFO_FILE = _lsf.LSBE_JOB_INFO_FILE
LSBE_MOD_OR_RUSAGE = _lsf.LSBE_MOD_OR_RUSAGE
LSBE_BAD_GROUP_NAME = _lsf.LSBE_BAD_GROUP_NAME
LSBE_BAD_HOST_NAME = _lsf.LSBE_BAD_HOST_NAME
LSBE_DT_BSUB = _lsf.LSBE_DT_BSUB
LSBE_PARENT_SYM_JOB = _lsf.LSBE_PARENT_SYM_JOB
LSBE_PARTITION_NO_CPU = _lsf.LSBE_PARTITION_NO_CPU
LSBE_PARTITION_BATCH = _lsf.LSBE_PARTITION_BATCH
LSBE_PARTITION_ONLINE = _lsf.LSBE_PARTITION_ONLINE
LSBE_NOLICENSE_BATCH = _lsf.LSBE_NOLICENSE_BATCH
LSBE_NOLICENSE_ONLINE = _lsf.LSBE_NOLICENSE_ONLINE
LSBE_SIGNAL_SRVJOB = _lsf.LSBE_SIGNAL_SRVJOB
LSBE_BEGIN_TIME_INVALID = _lsf.LSBE_BEGIN_TIME_INVALID
LSBE_END_TIME_INVALID = _lsf.LSBE_END_TIME_INVALID
LSBE_BAD_REG_EXPR = _lsf.LSBE_BAD_REG_EXPR
LSBE_GRP_REG_EXPR = _lsf.LSBE_GRP_REG_EXPR
LSBE_GRP_HAVE_NO_MEMB = _lsf.LSBE_GRP_HAVE_NO_MEMB
LSBE_APP_NULL = _lsf.LSBE_APP_NULL
LSBE_PROC_JOB_APP = _lsf.LSBE_PROC_JOB_APP
LSBE_PROC_APP_QUE = _lsf.LSBE_PROC_APP_QUE
LSBE_BAD_APPNAME = _lsf.LSBE_BAD_APPNAME
LSBE_APP_OVER_LIMIT = _lsf.LSBE_APP_OVER_LIMIT
LSBE_REMOVE_DEF_APP = _lsf.LSBE_REMOVE_DEF_APP
LSBE_EGO_DISABLED = _lsf.LSBE_EGO_DISABLED
LSBE_REMOTE_HOST = _lsf.LSBE_REMOTE_HOST
LSBE_SLA_EXCLUSIVE = _lsf.LSBE_SLA_EXCLUSIVE
LSBE_SLA_NONEXCLUSIVE = _lsf.LSBE_SLA_NONEXCLUSIVE
LSBE_PERFMON_STARTED = _lsf.LSBE_PERFMON_STARTED
LSBE_PERFMON_STOPED = _lsf.LSBE_PERFMON_STOPED
LSBE_PERFMON_PERIOD_SET = _lsf.LSBE_PERFMON_PERIOD_SET
LSBE_DEFAULT_SPOOL_DIR_DISABLED = _lsf.LSBE_DEFAULT_SPOOL_DIR_DISABLED
LSBE_APS_QUEUE_JOB = _lsf.LSBE_APS_QUEUE_JOB
LSBE_BAD_APS_JOB = _lsf.LSBE_BAD_APS_JOB
LSBE_BAD_APS_VAL = _lsf.LSBE_BAD_APS_VAL
LSBE_APS_STRING_UNDEF = _lsf.LSBE_APS_STRING_UNDEF
LSBE_SLA_JOB_APS_QUEUE = _lsf.LSBE_SLA_JOB_APS_QUEUE
LSBE_MOD_MIX_APS = _lsf.LSBE_MOD_MIX_APS
LSBE_APS_RANGE = _lsf.LSBE_APS_RANGE
LSBE_APS_ZERO = _lsf.LSBE_APS_ZERO
LSBE_DJOB_RES_PORT_UNKNOWN = _lsf.LSBE_DJOB_RES_PORT_UNKNOWN
LSBE_DJOB_RES_TIMEOUT = _lsf.LSBE_DJOB_RES_TIMEOUT
LSBE_DJOB_RES_IOERR = _lsf.LSBE_DJOB_RES_IOERR
LSBE_DJOB_RES_INTERNAL_FAILURE = _lsf.LSBE_DJOB_RES_INTERNAL_FAILURE
LSBE_DJOB_CAN_NOT_RUN = _lsf.LSBE_DJOB_CAN_NOT_RUN
LSBE_DJOB_VALIDATION_BAD_JOBID = _lsf.LSBE_DJOB_VALIDATION_BAD_JOBID
LSBE_DJOB_VALIDATION_BAD_HOST = _lsf.LSBE_DJOB_VALIDATION_BAD_HOST
LSBE_DJOB_VALIDATION_BAD_USER = _lsf.LSBE_DJOB_VALIDATION_BAD_USER
LSBE_DJOB_EXECUTE_TASK = _lsf.LSBE_DJOB_EXECUTE_TASK
LSBE_DJOB_WAIT_TASK = _lsf.LSBE_DJOB_WAIT_TASK
LSBE_APS_HPC = _lsf.LSBE_APS_HPC
LSBE_DIGEST_CHECK_BSUB = _lsf.LSBE_DIGEST_CHECK_BSUB
LSBE_DJOB_DISABLED = _lsf.LSBE_DJOB_DISABLED
LSBE_BAD_RUNTIME = _lsf.LSBE_BAD_RUNTIME
LSBE_BAD_RUNLIMIT = _lsf.LSBE_BAD_RUNLIMIT
LSBE_OVER_QUEUE_LIMIT = _lsf.LSBE_OVER_QUEUE_LIMIT
LSBE_SET_BY_RATIO = _lsf.LSBE_SET_BY_RATIO
LSBE_BAD_CWD = _lsf.LSBE_BAD_CWD
LSBE_JGRP_LIMIT_GRTR_THAN_PARENT = _lsf.LSBE_JGRP_LIMIT_GRTR_THAN_PARENT
LSBE_JGRP_LIMIT_LESS_THAN_CHILDREN = _lsf.LSBE_JGRP_LIMIT_LESS_THAN_CHILDREN
LSBE_NO_ARRAY_END_INDEX = _lsf.LSBE_NO_ARRAY_END_INDEX
LSBE_MOD_RUNTIME = _lsf.LSBE_MOD_RUNTIME
LSBE_BAD_SUCCESS_EXIT_VALUES = _lsf.LSBE_BAD_SUCCESS_EXIT_VALUES
LSBE_DUP_SUCCESS_EXIT_VALUES = _lsf.LSBE_DUP_SUCCESS_EXIT_VALUES
LSBE_NO_SUCCESS_EXIT_VALUES = _lsf.LSBE_NO_SUCCESS_EXIT_VALUES
LSBE_JOB_REQUEUE_BADARG = _lsf.LSBE_JOB_REQUEUE_BADARG
LSBE_JOB_REQUEUE_DUPLICATED = _lsf.LSBE_JOB_REQUEUE_DUPLICATED
LSBE_JOB_REQUEUE_INVALID_DIGIT = _lsf.LSBE_JOB_REQUEUE_INVALID_DIGIT
LSBE_JOB_REQUEUE_INVALID_TILDE = _lsf.LSBE_JOB_REQUEUE_INVALID_TILDE
LSBE_JOB_REQUEUE_NOVALID = _lsf.LSBE_JOB_REQUEUE_NOVALID
LSBE_NO_JGRP = _lsf.LSBE_NO_JGRP
LSBE_NOT_CONSUMABLE = _lsf.LSBE_NOT_CONSUMABLE
LSBE_RSV_BAD_EXEC = _lsf.LSBE_RSV_BAD_EXEC
LSBE_RSV_EVENTTYPE = _lsf.LSBE_RSV_EVENTTYPE
LSBE_RSV_SHIFT = _lsf.LSBE_RSV_SHIFT
LSBE_RSV_USHIFT = _lsf.LSBE_RSV_USHIFT
LSBE_RSV_NUMEVENTS = _lsf.LSBE_RSV_NUMEVENTS
LSBE_ADRSV_ID_VALID = _lsf.LSBE_ADRSV_ID_VALID
LSBE_ADRSV_DISABLE_NONRECUR = _lsf.LSBE_ADRSV_DISABLE_NONRECUR
LSBE_ADRSV_MOD_ACTINSTANCE = _lsf.LSBE_ADRSV_MOD_ACTINSTANCE
LSBE_ADRSV_HOST_NOTAVAIL = _lsf.LSBE_ADRSV_HOST_NOTAVAIL
LSBE_ADRSV_TIME_MOD_FAIL = _lsf.LSBE_ADRSV_TIME_MOD_FAIL
LSBE_ADRSV_R_AND_N = _lsf.LSBE_ADRSV_R_AND_N
LSBE_ADRSV_EMPTY = _lsf.LSBE_ADRSV_EMPTY
LSBE_ADRSV_SWITCHTYPE = _lsf.LSBE_ADRSV_SWITCHTYPE
LSBE_ADRSV_SYS_N = _lsf.LSBE_ADRSV_SYS_N
LSBE_ADRSV_DISABLE = _lsf.LSBE_ADRSV_DISABLE
LSBE_ADRSV_ID_UNIQUE = _lsf.LSBE_ADRSV_ID_UNIQUE
LSBE_BAD_RSVNAME = _lsf.LSBE_BAD_RSVNAME
LSBE_ADVRSV_ACTIVESTART = _lsf.LSBE_ADVRSV_ACTIVESTART
LSBE_ADRSV_ID_USED = _lsf.LSBE_ADRSV_ID_USED
LSBE_ADRSV_PREVDISABLED = _lsf.LSBE_ADRSV_PREVDISABLED
LSBE_ADRSV_DISABLECURR = _lsf.LSBE_ADRSV_DISABLECURR
LSBE_ADRSV_NOT_RSV_HOST = _lsf.LSBE_ADRSV_NOT_RSV_HOST
LSBE_RESREQ_OK = _lsf.LSBE_RESREQ_OK
LSBE_RESREQ_ERR = _lsf.LSBE_RESREQ_ERR
LSBE_ADRSV_HOST_USED = _lsf.LSBE_ADRSV_HOST_USED
LSBE_BAD_CHKPNTDIR = _lsf.LSBE_BAD_CHKPNTDIR
LSBE_ADRSV_MOD_REMOTE = _lsf.LSBE_ADRSV_MOD_REMOTE
LSBE_JOB_REQUEUE_BADEXCLUDE = _lsf.LSBE_JOB_REQUEUE_BADEXCLUDE
LSBE_ADRSV_DISABLE_DATE = _lsf.LSBE_ADRSV_DISABLE_DATE
LSBE_ADRSV_DETACH_MIX = _lsf.LSBE_ADRSV_DETACH_MIX
LSBE_ADRSV_DETACH_ACTIVE = _lsf.LSBE_ADRSV_DETACH_ACTIVE
LSBE_MISSING_START_END_TIME = _lsf.LSBE_MISSING_START_END_TIME
LSBE_JOB_RUSAGE_EXCEED_LIMIT = _lsf.LSBE_JOB_RUSAGE_EXCEED_LIMIT
LSBE_APP_RUSAGE_EXCEED_LIMIT = _lsf.LSBE_APP_RUSAGE_EXCEED_LIMIT
LSBE_CANDIDATE_HOST_EMPTY = _lsf.LSBE_CANDIDATE_HOST_EMPTY
LSBE_HS_BAD_AFTER_BRACKT = _lsf.LSBE_HS_BAD_AFTER_BRACKT
LSBE_HS_NO_END_INDEX = _lsf.LSBE_HS_NO_END_INDEX
LSBE_HS_BAD_COMMA = _lsf.LSBE_HS_BAD_COMMA
LSBE_HS_BAD_FORMAT = _lsf.LSBE_HS_BAD_FORMAT
LSBE_HS_BAD_ORDER = _lsf.LSBE_HS_BAD_ORDER
LSBE_HS_BAD_MANY_DIGITS = _lsf.LSBE_HS_BAD_MANY_DIGITS
LSBE_HS_BAD_NUM_DIGITS = _lsf.LSBE_HS_BAD_NUM_DIGITS
LSBE_HS_BAD_END_INDEX = _lsf.LSBE_HS_BAD_END_INDEX
LSBE_HS_BAD_INDEX = _lsf.LSBE_HS_BAD_INDEX
LSBE_COMMENTS = _lsf.LSBE_COMMENTS
LSBE_FIRST_HOSTS_NOT_IN_QUEUE = _lsf.LSBE_FIRST_HOSTS_NOT_IN_QUEUE
LSBE_JOB_NOTSTART = _lsf.LSBE_JOB_NOTSTART
LSBE_RUNTIME_INVAL = _lsf.LSBE_RUNTIME_INVAL
LSBE_SSH_NOT_INTERACTIVE = _lsf.LSBE_SSH_NOT_INTERACTIVE
LSBE_LESS_RUNTIME = _lsf.LSBE_LESS_RUNTIME
LSBE_RESIZE_NOTIFY_CMD_LEN = _lsf.LSBE_RESIZE_NOTIFY_CMD_LEN
LSBE_JOB_RESIZABLE = _lsf.LSBE_JOB_RESIZABLE
LSBE_RESIZE_RELEASE_HOSTSPEC = _lsf.LSBE_RESIZE_RELEASE_HOSTSPEC
LSBE_NO_RESIZE_NOTIFY = _lsf.LSBE_NO_RESIZE_NOTIFY
LSBE_RESIZE_RELEASE_FRISTHOST = _lsf.LSBE_RESIZE_RELEASE_FRISTHOST
LSBE_RESIZE_EVENT_INPROGRESS = _lsf.LSBE_RESIZE_EVENT_INPROGRESS
LSBE_RESIZE_BAD_SLOTS = _lsf.LSBE_RESIZE_BAD_SLOTS
LSBE_RESIZE_NO_ACTIVE_REQUEST = _lsf.LSBE_RESIZE_NO_ACTIVE_REQUEST
LSBE_HOST_NOT_IN_ALLOC = _lsf.LSBE_HOST_NOT_IN_ALLOC
LSBE_RESIZE_RELEASE_NOOP = _lsf.LSBE_RESIZE_RELEASE_NOOP
LSBE_RESIZE_URGENT_JOB = _lsf.LSBE_RESIZE_URGENT_JOB
LSBE_RESIZE_EGO_SLA_COEXIST = _lsf.LSBE_RESIZE_EGO_SLA_COEXIST
LSBE_HOST_NOT_SUPPORT_RESIZE = _lsf.LSBE_HOST_NOT_SUPPORT_RESIZE
LSBE_APP_RESIZABLE = _lsf.LSBE_APP_RESIZABLE
LSBE_RESIZE_LOST_AND_FOUND = _lsf.LSBE_RESIZE_LOST_AND_FOUND
LSBE_RESIZE_FIRSTHOST_LOST_AND_FOUND = _lsf.LSBE_RESIZE_FIRSTHOST_LOST_AND_FOUND
LSBE_RESIZE_BAD_HOST = _lsf.LSBE_RESIZE_BAD_HOST
LSBE_AUTORESIZE_APP = _lsf.LSBE_AUTORESIZE_APP
LSBE_RESIZE_PENDING_REQUEST = _lsf.LSBE_RESIZE_PENDING_REQUEST
LSBE_ASKED_HOSTS_NUMBER = _lsf.LSBE_ASKED_HOSTS_NUMBER
LSBE_AR_HOST_EMPTY = _lsf.LSBE_AR_HOST_EMPTY
LSBE_AR_FIRST_HOST_EMPTY = _lsf.LSBE_AR_FIRST_HOST_EMPTY
LSBE_JB = _lsf.LSBE_JB
LSBE_JB_DBLIB = _lsf.LSBE_JB_DBLIB
LSBE_JB_DB_UNREACH = _lsf.LSBE_JB_DB_UNREACH
LSBE_JB_MBD_UNREACH = _lsf.LSBE_JB_MBD_UNREACH
LSBE_JB_BES = _lsf.LSBE_JB_BES
LSBE_JB_BES_UNSUPPORTED_OP = _lsf.LSBE_JB_BES_UNSUPPORTED_OP
LSBE_LS_PROJECT_NAME = _lsf.LSBE_LS_PROJECT_NAME
LSBE_END_TIME_INVALID_COMPARE_START = _lsf.LSBE_END_TIME_INVALID_COMPARE_START
LSBE_HP_REDUNDANT_HOST = _lsf.LSBE_HP_REDUNDANT_HOST
LSBE_COMPOUND_APP_SLOTS = _lsf.LSBE_COMPOUND_APP_SLOTS
LSBE_COMPOUND_QUEUE_SLOTS = _lsf.LSBE_COMPOUND_QUEUE_SLOTS
LSBE_COMPOUND_RESIZE = _lsf.LSBE_COMPOUND_RESIZE
LSBE_CU_OVERLAPPING_HOST = _lsf.LSBE_CU_OVERLAPPING_HOST
LSBE_CU_BAD_HOST = _lsf.LSBE_CU_BAD_HOST
LSBE_CU_HOST_NOT_ALLOWED = _lsf.LSBE_CU_HOST_NOT_ALLOWED
LSBE_CU_NOT_LOWEST_LEVEL = _lsf.LSBE_CU_NOT_LOWEST_LEVEL
LSBE_CU_MOD_RESREQ = _lsf.LSBE_CU_MOD_RESREQ
LSBE_CU_AUTORESIZE = _lsf.LSBE_CU_AUTORESIZE
LSBE_NO_COMPUTE_UNIT_TYPES = _lsf.LSBE_NO_COMPUTE_UNIT_TYPES
LSBE_NO_COMPUTE_UNIT = _lsf.LSBE_NO_COMPUTE_UNIT
LSBE_BAD_COMPUTE_UNIT = _lsf.LSBE_BAD_COMPUTE_UNIT
LSBE_CU_EXCLUSIVE = _lsf.LSBE_CU_EXCLUSIVE
LSBE_CU_EXCLUSIVE_LEVEL = _lsf.LSBE_CU_EXCLUSIVE_LEVEL
LSBE_CU_SWITCH = _lsf.LSBE_CU_SWITCH
LSBE_COMPOUND_JOB_SLOTS = _lsf.LSBE_COMPOUND_JOB_SLOTS
LSBE_COMPOUND_QUEUE_RUSAGE_OR = _lsf.LSBE_COMPOUND_QUEUE_RUSAGE_OR
LSBE_CU_BALANCE_USABLECUSLOTS = _lsf.LSBE_CU_BALANCE_USABLECUSLOTS
LSBE_COMPOUND_TSJOB_APP = _lsf.LSBE_COMPOUND_TSJOB_APP
LSBE_COMPOUND_TSJOB_QUEUE = _lsf.LSBE_COMPOUND_TSJOB_QUEUE
LSBE_EXCEED_MAX_JOB_NAME_DEP = _lsf.LSBE_EXCEED_MAX_JOB_NAME_DEP
LSBE_WAIT_FOR_MC_SYNC = _lsf.LSBE_WAIT_FOR_MC_SYNC
LSBE_RUSAGE_EXCEED_RESRSV_LIMIT = _lsf.LSBE_RUSAGE_EXCEED_RESRSV_LIMIT
LSBE_JOB_DESCRIPTION_LEN = _lsf.LSBE_JOB_DESCRIPTION_LEN
LSBE_NOT_IN_SIMMODE = _lsf.LSBE_NOT_IN_SIMMODE
LSBE_SIM_OPT_RUNTIME = _lsf.LSBE_SIM_OPT_RUNTIME
LSBE_SIM_OPT_CPUTIME = _lsf.LSBE_SIM_OPT_CPUTIME
LSBE_SIM_OPT_MAXMEM = _lsf.LSBE_SIM_OPT_MAXMEM
LSBE_SIM_OPT_EXITSTATUS = _lsf.LSBE_SIM_OPT_EXITSTATUS
LSBE_SIM_OPT_SYNTAX = _lsf.LSBE_SIM_OPT_SYNTAX
LSBE_SIM_BSUB = _lsf.LSBE_SIM_BSUB
LSBE_MAX_SLOTS_IN_POOL = _lsf.LSBE_MAX_SLOTS_IN_POOL
LSBE_BAD_GUAR_RESOURCE_NAME = _lsf.LSBE_BAD_GUAR_RESOURCE_NAME
LSBE_GUAR_SLA_USER_NOT_ALLOWED = _lsf.LSBE_GUAR_SLA_USER_NOT_ALLOWED
LSBE_GUAR_SLA_QUEUE_NOT_ALLOWED = _lsf.LSBE_GUAR_SLA_QUEUE_NOT_ALLOWED
LSBE_GUAR_SLA_APP_NOT_ALLOWED = _lsf.LSBE_GUAR_SLA_APP_NOT_ALLOWED
LSBE_GUAR_SLA_PROJECT_NOT_ALLOWED = _lsf.LSBE_GUAR_SLA_PROJECT_NOT_ALLOWED
LSBE_GUAR_SLA_GROUP_NOT_ALLOWED = _lsf.LSBE_GUAR_SLA_GROUP_NOT_ALLOWED
LSBE_GUAR_SLA_GROUP_QUEUE_MISMATCH = _lsf.LSBE_GUAR_SLA_GROUP_QUEUE_MISMATCH
LSBE_SLA_NOT_GUAR_SLA = _lsf.LSBE_SLA_NOT_GUAR_SLA
LSBE_SLA_ACCESS_CONTROL = _lsf.LSBE_SLA_ACCESS_CONTROL
LSBE_GUAR_SLA_JOB_STARTED = _lsf.LSBE_GUAR_SLA_JOB_STARTED
LSBE_GUAR_SLA_INVALID_OP = _lsf.LSBE_GUAR_SLA_INVALID_OP
LSBE_LIVECONF_MBD_RETERR = _lsf.LSBE_LIVECONF_MBD_RETERR
LSBE_LIVECONF_MBD_REJECT = _lsf.LSBE_LIVECONF_MBD_REJECT
LSBE_LIVECONF_MBD_INFO = _lsf.LSBE_LIVECONF_MBD_INFO
LSBE_EXCEED_JOBSPERPACK_LIMITATION = _lsf.LSBE_EXCEED_JOBSPERPACK_LIMITATION
LSBE_PACK_SUBMISSION_DISABLED = _lsf.LSBE_PACK_SUBMISSION_DISABLED
LSBE_GUAR_SLA_LP_NOT_ALLOWED = _lsf.LSBE_GUAR_SLA_LP_NOT_ALLOWED
LSBE_GLB_MIX_MODE = _lsf.LSBE_GLB_MIX_MODE
LSBE_NUM_ERR = _lsf.LSBE_NUM_ERR
PREPARE_FOR_OP = _lsf.PREPARE_FOR_OP
READY_FOR_OP = _lsf.READY_FOR_OP
SUB_JOB_NAME = _lsf.SUB_JOB_NAME
SUB_QUEUE = _lsf.SUB_QUEUE
SUB_HOST = _lsf.SUB_HOST
SUB_IN_FILE = _lsf.SUB_IN_FILE
SUB_OUT_FILE = _lsf.SUB_OUT_FILE
SUB_ERR_FILE = _lsf.SUB_ERR_FILE
SUB_EXCLUSIVE = _lsf.SUB_EXCLUSIVE
SUB_NOTIFY_END = _lsf.SUB_NOTIFY_END
SUB_NOTIFY_BEGIN = _lsf.SUB_NOTIFY_BEGIN
SUB_USER_GROUP = _lsf.SUB_USER_GROUP
SUB_CHKPNT_PERIOD = _lsf.SUB_CHKPNT_PERIOD
SUB_CHKPNT_DIR = _lsf.SUB_CHKPNT_DIR
SUB_CHKPNTABLE = _lsf.SUB_CHKPNTABLE
SUB_RESTART_FORCE = _lsf.SUB_RESTART_FORCE
SUB_RESTART = _lsf.SUB_RESTART
SUB_RERUNNABLE = _lsf.SUB_RERUNNABLE
SUB_WINDOW_SIG = _lsf.SUB_WINDOW_SIG
SUB_HOST_SPEC = _lsf.SUB_HOST_SPEC
SUB_DEPEND_COND = _lsf.SUB_DEPEND_COND
SUB_RES_REQ = _lsf.SUB_RES_REQ
SUB_OTHER_FILES = _lsf.SUB_OTHER_FILES
SUB_PRE_EXEC = _lsf.SUB_PRE_EXEC
SUB_LOGIN_SHELL = _lsf.SUB_LOGIN_SHELL
SUB_MAIL_USER = _lsf.SUB_MAIL_USER
SUB_MODIFY = _lsf.SUB_MODIFY
SUB_MODIFY_ONCE = _lsf.SUB_MODIFY_ONCE
SUB_PROJECT_NAME = _lsf.SUB_PROJECT_NAME
SUB_INTERACTIVE = _lsf.SUB_INTERACTIVE
SUB_PTY = _lsf.SUB_PTY
SUB_PTY_SHELL = _lsf.SUB_PTY_SHELL
SUB_EXCEPT = _lsf.SUB_EXCEPT
SUB_TIME_EVENT = _lsf.SUB_TIME_EVENT
SUB2_HOLD = _lsf.SUB2_HOLD
SUB2_MODIFY_CMD = _lsf.SUB2_MODIFY_CMD
SUB2_BSUB_BLOCK = _lsf.SUB2_BSUB_BLOCK
SUB2_HOST_NT = _lsf.SUB2_HOST_NT
SUB2_HOST_UX = _lsf.SUB2_HOST_UX
SUB2_QUEUE_CHKPNT = _lsf.SUB2_QUEUE_CHKPNT
SUB2_QUEUE_RERUNNABLE = _lsf.SUB2_QUEUE_RERUNNABLE
SUB2_IN_FILE_SPOOL = _lsf.SUB2_IN_FILE_SPOOL
SUB2_JOB_CMD_SPOOL = _lsf.SUB2_JOB_CMD_SPOOL
SUB2_JOB_PRIORITY = _lsf.SUB2_JOB_PRIORITY
SUB2_USE_DEF_PROCLIMIT = _lsf.SUB2_USE_DEF_PROCLIMIT
SUB2_MODIFY_RUN_JOB = _lsf.SUB2_MODIFY_RUN_JOB
SUB2_MODIFY_PEND_JOB = _lsf.SUB2_MODIFY_PEND_JOB
SUB2_WARNING_TIME_PERIOD = _lsf.SUB2_WARNING_TIME_PERIOD
SUB2_WARNING_ACTION = _lsf.SUB2_WARNING_ACTION
SUB2_USE_RSV = _lsf.SUB2_USE_RSV
SUB2_TSJOB = _lsf.SUB2_TSJOB
SUB2_LSF2TP = _lsf.SUB2_LSF2TP
SUB2_JOB_GROUP = _lsf.SUB2_JOB_GROUP
SUB2_SLA = _lsf.SUB2_SLA
SUB2_EXTSCHED = _lsf.SUB2_EXTSCHED
SUB2_LICENSE_PROJECT = _lsf.SUB2_LICENSE_PROJECT
SUB2_OVERWRITE_OUT_FILE = _lsf.SUB2_OVERWRITE_OUT_FILE
SUB2_OVERWRITE_ERR_FILE = _lsf.SUB2_OVERWRITE_ERR_FILE
SUB2_SSM_JOB = _lsf.SUB2_SSM_JOB
SUB2_SYM_JOB = _lsf.SUB2_SYM_JOB
SUB2_SRV_JOB = _lsf.SUB2_SRV_JOB
SUB2_SYM_GRP = _lsf.SUB2_SYM_GRP
SUB2_SYM_JOB_PARENT = _lsf.SUB2_SYM_JOB_PARENT
SUB2_SYM_JOB_REALTIME = _lsf.SUB2_SYM_JOB_REALTIME
SUB2_SYM_JOB_PERSIST_SRV = _lsf.SUB2_SYM_JOB_PERSIST_SRV
SUB2_SSM_JOB_PERSIST = _lsf.SUB2_SSM_JOB_PERSIST
SUB3_APP = _lsf.SUB3_APP
SUB3_APP_RERUNNABLE = _lsf.SUB3_APP_RERUNNABLE
SUB3_ABSOLUTE_PRIORITY = _lsf.SUB3_ABSOLUTE_PRIORITY
SUB3_DEFAULT_JOBGROUP = _lsf.SUB3_DEFAULT_JOBGROUP
SUB3_POST_EXEC = _lsf.SUB3_POST_EXEC
SUB3_USER_SHELL_LIMITS = _lsf.SUB3_USER_SHELL_LIMITS
SUB3_CWD = _lsf.SUB3_CWD
SUB3_RUNTIME_ESTIMATION = _lsf.SUB3_RUNTIME_ESTIMATION
SUB3_NOT_RERUNNABLE = _lsf.SUB3_NOT_RERUNNABLE
SUB3_JOB_REQUEUE = _lsf.SUB3_JOB_REQUEUE
SUB3_INIT_CHKPNT_PERIOD = _lsf.SUB3_INIT_CHKPNT_PERIOD
SUB3_MIG_THRESHOLD = _lsf.SUB3_MIG_THRESHOLD
SUB3_APP_CHKPNT_DIR = _lsf.SUB3_APP_CHKPNT_DIR
SUB3_BSUB_CHK_RESREQ = _lsf.SUB3_BSUB_CHK_RESREQ
SUB3_RUNTIME_ESTIMATION_ACC = _lsf.SUB3_RUNTIME_ESTIMATION_ACC
SUB3_RUNTIME_ESTIMATION_PERC = _lsf.SUB3_RUNTIME_ESTIMATION_PERC
SUB3_INTERACTIVE_SSH = _lsf.SUB3_INTERACTIVE_SSH
SUB3_XJOB_SSH = _lsf.SUB3_XJOB_SSH
SUB3_AUTO_RESIZE = _lsf.SUB3_AUTO_RESIZE
SUB3_RESIZE_NOTIFY_CMD = _lsf.SUB3_RESIZE_NOTIFY_CMD
SUB3_BULK_SUBMIT = _lsf.SUB3_BULK_SUBMIT
SUB3_INTERACTIVE_TTY = _lsf.SUB3_INTERACTIVE_TTY
SUB3_FLOATING_CLIENT = _lsf.SUB3_FLOATING_CLIENT
SUB3_XFJOB = _lsf.SUB3_XFJOB
SUB3_XFJOB_EXCLUSIVE = _lsf.SUB3_XFJOB_EXCLUSIVE
SUB3_JOB_DESCRIPTION = _lsf.SUB3_JOB_DESCRIPTION
SUB3_SIMULATION = _lsf.SUB3_SIMULATION
LOST_AND_FOUND = _lsf.LOST_AND_FOUND
DELETE_NUMBER = _lsf.DELETE_NUMBER
DEL_NUMPRO = _lsf.DEL_NUMPRO
DEFAULT_NUMPRO = _lsf.DEFAULT_NUMPRO
CALADD = _lsf.CALADD
CALMOD = _lsf.CALMOD
CALDEL = _lsf.CALDEL
CALUNDEL = _lsf.CALUNDEL
CALOCCS = _lsf.CALOCCS
EVEADD = _lsf.EVEADD
EVEMOD = _lsf.EVEMOD
EVEDEL = _lsf.EVEDEL
class xFile(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, xFile, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, xFile, name)
    __repr__ = _swig_repr
    __swig_setmethods__["subFn"] = _lsf.xFile_subFn_set
    __swig_getmethods__["subFn"] = _lsf.xFile_subFn_get
    if _newclass:subFn = property(_lsf.xFile_subFn_get, _lsf.xFile_subFn_set)
    __swig_setmethods__["execFn"] = _lsf.xFile_execFn_set
    __swig_getmethods__["execFn"] = _lsf.xFile_execFn_get
    if _newclass:execFn = property(_lsf.xFile_execFn_get, _lsf.xFile_execFn_set)
    __swig_setmethods__["options"] = _lsf.xFile_options_set
    __swig_getmethods__["options"] = _lsf.xFile_options_get
    if _newclass:options = property(_lsf.xFile_options_get, _lsf.xFile_options_set)
    def __init__(self, *args): 
        this = _lsf.new_xFile(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _lsf.delete_xFile
    __del__ = lambda self : None;
xFile_swigregister = _lsf.xFile_swigregister
xFile_swigregister(xFile)
XF_OP_SUB2EXEC = _lsf.XF_OP_SUB2EXEC
XF_OP_EXEC2SUB = _lsf.XF_OP_EXEC2SUB
XF_OP_SUB2EXEC_APPEND = _lsf.XF_OP_SUB2EXEC_APPEND
XF_OP_EXEC2SUB_APPEND = _lsf.XF_OP_EXEC2SUB_APPEND
XF_OP_URL_SOURCE = _lsf.XF_OP_URL_SOURCE

NQS_ROUTE = _lsf.NQS_ROUTE
NQS_SIG = _lsf.NQS_SIG
NQS_SERVER = _lsf.NQS_SERVER
JDATA_EXT_TEST = _lsf.JDATA_EXT_TEST
JDATA_EXT_SIMREQ = _lsf.JDATA_EXT_SIMREQ
JDATA_EXT_JOBIDS = _lsf.JDATA_EXT_JOBIDS
JDATA_EXT_PACKJOB_ESUB = _lsf.JDATA_EXT_PACKJOB_ESUB
class submit_ext(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, submit_ext, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, submit_ext, name)
    __repr__ = _swig_repr
    __swig_setmethods__["num"] = _lsf.submit_ext_num_set
    __swig_getmethods__["num"] = _lsf.submit_ext_num_get
    if _newclass:num = property(_lsf.submit_ext_num_get, _lsf.submit_ext_num_set)
    __swig_setmethods__["keys"] = _lsf.submit_ext_keys_set
    __swig_getmethods__["keys"] = _lsf.submit_ext_keys_get
    if _newclass:keys = property(_lsf.submit_ext_keys_get, _lsf.submit_ext_keys_set)
    __swig_setmethods__["values"] = _lsf.submit_ext_values_set
    __swig_getmethods__["values"] = _lsf.submit_ext_values_get
    if _newclass:values = property(_lsf.submit_ext_values_get, _lsf.submit_ext_values_set)
    def __init__(self, *args): 
        this = _lsf.new_submit_ext(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _lsf.delete_submit_ext
    __del__ = lambda self : None;
submit_ext_swigregister = _lsf.submit_ext_swigregister
submit_ext_swigregister(submit_ext)

class submit(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, submit, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, submit, name)
    __repr__ = _swig_repr
    __swig_setmethods__["options"] = _lsf.submit_options_set
    __swig_getmethods__["options"] = _lsf.submit_options_get
    if _newclass:options = property(_lsf.submit_options_get, _lsf.submit_options_set)
    __swig_setmethods__["options2"] = _lsf.submit_options2_set
    __swig_getmethods__["options2"] = _lsf.submit_options2_get
    if _newclass:options2 = property(_lsf.submit_options2_get, _lsf.submit_options2_set)
    __swig_setmethods__["jobName"] = _lsf.submit_jobName_set
    __swig_getmethods__["jobName"] = _lsf.submit_jobName_get
    if _newclass:jobName = property(_lsf.submit_jobName_get, _lsf.submit_jobName_set)
    __swig_setmethods__["queue"] = _lsf.submit_queue_set
    __swig_getmethods__["queue"] = _lsf.submit_queue_get
    if _newclass:queue = property(_lsf.submit_queue_get, _lsf.submit_queue_set)
    __swig_setmethods__["numAskedHosts"] = _lsf.submit_numAskedHosts_set
    __swig_getmethods__["numAskedHosts"] = _lsf.submit_numAskedHosts_get
    if _newclass:numAskedHosts = property(_lsf.submit_numAskedHosts_get, _lsf.submit_numAskedHosts_set)
    __swig_setmethods__["askedHosts"] = _lsf.submit_askedHosts_set
    __swig_getmethods__["askedHosts"] = _lsf.submit_askedHosts_get
    if _newclass:askedHosts = property(_lsf.submit_askedHosts_get, _lsf.submit_askedHosts_set)
    __swig_setmethods__["resReq"] = _lsf.submit_resReq_set
    __swig_getmethods__["resReq"] = _lsf.submit_resReq_get
    if _newclass:resReq = property(_lsf.submit_resReq_get, _lsf.submit_resReq_set)
    __swig_setmethods__["rLimits"] = _lsf.submit_rLimits_set
    __swig_getmethods__["rLimits"] = _lsf.submit_rLimits_get
    if _newclass:rLimits = property(_lsf.submit_rLimits_get, _lsf.submit_rLimits_set)
    __swig_setmethods__["hostSpec"] = _lsf.submit_hostSpec_set
    __swig_getmethods__["hostSpec"] = _lsf.submit_hostSpec_get
    if _newclass:hostSpec = property(_lsf.submit_hostSpec_get, _lsf.submit_hostSpec_set)
    __swig_setmethods__["numProcessors"] = _lsf.submit_numProcessors_set
    __swig_getmethods__["numProcessors"] = _lsf.submit_numProcessors_get
    if _newclass:numProcessors = property(_lsf.submit_numProcessors_get, _lsf.submit_numProcessors_set)
    __swig_setmethods__["dependCond"] = _lsf.submit_dependCond_set
    __swig_getmethods__["dependCond"] = _lsf.submit_dependCond_get
    if _newclass:dependCond = property(_lsf.submit_dependCond_get, _lsf.submit_dependCond_set)
    __swig_setmethods__["timeEvent"] = _lsf.submit_timeEvent_set
    __swig_getmethods__["timeEvent"] = _lsf.submit_timeEvent_get
    if _newclass:timeEvent = property(_lsf.submit_timeEvent_get, _lsf.submit_timeEvent_set)
    __swig_setmethods__["beginTime"] = _lsf.submit_beginTime_set
    __swig_getmethods__["beginTime"] = _lsf.submit_beginTime_get
    if _newclass:beginTime = property(_lsf.submit_beginTime_get, _lsf.submit_beginTime_set)
    __swig_setmethods__["termTime"] = _lsf.submit_termTime_set
    __swig_getmethods__["termTime"] = _lsf.submit_termTime_get
    if _newclass:termTime = property(_lsf.submit_termTime_get, _lsf.submit_termTime_set)
    __swig_setmethods__["sigValue"] = _lsf.submit_sigValue_set
    __swig_getmethods__["sigValue"] = _lsf.submit_sigValue_get
    if _newclass:sigValue = property(_lsf.submit_sigValue_get, _lsf.submit_sigValue_set)
    __swig_setmethods__["inFile"] = _lsf.submit_inFile_set
    __swig_getmethods__["inFile"] = _lsf.submit_inFile_get
    if _newclass:inFile = property(_lsf.submit_inFile_get, _lsf.submit_inFile_set)
    __swig_setmethods__["outFile"] = _lsf.submit_outFile_set
    __swig_getmethods__["outFile"] = _lsf.submit_outFile_get
    if _newclass:outFile = property(_lsf.submit_outFile_get, _lsf.submit_outFile_set)
    __swig_setmethods__["errFile"] = _lsf.submit_errFile_set
    __swig_getmethods__["errFile"] = _lsf.submit_errFile_get
    if _newclass:errFile = property(_lsf.submit_errFile_get, _lsf.submit_errFile_set)
    __swig_setmethods__["command"] = _lsf.submit_command_set
    __swig_getmethods__["command"] = _lsf.submit_command_get
    if _newclass:command = property(_lsf.submit_command_get, _lsf.submit_command_set)
    __swig_setmethods__["newCommand"] = _lsf.submit_newCommand_set
    __swig_getmethods__["newCommand"] = _lsf.submit_newCommand_get
    if _newclass:newCommand = property(_lsf.submit_newCommand_get, _lsf.submit_newCommand_set)
    __swig_setmethods__["chkpntPeriod"] = _lsf.submit_chkpntPeriod_set
    __swig_getmethods__["chkpntPeriod"] = _lsf.submit_chkpntPeriod_get
    if _newclass:chkpntPeriod = property(_lsf.submit_chkpntPeriod_get, _lsf.submit_chkpntPeriod_set)
    __swig_setmethods__["chkpntDir"] = _lsf.submit_chkpntDir_set
    __swig_getmethods__["chkpntDir"] = _lsf.submit_chkpntDir_get
    if _newclass:chkpntDir = property(_lsf.submit_chkpntDir_get, _lsf.submit_chkpntDir_set)
    __swig_setmethods__["nxf"] = _lsf.submit_nxf_set
    __swig_getmethods__["nxf"] = _lsf.submit_nxf_get
    if _newclass:nxf = property(_lsf.submit_nxf_get, _lsf.submit_nxf_set)
    __swig_setmethods__["xf"] = _lsf.submit_xf_set
    __swig_getmethods__["xf"] = _lsf.submit_xf_get
    if _newclass:xf = property(_lsf.submit_xf_get, _lsf.submit_xf_set)
    __swig_setmethods__["preExecCmd"] = _lsf.submit_preExecCmd_set
    __swig_getmethods__["preExecCmd"] = _lsf.submit_preExecCmd_get
    if _newclass:preExecCmd = property(_lsf.submit_preExecCmd_get, _lsf.submit_preExecCmd_set)
    __swig_setmethods__["mailUser"] = _lsf.submit_mailUser_set
    __swig_getmethods__["mailUser"] = _lsf.submit_mailUser_get
    if _newclass:mailUser = property(_lsf.submit_mailUser_get, _lsf.submit_mailUser_set)
    __swig_setmethods__["delOptions"] = _lsf.submit_delOptions_set
    __swig_getmethods__["delOptions"] = _lsf.submit_delOptions_get
    if _newclass:delOptions = property(_lsf.submit_delOptions_get, _lsf.submit_delOptions_set)
    __swig_setmethods__["delOptions2"] = _lsf.submit_delOptions2_set
    __swig_getmethods__["delOptions2"] = _lsf.submit_delOptions2_get
    if _newclass:delOptions2 = property(_lsf.submit_delOptions2_get, _lsf.submit_delOptions2_set)
    __swig_setmethods__["projectName"] = _lsf.submit_projectName_set
    __swig_getmethods__["projectName"] = _lsf.submit_projectName_get
    if _newclass:projectName = property(_lsf.submit_projectName_get, _lsf.submit_projectName_set)
    __swig_setmethods__["maxNumProcessors"] = _lsf.submit_maxNumProcessors_set
    __swig_getmethods__["maxNumProcessors"] = _lsf.submit_maxNumProcessors_get
    if _newclass:maxNumProcessors = property(_lsf.submit_maxNumProcessors_get, _lsf.submit_maxNumProcessors_set)
    __swig_setmethods__["loginShell"] = _lsf.submit_loginShell_set
    __swig_getmethods__["loginShell"] = _lsf.submit_loginShell_get
    if _newclass:loginShell = property(_lsf.submit_loginShell_get, _lsf.submit_loginShell_set)
    __swig_setmethods__["userGroup"] = _lsf.submit_userGroup_set
    __swig_getmethods__["userGroup"] = _lsf.submit_userGroup_get
    if _newclass:userGroup = property(_lsf.submit_userGroup_get, _lsf.submit_userGroup_set)
    __swig_setmethods__["exceptList"] = _lsf.submit_exceptList_set
    __swig_getmethods__["exceptList"] = _lsf.submit_exceptList_get
    if _newclass:exceptList = property(_lsf.submit_exceptList_get, _lsf.submit_exceptList_set)
    __swig_setmethods__["userPriority"] = _lsf.submit_userPriority_set
    __swig_getmethods__["userPriority"] = _lsf.submit_userPriority_get
    if _newclass:userPriority = property(_lsf.submit_userPriority_get, _lsf.submit_userPriority_set)
    __swig_setmethods__["rsvId"] = _lsf.submit_rsvId_set
    __swig_getmethods__["rsvId"] = _lsf.submit_rsvId_get
    if _newclass:rsvId = property(_lsf.submit_rsvId_get, _lsf.submit_rsvId_set)
    __swig_setmethods__["jobGroup"] = _lsf.submit_jobGroup_set
    __swig_getmethods__["jobGroup"] = _lsf.submit_jobGroup_get
    if _newclass:jobGroup = property(_lsf.submit_jobGroup_get, _lsf.submit_jobGroup_set)
    __swig_setmethods__["sla"] = _lsf.submit_sla_set
    __swig_getmethods__["sla"] = _lsf.submit_sla_get
    if _newclass:sla = property(_lsf.submit_sla_get, _lsf.submit_sla_set)
    __swig_setmethods__["extsched"] = _lsf.submit_extsched_set
    __swig_getmethods__["extsched"] = _lsf.submit_extsched_get
    if _newclass:extsched = property(_lsf.submit_extsched_get, _lsf.submit_extsched_set)
    __swig_setmethods__["warningTimePeriod"] = _lsf.submit_warningTimePeriod_set
    __swig_getmethods__["warningTimePeriod"] = _lsf.submit_warningTimePeriod_get
    if _newclass:warningTimePeriod = property(_lsf.submit_warningTimePeriod_get, _lsf.submit_warningTimePeriod_set)
    __swig_setmethods__["warningAction"] = _lsf.submit_warningAction_set
    __swig_getmethods__["warningAction"] = _lsf.submit_warningAction_get
    if _newclass:warningAction = property(_lsf.submit_warningAction_get, _lsf.submit_warningAction_set)
    __swig_setmethods__["licenseProject"] = _lsf.submit_licenseProject_set
    __swig_getmethods__["licenseProject"] = _lsf.submit_licenseProject_get
    if _newclass:licenseProject = property(_lsf.submit_licenseProject_get, _lsf.submit_licenseProject_set)
    __swig_setmethods__["options3"] = _lsf.submit_options3_set
    __swig_getmethods__["options3"] = _lsf.submit_options3_get
    if _newclass:options3 = property(_lsf.submit_options3_get, _lsf.submit_options3_set)
    __swig_setmethods__["delOptions3"] = _lsf.submit_delOptions3_set
    __swig_getmethods__["delOptions3"] = _lsf.submit_delOptions3_get
    if _newclass:delOptions3 = property(_lsf.submit_delOptions3_get, _lsf.submit_delOptions3_set)
    __swig_setmethods__["app"] = _lsf.submit_app_set
    __swig_getmethods__["app"] = _lsf.submit_app_get
    if _newclass:app = property(_lsf.submit_app_get, _lsf.submit_app_set)
    __swig_setmethods__["jsdlFlag"] = _lsf.submit_jsdlFlag_set
    __swig_getmethods__["jsdlFlag"] = _lsf.submit_jsdlFlag_get
    if _newclass:jsdlFlag = property(_lsf.submit_jsdlFlag_get, _lsf.submit_jsdlFlag_set)
    __swig_setmethods__["jsdlDoc"] = _lsf.submit_jsdlDoc_set
    __swig_getmethods__["jsdlDoc"] = _lsf.submit_jsdlDoc_get
    if _newclass:jsdlDoc = property(_lsf.submit_jsdlDoc_get, _lsf.submit_jsdlDoc_set)
    __swig_setmethods__["correlator"] = _lsf.submit_correlator_set
    __swig_getmethods__["correlator"] = _lsf.submit_correlator_get
    if _newclass:correlator = property(_lsf.submit_correlator_get, _lsf.submit_correlator_set)
    __swig_setmethods__["apsString"] = _lsf.submit_apsString_set
    __swig_getmethods__["apsString"] = _lsf.submit_apsString_get
    if _newclass:apsString = property(_lsf.submit_apsString_get, _lsf.submit_apsString_set)
    __swig_setmethods__["postExecCmd"] = _lsf.submit_postExecCmd_set
    __swig_getmethods__["postExecCmd"] = _lsf.submit_postExecCmd_get
    if _newclass:postExecCmd = property(_lsf.submit_postExecCmd_get, _lsf.submit_postExecCmd_set)
    __swig_setmethods__["cwd"] = _lsf.submit_cwd_set
    __swig_getmethods__["cwd"] = _lsf.submit_cwd_get
    if _newclass:cwd = property(_lsf.submit_cwd_get, _lsf.submit_cwd_set)
    __swig_setmethods__["runtimeEstimation"] = _lsf.submit_runtimeEstimation_set
    __swig_getmethods__["runtimeEstimation"] = _lsf.submit_runtimeEstimation_get
    if _newclass:runtimeEstimation = property(_lsf.submit_runtimeEstimation_get, _lsf.submit_runtimeEstimation_set)
    __swig_setmethods__["requeueEValues"] = _lsf.submit_requeueEValues_set
    __swig_getmethods__["requeueEValues"] = _lsf.submit_requeueEValues_get
    if _newclass:requeueEValues = property(_lsf.submit_requeueEValues_get, _lsf.submit_requeueEValues_set)
    __swig_setmethods__["initChkpntPeriod"] = _lsf.submit_initChkpntPeriod_set
    __swig_getmethods__["initChkpntPeriod"] = _lsf.submit_initChkpntPeriod_get
    if _newclass:initChkpntPeriod = property(_lsf.submit_initChkpntPeriod_get, _lsf.submit_initChkpntPeriod_set)
    __swig_setmethods__["migThreshold"] = _lsf.submit_migThreshold_set
    __swig_getmethods__["migThreshold"] = _lsf.submit_migThreshold_get
    if _newclass:migThreshold = property(_lsf.submit_migThreshold_get, _lsf.submit_migThreshold_set)
    __swig_setmethods__["notifyCmd"] = _lsf.submit_notifyCmd_set
    __swig_getmethods__["notifyCmd"] = _lsf.submit_notifyCmd_get
    if _newclass:notifyCmd = property(_lsf.submit_notifyCmd_get, _lsf.submit_notifyCmd_set)
    __swig_setmethods__["jobDescription"] = _lsf.submit_jobDescription_set
    __swig_getmethods__["jobDescription"] = _lsf.submit_jobDescription_get
    if _newclass:jobDescription = property(_lsf.submit_jobDescription_get, _lsf.submit_jobDescription_set)
    __swig_setmethods__["submitExt"] = _lsf.submit_submitExt_set
    __swig_getmethods__["submitExt"] = _lsf.submit_submitExt_get
    if _newclass:submitExt = property(_lsf.submit_submitExt_get, _lsf.submit_submitExt_set)
    def __init__(self, *args): 
        this = _lsf.new_submit(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _lsf.delete_submit
    __del__ = lambda self : None;
submit_swigregister = _lsf.submit_swigregister
submit_swigregister(submit)

class submitReply(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, submitReply, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, submitReply, name)
    __repr__ = _swig_repr
    __swig_setmethods__["queue"] = _lsf.submitReply_queue_set
    __swig_getmethods__["queue"] = _lsf.submitReply_queue_get
    if _newclass:queue = property(_lsf.submitReply_queue_get, _lsf.submitReply_queue_set)
    __swig_setmethods__["badJobId"] = _lsf.submitReply_badJobId_set
    __swig_getmethods__["badJobId"] = _lsf.submitReply_badJobId_get
    if _newclass:badJobId = property(_lsf.submitReply_badJobId_get, _lsf.submitReply_badJobId_set)
    __swig_setmethods__["badJobName"] = _lsf.submitReply_badJobName_set
    __swig_getmethods__["badJobName"] = _lsf.submitReply_badJobName_get
    if _newclass:badJobName = property(_lsf.submitReply_badJobName_get, _lsf.submitReply_badJobName_set)
    __swig_setmethods__["badReqIndx"] = _lsf.submitReply_badReqIndx_set
    __swig_getmethods__["badReqIndx"] = _lsf.submitReply_badReqIndx_get
    if _newclass:badReqIndx = property(_lsf.submitReply_badReqIndx_get, _lsf.submitReply_badReqIndx_set)
    def __init__(self, *args): 
        this = _lsf.new_submitReply(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _lsf.delete_submitReply
    __del__ = lambda self : None;
submitReply_swigregister = _lsf.submitReply_swigregister
submitReply_swigregister(submitReply)

class packSubmitReply(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, packSubmitReply, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, packSubmitReply, name)
    __repr__ = _swig_repr
    __swig_setmethods__["num"] = _lsf.packSubmitReply_num_set
    __swig_getmethods__["num"] = _lsf.packSubmitReply_num_get
    if _newclass:num = property(_lsf.packSubmitReply_num_get, _lsf.packSubmitReply_num_set)
    __swig_setmethods__["lserrno"] = _lsf.packSubmitReply_lserrno_set
    __swig_getmethods__["lserrno"] = _lsf.packSubmitReply_lserrno_get
    if _newclass:lserrno = property(_lsf.packSubmitReply_lserrno_get, _lsf.packSubmitReply_lserrno_set)
    __swig_setmethods__["submitReplies"] = _lsf.packSubmitReply_submitReplies_set
    __swig_getmethods__["submitReplies"] = _lsf.packSubmitReply_submitReplies_get
    if _newclass:submitReplies = property(_lsf.packSubmitReply_submitReplies_get, _lsf.packSubmitReply_submitReplies_set)
    def __init__(self, *args): 
        this = _lsf.new_packSubmitReply(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _lsf.delete_packSubmitReply
    __del__ = lambda self : None;
packSubmitReply_swigregister = _lsf.packSubmitReply_swigregister
packSubmitReply_swigregister(packSubmitReply)

class packSubmit(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, packSubmit, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, packSubmit, name)
    __repr__ = _swig_repr
    __swig_setmethods__["num"] = _lsf.packSubmit_num_set
    __swig_getmethods__["num"] = _lsf.packSubmit_num_get
    if _newclass:num = property(_lsf.packSubmit_num_get, _lsf.packSubmit_num_set)
    __swig_setmethods__["reqs"] = _lsf.packSubmit_reqs_set
    __swig_getmethods__["reqs"] = _lsf.packSubmit_reqs_get
    if _newclass:reqs = property(_lsf.packSubmit_reqs_get, _lsf.packSubmit_reqs_set)
    def __init__(self, *args): 
        this = _lsf.new_packSubmit(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _lsf.delete_packSubmit
    __del__ = lambda self : None;
packSubmit_swigregister = _lsf.packSubmit_swigregister
packSubmit_swigregister(packSubmit)

class submig(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, submig, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, submig, name)
    __repr__ = _swig_repr
    __swig_setmethods__["jobId"] = _lsf.submig_jobId_set
    __swig_getmethods__["jobId"] = _lsf.submig_jobId_get
    if _newclass:jobId = property(_lsf.submig_jobId_get, _lsf.submig_jobId_set)
    __swig_setmethods__["options"] = _lsf.submig_options_set
    __swig_getmethods__["options"] = _lsf.submig_options_get
    if _newclass:options = property(_lsf.submig_options_get, _lsf.submig_options_set)
    __swig_setmethods__["numAskedHosts"] = _lsf.submig_numAskedHosts_set
    __swig_getmethods__["numAskedHosts"] = _lsf.submig_numAskedHosts_get
    if _newclass:numAskedHosts = property(_lsf.submig_numAskedHosts_get, _lsf.submig_numAskedHosts_set)
    __swig_setmethods__["askedHosts"] = _lsf.submig_askedHosts_set
    __swig_getmethods__["askedHosts"] = _lsf.submig_askedHosts_get
    if _newclass:askedHosts = property(_lsf.submig_askedHosts_get, _lsf.submig_askedHosts_set)
    def __init__(self, *args): 
        this = _lsf.new_submig(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _lsf.delete_submig
    __del__ = lambda self : None;
submig_swigregister = _lsf.submig_swigregister
submig_swigregister(submig)

class jgrpAdd(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, jgrpAdd, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, jgrpAdd, name)
    __repr__ = _swig_repr
    __swig_setmethods__["groupSpec"] = _lsf.jgrpAdd_groupSpec_set
    __swig_getmethods__["groupSpec"] = _lsf.jgrpAdd_groupSpec_get
    if _newclass:groupSpec = property(_lsf.jgrpAdd_groupSpec_get, _lsf.jgrpAdd_groupSpec_set)
    __swig_setmethods__["timeEvent"] = _lsf.jgrpAdd_timeEvent_set
    __swig_getmethods__["timeEvent"] = _lsf.jgrpAdd_timeEvent_get
    if _newclass:timeEvent = property(_lsf.jgrpAdd_timeEvent_get, _lsf.jgrpAdd_timeEvent_set)
    __swig_setmethods__["depCond"] = _lsf.jgrpAdd_depCond_set
    __swig_getmethods__["depCond"] = _lsf.jgrpAdd_depCond_get
    if _newclass:depCond = property(_lsf.jgrpAdd_depCond_get, _lsf.jgrpAdd_depCond_set)
    __swig_setmethods__["sla"] = _lsf.jgrpAdd_sla_set
    __swig_getmethods__["sla"] = _lsf.jgrpAdd_sla_get
    if _newclass:sla = property(_lsf.jgrpAdd_sla_get, _lsf.jgrpAdd_sla_set)
    __swig_setmethods__["maxJLimit"] = _lsf.jgrpAdd_maxJLimit_set
    __swig_getmethods__["maxJLimit"] = _lsf.jgrpAdd_maxJLimit_get
    if _newclass:maxJLimit = property(_lsf.jgrpAdd_maxJLimit_get, _lsf.jgrpAdd_maxJLimit_set)
    def __init__(self, *args): 
        this = _lsf.new_jgrpAdd(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _lsf.delete_jgrpAdd
    __del__ = lambda self : None;
jgrpAdd_swigregister = _lsf.jgrpAdd_swigregister
jgrpAdd_swigregister(jgrpAdd)

class jgrpMod(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, jgrpMod, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, jgrpMod, name)
    __repr__ = _swig_repr
    __swig_setmethods__["destSpec"] = _lsf.jgrpMod_destSpec_set
    __swig_getmethods__["destSpec"] = _lsf.jgrpMod_destSpec_get
    if _newclass:destSpec = property(_lsf.jgrpMod_destSpec_get, _lsf.jgrpMod_destSpec_set)
    __swig_setmethods__["jgrp"] = _lsf.jgrpMod_jgrp_set
    __swig_getmethods__["jgrp"] = _lsf.jgrpMod_jgrp_get
    if _newclass:jgrp = property(_lsf.jgrpMod_jgrp_get, _lsf.jgrpMod_jgrp_set)
    def __init__(self, *args): 
        this = _lsf.new_jgrpMod(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _lsf.delete_jgrpMod
    __del__ = lambda self : None;
jgrpMod_swigregister = _lsf.jgrpMod_swigregister
jgrpMod_swigregister(jgrpMod)

class jgrpReply(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, jgrpReply, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, jgrpReply, name)
    __repr__ = _swig_repr
    __swig_setmethods__["badJgrpName"] = _lsf.jgrpReply_badJgrpName_set
    __swig_getmethods__["badJgrpName"] = _lsf.jgrpReply_badJgrpName_get
    if _newclass:badJgrpName = property(_lsf.jgrpReply_badJgrpName_get, _lsf.jgrpReply_badJgrpName_set)
    __swig_setmethods__["num"] = _lsf.jgrpReply_num_set
    __swig_getmethods__["num"] = _lsf.jgrpReply_num_get
    if _newclass:num = property(_lsf.jgrpReply_num_get, _lsf.jgrpReply_num_set)
    __swig_setmethods__["delJgrpList"] = _lsf.jgrpReply_delJgrpList_set
    __swig_getmethods__["delJgrpList"] = _lsf.jgrpReply_delJgrpList_get
    if _newclass:delJgrpList = property(_lsf.jgrpReply_delJgrpList_get, _lsf.jgrpReply_delJgrpList_set)
    def __init__(self, *args): 
        this = _lsf.new_jgrpReply(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _lsf.delete_jgrpReply
    __del__ = lambda self : None;
jgrpReply_swigregister = _lsf.jgrpReply_swigregister
jgrpReply_swigregister(jgrpReply)

class signalBulkJobs(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, signalBulkJobs, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, signalBulkJobs, name)
    __repr__ = _swig_repr
    __swig_setmethods__["signal"] = _lsf.signalBulkJobs_signal_set
    __swig_getmethods__["signal"] = _lsf.signalBulkJobs_signal_get
    if _newclass:signal = property(_lsf.signalBulkJobs_signal_get, _lsf.signalBulkJobs_signal_set)
    __swig_setmethods__["njobs"] = _lsf.signalBulkJobs_njobs_set
    __swig_getmethods__["njobs"] = _lsf.signalBulkJobs_njobs_get
    if _newclass:njobs = property(_lsf.signalBulkJobs_njobs_get, _lsf.signalBulkJobs_njobs_set)
    __swig_setmethods__["jobs"] = _lsf.signalBulkJobs_jobs_set
    __swig_getmethods__["jobs"] = _lsf.signalBulkJobs_jobs_get
    if _newclass:jobs = property(_lsf.signalBulkJobs_jobs_get, _lsf.signalBulkJobs_jobs_set)
    __swig_setmethods__["flags"] = _lsf.signalBulkJobs_flags_set
    __swig_getmethods__["flags"] = _lsf.signalBulkJobs_flags_get
    if _newclass:flags = property(_lsf.signalBulkJobs_flags_get, _lsf.signalBulkJobs_flags_set)
    def __init__(self, *args): 
        this = _lsf.new_signalBulkJobs(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _lsf.delete_signalBulkJobs
    __del__ = lambda self : None;
signalBulkJobs_swigregister = _lsf.signalBulkJobs_swigregister
signalBulkJobs_swigregister(signalBulkJobs)

class jgrpCtrl(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, jgrpCtrl, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, jgrpCtrl, name)
    __repr__ = _swig_repr
    __swig_setmethods__["groupSpec"] = _lsf.jgrpCtrl_groupSpec_set
    __swig_getmethods__["groupSpec"] = _lsf.jgrpCtrl_groupSpec_get
    if _newclass:groupSpec = property(_lsf.jgrpCtrl_groupSpec_get, _lsf.jgrpCtrl_groupSpec_set)
    __swig_setmethods__["userSpec"] = _lsf.jgrpCtrl_userSpec_set
    __swig_getmethods__["userSpec"] = _lsf.jgrpCtrl_userSpec_get
    if _newclass:userSpec = property(_lsf.jgrpCtrl_userSpec_get, _lsf.jgrpCtrl_userSpec_set)
    __swig_setmethods__["options"] = _lsf.jgrpCtrl_options_set
    __swig_getmethods__["options"] = _lsf.jgrpCtrl_options_get
    if _newclass:options = property(_lsf.jgrpCtrl_options_get, _lsf.jgrpCtrl_options_set)
    __swig_setmethods__["ctrlOp"] = _lsf.jgrpCtrl_ctrlOp_set
    __swig_getmethods__["ctrlOp"] = _lsf.jgrpCtrl_ctrlOp_get
    if _newclass:ctrlOp = property(_lsf.jgrpCtrl_ctrlOp_get, _lsf.jgrpCtrl_ctrlOp_set)
    def __init__(self, *args): 
        this = _lsf.new_jgrpCtrl(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _lsf.delete_jgrpCtrl
    __del__ = lambda self : None;
jgrpCtrl_swigregister = _lsf.jgrpCtrl_swigregister
jgrpCtrl_swigregister(jgrpCtrl)

LSB_CHKPERIOD_NOCHNG = _lsf.LSB_CHKPERIOD_NOCHNG
LSB_CHKPNT_KILL = _lsf.LSB_CHKPNT_KILL
LSB_CHKPNT_FORCE = _lsf.LSB_CHKPNT_FORCE
LSB_CHKPNT_COPY = _lsf.LSB_CHKPNT_COPY
LSB_CHKPNT_MIG = _lsf.LSB_CHKPNT_MIG
LSB_CHKPNT_STOP = _lsf.LSB_CHKPNT_STOP
LSB_KILL_REQUEUE = _lsf.LSB_KILL_REQUEUE
ALL_USERS = _lsf.ALL_USERS
ALL_JOB = _lsf.ALL_JOB
DONE_JOB = _lsf.DONE_JOB
PEND_JOB = _lsf.PEND_JOB
SUSP_JOB = _lsf.SUSP_JOB
CUR_JOB = _lsf.CUR_JOB
LAST_JOB = _lsf.LAST_JOB
RUN_JOB = _lsf.RUN_JOB
JOBID_ONLY = _lsf.JOBID_ONLY
HOST_NAME = _lsf.HOST_NAME
NO_PEND_REASONS = _lsf.NO_PEND_REASONS
JGRP_INFO = _lsf.JGRP_INFO
JGRP_RECURSIVE = _lsf.JGRP_RECURSIVE
JGRP_ARRAY_INFO = _lsf.JGRP_ARRAY_INFO
JOBID_ONLY_ALL = _lsf.JOBID_ONLY_ALL
ZOMBIE_JOB = _lsf.ZOMBIE_JOB
TRANSPARENT_MC = _lsf.TRANSPARENT_MC
EXCEPT_JOB = _lsf.EXCEPT_JOB
MUREX_JOB = _lsf.MUREX_JOB
TO_SYM_UA = _lsf.TO_SYM_UA
SYM_TOP_LEVEL_ONLY = _lsf.SYM_TOP_LEVEL_ONLY
JGRP_NAME = _lsf.JGRP_NAME
COND_HOSTNAME = _lsf.COND_HOSTNAME
FROM_BJOBSCMD = _lsf.FROM_BJOBSCMD
WITH_LOPTION = _lsf.WITH_LOPTION
APS_JOB = _lsf.APS_JOB
UGRP_INFO = _lsf.UGRP_INFO
TIME_LEFT = _lsf.TIME_LEFT
FINISH_TIME = _lsf.FINISH_TIME
COM_PERCENTAGE = _lsf.COM_PERCENTAGE
SSCHED_JOB = _lsf.SSCHED_JOB
KILL_JGRP_RECURSIVE = _lsf.KILL_JGRP_RECURSIVE
JGRP_NODE_JOB = _lsf.JGRP_NODE_JOB
JGRP_NODE_GROUP = _lsf.JGRP_NODE_GROUP
JGRP_NODE_ARRAY = _lsf.JGRP_NODE_ARRAY
JGRP_NODE_SLA = _lsf.JGRP_NODE_SLA
LSB_MAX_ARRAY_JOBID = _lsf.LSB_MAX_ARRAY_JOBID
LSB_MAX_ARRAY_IDX = _lsf.LSB_MAX_ARRAY_IDX
LSB_MAX_SEDJOB_RUNID = _lsf.LSB_MAX_SEDJOB_RUNID
JGRP_INACTIVE = _lsf.JGRP_INACTIVE
JGRP_ACTIVE = _lsf.JGRP_ACTIVE
JGRP_HOLD = _lsf.JGRP_HOLD
JGRP_UNDEFINED = _lsf.JGRP_UNDEFINED
JGRP_RELEASE = _lsf.JGRP_RELEASE
JGRP_DEL = _lsf.JGRP_DEL
JGRP_COUNT_NJOBS = _lsf.JGRP_COUNT_NJOBS
JGRP_COUNT_PEND = _lsf.JGRP_COUNT_PEND
JGRP_COUNT_NPSUSP = _lsf.JGRP_COUNT_NPSUSP
JGRP_COUNT_NRUN = _lsf.JGRP_COUNT_NRUN
JGRP_COUNT_NSSUSP = _lsf.JGRP_COUNT_NSSUSP
JGRP_COUNT_NUSUSP = _lsf.JGRP_COUNT_NUSUSP
JGRP_COUNT_NEXIT = _lsf.JGRP_COUNT_NEXIT
JGRP_COUNT_NDONE = _lsf.JGRP_COUNT_NDONE
JGRP_COUNT_NJOBS_SLOTS = _lsf.JGRP_COUNT_NJOBS_SLOTS
JGRP_COUNT_PEND_SLOTS = _lsf.JGRP_COUNT_PEND_SLOTS
JGRP_COUNT_RUN_SLOTS = _lsf.JGRP_COUNT_RUN_SLOTS
JGRP_COUNT_SSUSP_SLOTS = _lsf.JGRP_COUNT_SSUSP_SLOTS
JGRP_COUNT_USUSP_SLOTS = _lsf.JGRP_COUNT_USUSP_SLOTS
JGRP_COUNT_RESV_SLOTS = _lsf.JGRP_COUNT_RESV_SLOTS
JGRP_MOD_LIMIT = _lsf.JGRP_MOD_LIMIT
NUM_JGRP_JOB_COUNTERS = _lsf.NUM_JGRP_JOB_COUNTERS
NUM_JGRP_COUNTERS = _lsf.NUM_JGRP_COUNTERS
JGRP_CREATE_EXP = _lsf.JGRP_CREATE_EXP
JGRP_CREATE_IMP = _lsf.JGRP_CREATE_IMP
class jgrp(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, jgrp, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, jgrp, name)
    __repr__ = _swig_repr
    __swig_setmethods__["name"] = _lsf.jgrp_name_set
    __swig_getmethods__["name"] = _lsf.jgrp_name_get
    if _newclass:name = property(_lsf.jgrp_name_get, _lsf.jgrp_name_set)
    __swig_setmethods__["path"] = _lsf.jgrp_path_set
    __swig_getmethods__["path"] = _lsf.jgrp_path_get
    if _newclass:path = property(_lsf.jgrp_path_get, _lsf.jgrp_path_set)
    __swig_setmethods__["user"] = _lsf.jgrp_user_set
    __swig_getmethods__["user"] = _lsf.jgrp_user_get
    if _newclass:user = property(_lsf.jgrp_user_get, _lsf.jgrp_user_set)
    __swig_setmethods__["sla"] = _lsf.jgrp_sla_set
    __swig_getmethods__["sla"] = _lsf.jgrp_sla_get
    if _newclass:sla = property(_lsf.jgrp_sla_get, _lsf.jgrp_sla_set)
    __swig_setmethods__["counters"] = _lsf.jgrp_counters_set
    __swig_getmethods__["counters"] = _lsf.jgrp_counters_get
    if _newclass:counters = property(_lsf.jgrp_counters_get, _lsf.jgrp_counters_set)
    __swig_setmethods__["maxJLimit"] = _lsf.jgrp_maxJLimit_set
    __swig_getmethods__["maxJLimit"] = _lsf.jgrp_maxJLimit_get
    if _newclass:maxJLimit = property(_lsf.jgrp_maxJLimit_get, _lsf.jgrp_maxJLimit_set)
    def __init__(self, *args): 
        this = _lsf.new_jgrp(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _lsf.delete_jgrp
    __del__ = lambda self : None;
jgrp_swigregister = _lsf.jgrp_swigregister
jgrp_swigregister(jgrp)

class jobAttrInfoEnt(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, jobAttrInfoEnt, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, jobAttrInfoEnt, name)
    __repr__ = _swig_repr
    __swig_setmethods__["jobId"] = _lsf.jobAttrInfoEnt_jobId_set
    __swig_getmethods__["jobId"] = _lsf.jobAttrInfoEnt_jobId_get
    if _newclass:jobId = property(_lsf.jobAttrInfoEnt_jobId_get, _lsf.jobAttrInfoEnt_jobId_set)
    __swig_setmethods__["port"] = _lsf.jobAttrInfoEnt_port_set
    __swig_getmethods__["port"] = _lsf.jobAttrInfoEnt_port_get
    if _newclass:port = property(_lsf.jobAttrInfoEnt_port_get, _lsf.jobAttrInfoEnt_port_set)
    __swig_setmethods__["hostname"] = _lsf.jobAttrInfoEnt_hostname_set
    __swig_getmethods__["hostname"] = _lsf.jobAttrInfoEnt_hostname_get
    if _newclass:hostname = property(_lsf.jobAttrInfoEnt_hostname_get, _lsf.jobAttrInfoEnt_hostname_set)
    def __init__(self, *args): 
        this = _lsf.new_jobAttrInfoEnt(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _lsf.delete_jobAttrInfoEnt
    __del__ = lambda self : None;
jobAttrInfoEnt_swigregister = _lsf.jobAttrInfoEnt_swigregister
jobAttrInfoEnt_swigregister(jobAttrInfoEnt)

class jobAttrSetLog(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, jobAttrSetLog, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, jobAttrSetLog, name)
    __repr__ = _swig_repr
    __swig_setmethods__["jobId"] = _lsf.jobAttrSetLog_jobId_set
    __swig_getmethods__["jobId"] = _lsf.jobAttrSetLog_jobId_get
    if _newclass:jobId = property(_lsf.jobAttrSetLog_jobId_get, _lsf.jobAttrSetLog_jobId_set)
    __swig_setmethods__["idx"] = _lsf.jobAttrSetLog_idx_set
    __swig_getmethods__["idx"] = _lsf.jobAttrSetLog_idx_get
    if _newclass:idx = property(_lsf.jobAttrSetLog_idx_get, _lsf.jobAttrSetLog_idx_set)
    __swig_setmethods__["uid"] = _lsf.jobAttrSetLog_uid_set
    __swig_getmethods__["uid"] = _lsf.jobAttrSetLog_uid_get
    if _newclass:uid = property(_lsf.jobAttrSetLog_uid_get, _lsf.jobAttrSetLog_uid_set)
    __swig_setmethods__["port"] = _lsf.jobAttrSetLog_port_set
    __swig_getmethods__["port"] = _lsf.jobAttrSetLog_port_get
    if _newclass:port = property(_lsf.jobAttrSetLog_port_get, _lsf.jobAttrSetLog_port_set)
    __swig_setmethods__["hostname"] = _lsf.jobAttrSetLog_hostname_set
    __swig_getmethods__["hostname"] = _lsf.jobAttrSetLog_hostname_get
    if _newclass:hostname = property(_lsf.jobAttrSetLog_hostname_get, _lsf.jobAttrSetLog_hostname_set)
    def __init__(self, *args): 
        this = _lsf.new_jobAttrSetLog(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _lsf.delete_jobAttrSetLog
    __del__ = lambda self : None;
jobAttrSetLog_swigregister = _lsf.jobAttrSetLog_swigregister
jobAttrSetLog_swigregister(jobAttrSetLog)

class jobInfoHead(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, jobInfoHead, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, jobInfoHead, name)
    __repr__ = _swig_repr
    __swig_setmethods__["numJobs"] = _lsf.jobInfoHead_numJobs_set
    __swig_getmethods__["numJobs"] = _lsf.jobInfoHead_numJobs_get
    if _newclass:numJobs = property(_lsf.jobInfoHead_numJobs_get, _lsf.jobInfoHead_numJobs_set)
    __swig_setmethods__["jobIds"] = _lsf.jobInfoHead_jobIds_set
    __swig_getmethods__["jobIds"] = _lsf.jobInfoHead_jobIds_get
    if _newclass:jobIds = property(_lsf.jobInfoHead_jobIds_get, _lsf.jobInfoHead_jobIds_set)
    __swig_setmethods__["numHosts"] = _lsf.jobInfoHead_numHosts_set
    __swig_getmethods__["numHosts"] = _lsf.jobInfoHead_numHosts_get
    if _newclass:numHosts = property(_lsf.jobInfoHead_numHosts_get, _lsf.jobInfoHead_numHosts_set)
    __swig_setmethods__["hostNames"] = _lsf.jobInfoHead_hostNames_set
    __swig_getmethods__["hostNames"] = _lsf.jobInfoHead_hostNames_get
    if _newclass:hostNames = property(_lsf.jobInfoHead_hostNames_get, _lsf.jobInfoHead_hostNames_set)
    __swig_setmethods__["numClusters"] = _lsf.jobInfoHead_numClusters_set
    __swig_getmethods__["numClusters"] = _lsf.jobInfoHead_numClusters_get
    if _newclass:numClusters = property(_lsf.jobInfoHead_numClusters_get, _lsf.jobInfoHead_numClusters_set)
    __swig_setmethods__["clusterNames"] = _lsf.jobInfoHead_clusterNames_set
    __swig_getmethods__["clusterNames"] = _lsf.jobInfoHead_clusterNames_get
    if _newclass:clusterNames = property(_lsf.jobInfoHead_clusterNames_get, _lsf.jobInfoHead_clusterNames_set)
    __swig_setmethods__["numRemoteHosts"] = _lsf.jobInfoHead_numRemoteHosts_set
    __swig_getmethods__["numRemoteHosts"] = _lsf.jobInfoHead_numRemoteHosts_get
    if _newclass:numRemoteHosts = property(_lsf.jobInfoHead_numRemoteHosts_get, _lsf.jobInfoHead_numRemoteHosts_set)
    __swig_setmethods__["remoteHosts"] = _lsf.jobInfoHead_remoteHosts_set
    __swig_getmethods__["remoteHosts"] = _lsf.jobInfoHead_remoteHosts_get
    if _newclass:remoteHosts = property(_lsf.jobInfoHead_remoteHosts_get, _lsf.jobInfoHead_remoteHosts_set)
    def __init__(self, *args): 
        this = _lsf.new_jobInfoHead(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _lsf.delete_jobInfoHead
    __del__ = lambda self : None;
jobInfoHead_swigregister = _lsf.jobInfoHead_swigregister
jobInfoHead_swigregister(jobInfoHead)

class jobInfoHeadExt(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, jobInfoHeadExt, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, jobInfoHeadExt, name)
    __repr__ = _swig_repr
    __swig_setmethods__["jobInfoHead"] = _lsf.jobInfoHeadExt_jobInfoHead_set
    __swig_getmethods__["jobInfoHead"] = _lsf.jobInfoHeadExt_jobInfoHead_get
    if _newclass:jobInfoHead = property(_lsf.jobInfoHeadExt_jobInfoHead_get, _lsf.jobInfoHeadExt_jobInfoHead_set)
    __swig_setmethods__["groupInfo"] = _lsf.jobInfoHeadExt_groupInfo_set
    __swig_getmethods__["groupInfo"] = _lsf.jobInfoHeadExt_groupInfo_get
    if _newclass:groupInfo = property(_lsf.jobInfoHeadExt_groupInfo_get, _lsf.jobInfoHeadExt_groupInfo_set)
    def __init__(self, *args): 
        this = _lsf.new_jobInfoHeadExt(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _lsf.delete_jobInfoHeadExt
    __del__ = lambda self : None;
jobInfoHeadExt_swigregister = _lsf.jobInfoHeadExt_swigregister
jobInfoHeadExt_swigregister(jobInfoHeadExt)

class reserveItem(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, reserveItem, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, reserveItem, name)
    __repr__ = _swig_repr
    __swig_setmethods__["resName"] = _lsf.reserveItem_resName_set
    __swig_getmethods__["resName"] = _lsf.reserveItem_resName_get
    if _newclass:resName = property(_lsf.reserveItem_resName_get, _lsf.reserveItem_resName_set)
    __swig_setmethods__["nHost"] = _lsf.reserveItem_nHost_set
    __swig_getmethods__["nHost"] = _lsf.reserveItem_nHost_get
    if _newclass:nHost = property(_lsf.reserveItem_nHost_get, _lsf.reserveItem_nHost_set)
    __swig_setmethods__["value"] = _lsf.reserveItem_value_set
    __swig_getmethods__["value"] = _lsf.reserveItem_value_get
    if _newclass:value = property(_lsf.reserveItem_value_get, _lsf.reserveItem_value_set)
    __swig_setmethods__["shared"] = _lsf.reserveItem_shared_set
    __swig_getmethods__["shared"] = _lsf.reserveItem_shared_get
    if _newclass:shared = property(_lsf.reserveItem_shared_get, _lsf.reserveItem_shared_set)
    def __init__(self, *args): 
        this = _lsf.new_reserveItem(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _lsf.delete_reserveItem
    __del__ = lambda self : None;
reserveItem_swigregister = _lsf.reserveItem_swigregister
reserveItem_swigregister(reserveItem)

class jobInfoEnt(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, jobInfoEnt, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, jobInfoEnt, name)
    __repr__ = _swig_repr
    __swig_setmethods__["jobId"] = _lsf.jobInfoEnt_jobId_set
    __swig_getmethods__["jobId"] = _lsf.jobInfoEnt_jobId_get
    if _newclass:jobId = property(_lsf.jobInfoEnt_jobId_get, _lsf.jobInfoEnt_jobId_set)
    __swig_setmethods__["user"] = _lsf.jobInfoEnt_user_set
    __swig_getmethods__["user"] = _lsf.jobInfoEnt_user_get
    if _newclass:user = property(_lsf.jobInfoEnt_user_get, _lsf.jobInfoEnt_user_set)
    __swig_setmethods__["status"] = _lsf.jobInfoEnt_status_set
    __swig_getmethods__["status"] = _lsf.jobInfoEnt_status_get
    if _newclass:status = property(_lsf.jobInfoEnt_status_get, _lsf.jobInfoEnt_status_set)
    __swig_setmethods__["reasonTb"] = _lsf.jobInfoEnt_reasonTb_set
    __swig_getmethods__["reasonTb"] = _lsf.jobInfoEnt_reasonTb_get
    if _newclass:reasonTb = property(_lsf.jobInfoEnt_reasonTb_get, _lsf.jobInfoEnt_reasonTb_set)
    __swig_setmethods__["numReasons"] = _lsf.jobInfoEnt_numReasons_set
    __swig_getmethods__["numReasons"] = _lsf.jobInfoEnt_numReasons_get
    if _newclass:numReasons = property(_lsf.jobInfoEnt_numReasons_get, _lsf.jobInfoEnt_numReasons_set)
    __swig_setmethods__["reasons"] = _lsf.jobInfoEnt_reasons_set
    __swig_getmethods__["reasons"] = _lsf.jobInfoEnt_reasons_get
    if _newclass:reasons = property(_lsf.jobInfoEnt_reasons_get, _lsf.jobInfoEnt_reasons_set)
    __swig_setmethods__["subreasons"] = _lsf.jobInfoEnt_subreasons_set
    __swig_getmethods__["subreasons"] = _lsf.jobInfoEnt_subreasons_get
    if _newclass:subreasons = property(_lsf.jobInfoEnt_subreasons_get, _lsf.jobInfoEnt_subreasons_set)
    __swig_setmethods__["jobPid"] = _lsf.jobInfoEnt_jobPid_set
    __swig_getmethods__["jobPid"] = _lsf.jobInfoEnt_jobPid_get
    if _newclass:jobPid = property(_lsf.jobInfoEnt_jobPid_get, _lsf.jobInfoEnt_jobPid_set)
    __swig_setmethods__["submitTime"] = _lsf.jobInfoEnt_submitTime_set
    __swig_getmethods__["submitTime"] = _lsf.jobInfoEnt_submitTime_get
    if _newclass:submitTime = property(_lsf.jobInfoEnt_submitTime_get, _lsf.jobInfoEnt_submitTime_set)
    __swig_setmethods__["reserveTime"] = _lsf.jobInfoEnt_reserveTime_set
    __swig_getmethods__["reserveTime"] = _lsf.jobInfoEnt_reserveTime_get
    if _newclass:reserveTime = property(_lsf.jobInfoEnt_reserveTime_get, _lsf.jobInfoEnt_reserveTime_set)
    __swig_setmethods__["startTime"] = _lsf.jobInfoEnt_startTime_set
    __swig_getmethods__["startTime"] = _lsf.jobInfoEnt_startTime_get
    if _newclass:startTime = property(_lsf.jobInfoEnt_startTime_get, _lsf.jobInfoEnt_startTime_set)
    __swig_setmethods__["predictedStartTime"] = _lsf.jobInfoEnt_predictedStartTime_set
    __swig_getmethods__["predictedStartTime"] = _lsf.jobInfoEnt_predictedStartTime_get
    if _newclass:predictedStartTime = property(_lsf.jobInfoEnt_predictedStartTime_get, _lsf.jobInfoEnt_predictedStartTime_set)
    __swig_setmethods__["endTime"] = _lsf.jobInfoEnt_endTime_set
    __swig_getmethods__["endTime"] = _lsf.jobInfoEnt_endTime_get
    if _newclass:endTime = property(_lsf.jobInfoEnt_endTime_get, _lsf.jobInfoEnt_endTime_set)
    __swig_setmethods__["lastEvent"] = _lsf.jobInfoEnt_lastEvent_set
    __swig_getmethods__["lastEvent"] = _lsf.jobInfoEnt_lastEvent_get
    if _newclass:lastEvent = property(_lsf.jobInfoEnt_lastEvent_get, _lsf.jobInfoEnt_lastEvent_set)
    __swig_setmethods__["nextEvent"] = _lsf.jobInfoEnt_nextEvent_set
    __swig_getmethods__["nextEvent"] = _lsf.jobInfoEnt_nextEvent_get
    if _newclass:nextEvent = property(_lsf.jobInfoEnt_nextEvent_get, _lsf.jobInfoEnt_nextEvent_set)
    __swig_setmethods__["duration"] = _lsf.jobInfoEnt_duration_set
    __swig_getmethods__["duration"] = _lsf.jobInfoEnt_duration_get
    if _newclass:duration = property(_lsf.jobInfoEnt_duration_get, _lsf.jobInfoEnt_duration_set)
    __swig_setmethods__["cpuTime"] = _lsf.jobInfoEnt_cpuTime_set
    __swig_getmethods__["cpuTime"] = _lsf.jobInfoEnt_cpuTime_get
    if _newclass:cpuTime = property(_lsf.jobInfoEnt_cpuTime_get, _lsf.jobInfoEnt_cpuTime_set)
    __swig_setmethods__["umask"] = _lsf.jobInfoEnt_umask_set
    __swig_getmethods__["umask"] = _lsf.jobInfoEnt_umask_get
    if _newclass:umask = property(_lsf.jobInfoEnt_umask_get, _lsf.jobInfoEnt_umask_set)
    __swig_setmethods__["cwd"] = _lsf.jobInfoEnt_cwd_set
    __swig_getmethods__["cwd"] = _lsf.jobInfoEnt_cwd_get
    if _newclass:cwd = property(_lsf.jobInfoEnt_cwd_get, _lsf.jobInfoEnt_cwd_set)
    __swig_setmethods__["subHomeDir"] = _lsf.jobInfoEnt_subHomeDir_set
    __swig_getmethods__["subHomeDir"] = _lsf.jobInfoEnt_subHomeDir_get
    if _newclass:subHomeDir = property(_lsf.jobInfoEnt_subHomeDir_get, _lsf.jobInfoEnt_subHomeDir_set)
    __swig_setmethods__["fromHost"] = _lsf.jobInfoEnt_fromHost_set
    __swig_getmethods__["fromHost"] = _lsf.jobInfoEnt_fromHost_get
    if _newclass:fromHost = property(_lsf.jobInfoEnt_fromHost_get, _lsf.jobInfoEnt_fromHost_set)
    __swig_setmethods__["exHosts"] = _lsf.jobInfoEnt_exHosts_set
    __swig_getmethods__["exHosts"] = _lsf.jobInfoEnt_exHosts_get
    if _newclass:exHosts = property(_lsf.jobInfoEnt_exHosts_get, _lsf.jobInfoEnt_exHosts_set)
    __swig_setmethods__["numExHosts"] = _lsf.jobInfoEnt_numExHosts_set
    __swig_getmethods__["numExHosts"] = _lsf.jobInfoEnt_numExHosts_get
    if _newclass:numExHosts = property(_lsf.jobInfoEnt_numExHosts_get, _lsf.jobInfoEnt_numExHosts_set)
    __swig_setmethods__["cpuFactor"] = _lsf.jobInfoEnt_cpuFactor_set
    __swig_getmethods__["cpuFactor"] = _lsf.jobInfoEnt_cpuFactor_get
    if _newclass:cpuFactor = property(_lsf.jobInfoEnt_cpuFactor_get, _lsf.jobInfoEnt_cpuFactor_set)
    __swig_setmethods__["nIdx"] = _lsf.jobInfoEnt_nIdx_set
    __swig_getmethods__["nIdx"] = _lsf.jobInfoEnt_nIdx_get
    if _newclass:nIdx = property(_lsf.jobInfoEnt_nIdx_get, _lsf.jobInfoEnt_nIdx_set)
    __swig_setmethods__["loadSched"] = _lsf.jobInfoEnt_loadSched_set
    __swig_getmethods__["loadSched"] = _lsf.jobInfoEnt_loadSched_get
    if _newclass:loadSched = property(_lsf.jobInfoEnt_loadSched_get, _lsf.jobInfoEnt_loadSched_set)
    __swig_setmethods__["loadStop"] = _lsf.jobInfoEnt_loadStop_set
    __swig_getmethods__["loadStop"] = _lsf.jobInfoEnt_loadStop_get
    if _newclass:loadStop = property(_lsf.jobInfoEnt_loadStop_get, _lsf.jobInfoEnt_loadStop_set)
    __swig_setmethods__["submit"] = _lsf.jobInfoEnt_submit_set
    __swig_getmethods__["submit"] = _lsf.jobInfoEnt_submit_get
    if _newclass:submit = property(_lsf.jobInfoEnt_submit_get, _lsf.jobInfoEnt_submit_set)
    __swig_setmethods__["exitStatus"] = _lsf.jobInfoEnt_exitStatus_set
    __swig_getmethods__["exitStatus"] = _lsf.jobInfoEnt_exitStatus_get
    if _newclass:exitStatus = property(_lsf.jobInfoEnt_exitStatus_get, _lsf.jobInfoEnt_exitStatus_set)
    __swig_setmethods__["execUid"] = _lsf.jobInfoEnt_execUid_set
    __swig_getmethods__["execUid"] = _lsf.jobInfoEnt_execUid_get
    if _newclass:execUid = property(_lsf.jobInfoEnt_execUid_get, _lsf.jobInfoEnt_execUid_set)
    __swig_setmethods__["execHome"] = _lsf.jobInfoEnt_execHome_set
    __swig_getmethods__["execHome"] = _lsf.jobInfoEnt_execHome_get
    if _newclass:execHome = property(_lsf.jobInfoEnt_execHome_get, _lsf.jobInfoEnt_execHome_set)
    __swig_setmethods__["execCwd"] = _lsf.jobInfoEnt_execCwd_set
    __swig_getmethods__["execCwd"] = _lsf.jobInfoEnt_execCwd_get
    if _newclass:execCwd = property(_lsf.jobInfoEnt_execCwd_get, _lsf.jobInfoEnt_execCwd_set)
    __swig_setmethods__["execUsername"] = _lsf.jobInfoEnt_execUsername_set
    __swig_getmethods__["execUsername"] = _lsf.jobInfoEnt_execUsername_get
    if _newclass:execUsername = property(_lsf.jobInfoEnt_execUsername_get, _lsf.jobInfoEnt_execUsername_set)
    __swig_setmethods__["jRusageUpdateTime"] = _lsf.jobInfoEnt_jRusageUpdateTime_set
    __swig_getmethods__["jRusageUpdateTime"] = _lsf.jobInfoEnt_jRusageUpdateTime_get
    if _newclass:jRusageUpdateTime = property(_lsf.jobInfoEnt_jRusageUpdateTime_get, _lsf.jobInfoEnt_jRusageUpdateTime_set)
    __swig_setmethods__["runRusage"] = _lsf.jobInfoEnt_runRusage_set
    __swig_getmethods__["runRusage"] = _lsf.jobInfoEnt_runRusage_get
    if _newclass:runRusage = property(_lsf.jobInfoEnt_runRusage_get, _lsf.jobInfoEnt_runRusage_set)
    __swig_setmethods__["jType"] = _lsf.jobInfoEnt_jType_set
    __swig_getmethods__["jType"] = _lsf.jobInfoEnt_jType_get
    if _newclass:jType = property(_lsf.jobInfoEnt_jType_get, _lsf.jobInfoEnt_jType_set)
    __swig_setmethods__["parentGroup"] = _lsf.jobInfoEnt_parentGroup_set
    __swig_getmethods__["parentGroup"] = _lsf.jobInfoEnt_parentGroup_get
    if _newclass:parentGroup = property(_lsf.jobInfoEnt_parentGroup_get, _lsf.jobInfoEnt_parentGroup_set)
    __swig_setmethods__["jName"] = _lsf.jobInfoEnt_jName_set
    __swig_getmethods__["jName"] = _lsf.jobInfoEnt_jName_get
    if _newclass:jName = property(_lsf.jobInfoEnt_jName_get, _lsf.jobInfoEnt_jName_set)
    __swig_setmethods__["counter"] = _lsf.jobInfoEnt_counter_set
    __swig_getmethods__["counter"] = _lsf.jobInfoEnt_counter_get
    if _newclass:counter = property(_lsf.jobInfoEnt_counter_get, _lsf.jobInfoEnt_counter_set)
    __swig_setmethods__["port"] = _lsf.jobInfoEnt_port_set
    __swig_getmethods__["port"] = _lsf.jobInfoEnt_port_get
    if _newclass:port = property(_lsf.jobInfoEnt_port_get, _lsf.jobInfoEnt_port_set)
    __swig_setmethods__["jobPriority"] = _lsf.jobInfoEnt_jobPriority_set
    __swig_getmethods__["jobPriority"] = _lsf.jobInfoEnt_jobPriority_get
    if _newclass:jobPriority = property(_lsf.jobInfoEnt_jobPriority_get, _lsf.jobInfoEnt_jobPriority_set)
    __swig_setmethods__["numExternalMsg"] = _lsf.jobInfoEnt_numExternalMsg_set
    __swig_getmethods__["numExternalMsg"] = _lsf.jobInfoEnt_numExternalMsg_get
    if _newclass:numExternalMsg = property(_lsf.jobInfoEnt_numExternalMsg_get, _lsf.jobInfoEnt_numExternalMsg_set)
    __swig_setmethods__["externalMsg"] = _lsf.jobInfoEnt_externalMsg_set
    __swig_getmethods__["externalMsg"] = _lsf.jobInfoEnt_externalMsg_get
    if _newclass:externalMsg = property(_lsf.jobInfoEnt_externalMsg_get, _lsf.jobInfoEnt_externalMsg_set)
    __swig_setmethods__["clusterId"] = _lsf.jobInfoEnt_clusterId_set
    __swig_getmethods__["clusterId"] = _lsf.jobInfoEnt_clusterId_get
    if _newclass:clusterId = property(_lsf.jobInfoEnt_clusterId_get, _lsf.jobInfoEnt_clusterId_set)
    __swig_setmethods__["detailReason"] = _lsf.jobInfoEnt_detailReason_set
    __swig_getmethods__["detailReason"] = _lsf.jobInfoEnt_detailReason_get
    if _newclass:detailReason = property(_lsf.jobInfoEnt_detailReason_get, _lsf.jobInfoEnt_detailReason_set)
    __swig_setmethods__["idleFactor"] = _lsf.jobInfoEnt_idleFactor_set
    __swig_getmethods__["idleFactor"] = _lsf.jobInfoEnt_idleFactor_get
    if _newclass:idleFactor = property(_lsf.jobInfoEnt_idleFactor_get, _lsf.jobInfoEnt_idleFactor_set)
    __swig_setmethods__["exceptMask"] = _lsf.jobInfoEnt_exceptMask_set
    __swig_getmethods__["exceptMask"] = _lsf.jobInfoEnt_exceptMask_get
    if _newclass:exceptMask = property(_lsf.jobInfoEnt_exceptMask_get, _lsf.jobInfoEnt_exceptMask_set)
    __swig_setmethods__["additionalInfo"] = _lsf.jobInfoEnt_additionalInfo_set
    __swig_getmethods__["additionalInfo"] = _lsf.jobInfoEnt_additionalInfo_get
    if _newclass:additionalInfo = property(_lsf.jobInfoEnt_additionalInfo_get, _lsf.jobInfoEnt_additionalInfo_set)
    __swig_setmethods__["exitInfo"] = _lsf.jobInfoEnt_exitInfo_set
    __swig_getmethods__["exitInfo"] = _lsf.jobInfoEnt_exitInfo_get
    if _newclass:exitInfo = property(_lsf.jobInfoEnt_exitInfo_get, _lsf.jobInfoEnt_exitInfo_set)
    __swig_setmethods__["warningTimePeriod"] = _lsf.jobInfoEnt_warningTimePeriod_set
    __swig_getmethods__["warningTimePeriod"] = _lsf.jobInfoEnt_warningTimePeriod_get
    if _newclass:warningTimePeriod = property(_lsf.jobInfoEnt_warningTimePeriod_get, _lsf.jobInfoEnt_warningTimePeriod_set)
    __swig_setmethods__["warningAction"] = _lsf.jobInfoEnt_warningAction_set
    __swig_getmethods__["warningAction"] = _lsf.jobInfoEnt_warningAction_get
    if _newclass:warningAction = property(_lsf.jobInfoEnt_warningAction_get, _lsf.jobInfoEnt_warningAction_set)
    __swig_setmethods__["chargedSAAP"] = _lsf.jobInfoEnt_chargedSAAP_set
    __swig_getmethods__["chargedSAAP"] = _lsf.jobInfoEnt_chargedSAAP_get
    if _newclass:chargedSAAP = property(_lsf.jobInfoEnt_chargedSAAP_get, _lsf.jobInfoEnt_chargedSAAP_set)
    __swig_setmethods__["execRusage"] = _lsf.jobInfoEnt_execRusage_set
    __swig_getmethods__["execRusage"] = _lsf.jobInfoEnt_execRusage_get
    if _newclass:execRusage = property(_lsf.jobInfoEnt_execRusage_get, _lsf.jobInfoEnt_execRusage_set)
    __swig_setmethods__["rsvInActive"] = _lsf.jobInfoEnt_rsvInActive_set
    __swig_getmethods__["rsvInActive"] = _lsf.jobInfoEnt_rsvInActive_get
    if _newclass:rsvInActive = property(_lsf.jobInfoEnt_rsvInActive_get, _lsf.jobInfoEnt_rsvInActive_set)
    __swig_setmethods__["numLicense"] = _lsf.jobInfoEnt_numLicense_set
    __swig_getmethods__["numLicense"] = _lsf.jobInfoEnt_numLicense_get
    if _newclass:numLicense = property(_lsf.jobInfoEnt_numLicense_get, _lsf.jobInfoEnt_numLicense_set)
    __swig_setmethods__["licenseNames"] = _lsf.jobInfoEnt_licenseNames_set
    __swig_getmethods__["licenseNames"] = _lsf.jobInfoEnt_licenseNames_get
    if _newclass:licenseNames = property(_lsf.jobInfoEnt_licenseNames_get, _lsf.jobInfoEnt_licenseNames_set)
    __swig_setmethods__["aps"] = _lsf.jobInfoEnt_aps_set
    __swig_getmethods__["aps"] = _lsf.jobInfoEnt_aps_get
    if _newclass:aps = property(_lsf.jobInfoEnt_aps_get, _lsf.jobInfoEnt_aps_set)
    __swig_setmethods__["adminAps"] = _lsf.jobInfoEnt_adminAps_set
    __swig_getmethods__["adminAps"] = _lsf.jobInfoEnt_adminAps_get
    if _newclass:adminAps = property(_lsf.jobInfoEnt_adminAps_get, _lsf.jobInfoEnt_adminAps_set)
    __swig_setmethods__["runTime"] = _lsf.jobInfoEnt_runTime_set
    __swig_getmethods__["runTime"] = _lsf.jobInfoEnt_runTime_get
    if _newclass:runTime = property(_lsf.jobInfoEnt_runTime_get, _lsf.jobInfoEnt_runTime_set)
    __swig_setmethods__["reserveCnt"] = _lsf.jobInfoEnt_reserveCnt_set
    __swig_getmethods__["reserveCnt"] = _lsf.jobInfoEnt_reserveCnt_get
    if _newclass:reserveCnt = property(_lsf.jobInfoEnt_reserveCnt_get, _lsf.jobInfoEnt_reserveCnt_set)
    __swig_setmethods__["items"] = _lsf.jobInfoEnt_items_set
    __swig_getmethods__["items"] = _lsf.jobInfoEnt_items_get
    if _newclass:items = property(_lsf.jobInfoEnt_items_get, _lsf.jobInfoEnt_items_set)
    __swig_setmethods__["adminFactorVal"] = _lsf.jobInfoEnt_adminFactorVal_set
    __swig_getmethods__["adminFactorVal"] = _lsf.jobInfoEnt_adminFactorVal_get
    if _newclass:adminFactorVal = property(_lsf.jobInfoEnt_adminFactorVal_get, _lsf.jobInfoEnt_adminFactorVal_set)
    __swig_setmethods__["resizeMin"] = _lsf.jobInfoEnt_resizeMin_set
    __swig_getmethods__["resizeMin"] = _lsf.jobInfoEnt_resizeMin_get
    if _newclass:resizeMin = property(_lsf.jobInfoEnt_resizeMin_get, _lsf.jobInfoEnt_resizeMin_set)
    __swig_setmethods__["resizeMax"] = _lsf.jobInfoEnt_resizeMax_set
    __swig_getmethods__["resizeMax"] = _lsf.jobInfoEnt_resizeMax_get
    if _newclass:resizeMax = property(_lsf.jobInfoEnt_resizeMax_get, _lsf.jobInfoEnt_resizeMax_set)
    __swig_setmethods__["resizeReqTime"] = _lsf.jobInfoEnt_resizeReqTime_set
    __swig_getmethods__["resizeReqTime"] = _lsf.jobInfoEnt_resizeReqTime_get
    if _newclass:resizeReqTime = property(_lsf.jobInfoEnt_resizeReqTime_get, _lsf.jobInfoEnt_resizeReqTime_set)
    __swig_setmethods__["jStartNumExHosts"] = _lsf.jobInfoEnt_jStartNumExHosts_set
    __swig_getmethods__["jStartNumExHosts"] = _lsf.jobInfoEnt_jStartNumExHosts_get
    if _newclass:jStartNumExHosts = property(_lsf.jobInfoEnt_jStartNumExHosts_get, _lsf.jobInfoEnt_jStartNumExHosts_set)
    __swig_setmethods__["jStartExHosts"] = _lsf.jobInfoEnt_jStartExHosts_set
    __swig_getmethods__["jStartExHosts"] = _lsf.jobInfoEnt_jStartExHosts_get
    if _newclass:jStartExHosts = property(_lsf.jobInfoEnt_jStartExHosts_get, _lsf.jobInfoEnt_jStartExHosts_set)
    __swig_setmethods__["lastResizeTime"] = _lsf.jobInfoEnt_lastResizeTime_set
    __swig_getmethods__["lastResizeTime"] = _lsf.jobInfoEnt_lastResizeTime_get
    if _newclass:lastResizeTime = property(_lsf.jobInfoEnt_lastResizeTime_get, _lsf.jobInfoEnt_lastResizeTime_set)
    __swig_setmethods__["numhRusages"] = _lsf.jobInfoEnt_numhRusages_set
    __swig_getmethods__["numhRusages"] = _lsf.jobInfoEnt_numhRusages_get
    if _newclass:numhRusages = property(_lsf.jobInfoEnt_numhRusages_get, _lsf.jobInfoEnt_numhRusages_set)
    __swig_setmethods__["hostRusage"] = _lsf.jobInfoEnt_hostRusage_set
    __swig_getmethods__["hostRusage"] = _lsf.jobInfoEnt_hostRusage_get
    if _newclass:hostRusage = property(_lsf.jobInfoEnt_hostRusage_get, _lsf.jobInfoEnt_hostRusage_set)
    def __init__(self, *args): 
        this = _lsf.new_jobInfoEnt(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _lsf.delete_jobInfoEnt
    __del__ = lambda self : None;
jobInfoEnt_swigregister = _lsf.jobInfoEnt_swigregister
jobInfoEnt_swigregister(jobInfoEnt)

J_EXCEPT_OVERRUN = _lsf.J_EXCEPT_OVERRUN
J_EXCEPT_UNDERUN = _lsf.J_EXCEPT_UNDERUN
J_EXCEPT_IDLE = _lsf.J_EXCEPT_IDLE
J_EXCEPT_RUNTIME_EST_EXCEEDED = _lsf.J_EXCEPT_RUNTIME_EST_EXCEEDED
OVERRUN = _lsf.OVERRUN
UNDERRUN = _lsf.UNDERRUN
IDLE = _lsf.IDLE
SPACE = _lsf.SPACE
RUNTIME_EST_EXCEEDED = _lsf.RUNTIME_EST_EXCEEDED
class jobInfoReq(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, jobInfoReq, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, jobInfoReq, name)
    __repr__ = _swig_repr
    __swig_setmethods__["options"] = _lsf.jobInfoReq_options_set
    __swig_getmethods__["options"] = _lsf.jobInfoReq_options_get
    if _newclass:options = property(_lsf.jobInfoReq_options_get, _lsf.jobInfoReq_options_set)
    __swig_setmethods__["userName"] = _lsf.jobInfoReq_userName_set
    __swig_getmethods__["userName"] = _lsf.jobInfoReq_userName_get
    if _newclass:userName = property(_lsf.jobInfoReq_userName_get, _lsf.jobInfoReq_userName_set)
    __swig_setmethods__["jobId"] = _lsf.jobInfoReq_jobId_set
    __swig_getmethods__["jobId"] = _lsf.jobInfoReq_jobId_get
    if _newclass:jobId = property(_lsf.jobInfoReq_jobId_get, _lsf.jobInfoReq_jobId_set)
    __swig_setmethods__["jobName"] = _lsf.jobInfoReq_jobName_set
    __swig_getmethods__["jobName"] = _lsf.jobInfoReq_jobName_get
    if _newclass:jobName = property(_lsf.jobInfoReq_jobName_get, _lsf.jobInfoReq_jobName_set)
    __swig_setmethods__["queue"] = _lsf.jobInfoReq_queue_set
    __swig_getmethods__["queue"] = _lsf.jobInfoReq_queue_get
    if _newclass:queue = property(_lsf.jobInfoReq_queue_get, _lsf.jobInfoReq_queue_set)
    __swig_setmethods__["host"] = _lsf.jobInfoReq_host_set
    __swig_getmethods__["host"] = _lsf.jobInfoReq_host_get
    if _newclass:host = property(_lsf.jobInfoReq_host_get, _lsf.jobInfoReq_host_set)
    __swig_setmethods__["app"] = _lsf.jobInfoReq_app_set
    __swig_getmethods__["app"] = _lsf.jobInfoReq_app_get
    if _newclass:app = property(_lsf.jobInfoReq_app_get, _lsf.jobInfoReq_app_set)
    __swig_setmethods__["jobDescription"] = _lsf.jobInfoReq_jobDescription_set
    __swig_getmethods__["jobDescription"] = _lsf.jobInfoReq_jobDescription_get
    if _newclass:jobDescription = property(_lsf.jobInfoReq_jobDescription_get, _lsf.jobInfoReq_jobDescription_set)
    __swig_setmethods__["submitExt"] = _lsf.jobInfoReq_submitExt_set
    __swig_getmethods__["submitExt"] = _lsf.jobInfoReq_submitExt_get
    if _newclass:submitExt = property(_lsf.jobInfoReq_submitExt_get, _lsf.jobInfoReq_submitExt_set)
    def __init__(self, *args): 
        this = _lsf.new_jobInfoReq(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _lsf.delete_jobInfoReq
    __del__ = lambda self : None;
jobInfoReq_swigregister = _lsf.jobInfoReq_swigregister
jobInfoReq_swigregister(jobInfoReq)

class userInfoEnt(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, userInfoEnt, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, userInfoEnt, name)
    __repr__ = _swig_repr
    __swig_setmethods__["user"] = _lsf.userInfoEnt_user_set
    __swig_getmethods__["user"] = _lsf.userInfoEnt_user_get
    if _newclass:user = property(_lsf.userInfoEnt_user_get, _lsf.userInfoEnt_user_set)
    __swig_setmethods__["procJobLimit"] = _lsf.userInfoEnt_procJobLimit_set
    __swig_getmethods__["procJobLimit"] = _lsf.userInfoEnt_procJobLimit_get
    if _newclass:procJobLimit = property(_lsf.userInfoEnt_procJobLimit_get, _lsf.userInfoEnt_procJobLimit_set)
    __swig_setmethods__["maxJobs"] = _lsf.userInfoEnt_maxJobs_set
    __swig_getmethods__["maxJobs"] = _lsf.userInfoEnt_maxJobs_get
    if _newclass:maxJobs = property(_lsf.userInfoEnt_maxJobs_get, _lsf.userInfoEnt_maxJobs_set)
    __swig_setmethods__["numStartJobs"] = _lsf.userInfoEnt_numStartJobs_set
    __swig_getmethods__["numStartJobs"] = _lsf.userInfoEnt_numStartJobs_get
    if _newclass:numStartJobs = property(_lsf.userInfoEnt_numStartJobs_get, _lsf.userInfoEnt_numStartJobs_set)
    __swig_setmethods__["numJobs"] = _lsf.userInfoEnt_numJobs_set
    __swig_getmethods__["numJobs"] = _lsf.userInfoEnt_numJobs_get
    if _newclass:numJobs = property(_lsf.userInfoEnt_numJobs_get, _lsf.userInfoEnt_numJobs_set)
    __swig_setmethods__["numPEND"] = _lsf.userInfoEnt_numPEND_set
    __swig_getmethods__["numPEND"] = _lsf.userInfoEnt_numPEND_get
    if _newclass:numPEND = property(_lsf.userInfoEnt_numPEND_get, _lsf.userInfoEnt_numPEND_set)
    __swig_setmethods__["numRUN"] = _lsf.userInfoEnt_numRUN_set
    __swig_getmethods__["numRUN"] = _lsf.userInfoEnt_numRUN_get
    if _newclass:numRUN = property(_lsf.userInfoEnt_numRUN_get, _lsf.userInfoEnt_numRUN_set)
    __swig_setmethods__["numSSUSP"] = _lsf.userInfoEnt_numSSUSP_set
    __swig_getmethods__["numSSUSP"] = _lsf.userInfoEnt_numSSUSP_get
    if _newclass:numSSUSP = property(_lsf.userInfoEnt_numSSUSP_get, _lsf.userInfoEnt_numSSUSP_set)
    __swig_setmethods__["numUSUSP"] = _lsf.userInfoEnt_numUSUSP_set
    __swig_getmethods__["numUSUSP"] = _lsf.userInfoEnt_numUSUSP_get
    if _newclass:numUSUSP = property(_lsf.userInfoEnt_numUSUSP_get, _lsf.userInfoEnt_numUSUSP_set)
    __swig_setmethods__["numRESERVE"] = _lsf.userInfoEnt_numRESERVE_set
    __swig_getmethods__["numRESERVE"] = _lsf.userInfoEnt_numRESERVE_get
    if _newclass:numRESERVE = property(_lsf.userInfoEnt_numRESERVE_get, _lsf.userInfoEnt_numRESERVE_set)
    __swig_setmethods__["maxPendJobs"] = _lsf.userInfoEnt_maxPendJobs_set
    __swig_getmethods__["maxPendJobs"] = _lsf.userInfoEnt_maxPendJobs_get
    if _newclass:maxPendJobs = property(_lsf.userInfoEnt_maxPendJobs_get, _lsf.userInfoEnt_maxPendJobs_set)
    def __init__(self, *args): 
        this = _lsf.new_userInfoEnt(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _lsf.delete_userInfoEnt
    __del__ = lambda self : None;
userInfoEnt_swigregister = _lsf.userInfoEnt_swigregister
userInfoEnt_swigregister(userInfoEnt)

class userEquivalentInfoEnt(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, userEquivalentInfoEnt, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, userEquivalentInfoEnt, name)
    __repr__ = _swig_repr
    __swig_setmethods__["equivalentUsers"] = _lsf.userEquivalentInfoEnt_equivalentUsers_set
    __swig_getmethods__["equivalentUsers"] = _lsf.userEquivalentInfoEnt_equivalentUsers_get
    if _newclass:equivalentUsers = property(_lsf.userEquivalentInfoEnt_equivalentUsers_get, _lsf.userEquivalentInfoEnt_equivalentUsers_set)
    def __init__(self, *args): 
        this = _lsf.new_userEquivalentInfoEnt(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _lsf.delete_userEquivalentInfoEnt
    __del__ = lambda self : None;
userEquivalentInfoEnt_swigregister = _lsf.userEquivalentInfoEnt_swigregister
userEquivalentInfoEnt_swigregister(userEquivalentInfoEnt)

class userMappingInfoEnt(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, userMappingInfoEnt, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, userMappingInfoEnt, name)
    __repr__ = _swig_repr
    __swig_setmethods__["localUsers"] = _lsf.userMappingInfoEnt_localUsers_set
    __swig_getmethods__["localUsers"] = _lsf.userMappingInfoEnt_localUsers_get
    if _newclass:localUsers = property(_lsf.userMappingInfoEnt_localUsers_get, _lsf.userMappingInfoEnt_localUsers_set)
    __swig_setmethods__["remoteUsers"] = _lsf.userMappingInfoEnt_remoteUsers_set
    __swig_getmethods__["remoteUsers"] = _lsf.userMappingInfoEnt_remoteUsers_get
    if _newclass:remoteUsers = property(_lsf.userMappingInfoEnt_remoteUsers_get, _lsf.userMappingInfoEnt_remoteUsers_set)
    __swig_setmethods__["direction"] = _lsf.userMappingInfoEnt_direction_set
    __swig_getmethods__["direction"] = _lsf.userMappingInfoEnt_direction_get
    if _newclass:direction = property(_lsf.userMappingInfoEnt_direction_get, _lsf.userMappingInfoEnt_direction_set)
    def __init__(self, *args): 
        this = _lsf.new_userMappingInfoEnt(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _lsf.delete_userMappingInfoEnt
    __del__ = lambda self : None;
userMappingInfoEnt_swigregister = _lsf.userMappingInfoEnt_swigregister
userMappingInfoEnt_swigregister(userMappingInfoEnt)

class apsFactorMap(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, apsFactorMap, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, apsFactorMap, name)
    __repr__ = _swig_repr
    __swig_setmethods__["factorName"] = _lsf.apsFactorMap_factorName_set
    __swig_getmethods__["factorName"] = _lsf.apsFactorMap_factorName_get
    if _newclass:factorName = property(_lsf.apsFactorMap_factorName_get, _lsf.apsFactorMap_factorName_set)
    __swig_setmethods__["subFactorNames"] = _lsf.apsFactorMap_subFactorNames_set
    __swig_getmethods__["subFactorNames"] = _lsf.apsFactorMap_subFactorNames_get
    if _newclass:subFactorNames = property(_lsf.apsFactorMap_subFactorNames_get, _lsf.apsFactorMap_subFactorNames_set)
    def __init__(self, *args): 
        this = _lsf.new_apsFactorMap(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _lsf.delete_apsFactorMap
    __del__ = lambda self : None;
apsFactorMap_swigregister = _lsf.apsFactorMap_swigregister
apsFactorMap_swigregister(apsFactorMap)

class apsLongNameMap(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, apsLongNameMap, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, apsLongNameMap, name)
    __repr__ = _swig_repr
    __swig_setmethods__["shortName"] = _lsf.apsLongNameMap_shortName_set
    __swig_getmethods__["shortName"] = _lsf.apsLongNameMap_shortName_get
    if _newclass:shortName = property(_lsf.apsLongNameMap_shortName_get, _lsf.apsLongNameMap_shortName_set)
    __swig_setmethods__["longName"] = _lsf.apsLongNameMap_longName_set
    __swig_getmethods__["longName"] = _lsf.apsLongNameMap_longName_get
    if _newclass:longName = property(_lsf.apsLongNameMap_longName_get, _lsf.apsLongNameMap_longName_set)
    def __init__(self, *args): 
        this = _lsf.new_apsLongNameMap(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _lsf.delete_apsLongNameMap
    __del__ = lambda self : None;
apsLongNameMap_swigregister = _lsf.apsLongNameMap_swigregister
apsLongNameMap_swigregister(apsLongNameMap)

ALL_QUEUE = _lsf.ALL_QUEUE
DFT_QUEUE = _lsf.DFT_QUEUE
CHECK_HOST = _lsf.CHECK_HOST
CHECK_USER = _lsf.CHECK_USER
SORT_HOST = _lsf.SORT_HOST
QUEUE_SHORT_FORMAT = _lsf.QUEUE_SHORT_FORMAT
EXPAND_HOSTNAME = _lsf.EXPAND_HOSTNAME
RETRIEVE_BATCH = _lsf.RETRIEVE_BATCH
LSB_SIG_NUM_40 = _lsf.LSB_SIG_NUM_40
LSB_SIG_NUM_41 = _lsf.LSB_SIG_NUM_41
LSB_SIG_NUM_51 = _lsf.LSB_SIG_NUM_51
LSB_SIG_NUM_60 = _lsf.LSB_SIG_NUM_60
LSB_SIG_NUM = _lsf.LSB_SIG_NUM
DCP_LEND_HOSTS = _lsf.DCP_LEND_HOSTS
DCP_BORROW_HOSTS = _lsf.DCP_BORROW_HOSTS
DCP_ALLOC_CPU_OK = _lsf.DCP_ALLOC_CPU_OK
DCP_UNDER_ALLOC_CPU = _lsf.DCP_UNDER_ALLOC_CPU
DCP_JOB_WAIT_FOR_CPU = _lsf.DCP_JOB_WAIT_FOR_CPU
DCP_ALLOC_CPU_BUSY = _lsf.DCP_ALLOC_CPU_BUSY
class fsFactors(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, fsFactors, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, fsFactors, name)
    __repr__ = _swig_repr
    __swig_setmethods__["runTimeFactor"] = _lsf.fsFactors_runTimeFactor_set
    __swig_getmethods__["runTimeFactor"] = _lsf.fsFactors_runTimeFactor_get
    if _newclass:runTimeFactor = property(_lsf.fsFactors_runTimeFactor_get, _lsf.fsFactors_runTimeFactor_set)
    __swig_setmethods__["cpuTimeFactor"] = _lsf.fsFactors_cpuTimeFactor_set
    __swig_getmethods__["cpuTimeFactor"] = _lsf.fsFactors_cpuTimeFactor_get
    if _newclass:cpuTimeFactor = property(_lsf.fsFactors_cpuTimeFactor_get, _lsf.fsFactors_cpuTimeFactor_set)
    __swig_setmethods__["runJobFactor"] = _lsf.fsFactors_runJobFactor_set
    __swig_getmethods__["runJobFactor"] = _lsf.fsFactors_runJobFactor_get
    if _newclass:runJobFactor = property(_lsf.fsFactors_runJobFactor_get, _lsf.fsFactors_runJobFactor_set)
    __swig_setmethods__["histHours"] = _lsf.fsFactors_histHours_set
    __swig_getmethods__["histHours"] = _lsf.fsFactors_histHours_get
    if _newclass:histHours = property(_lsf.fsFactors_histHours_get, _lsf.fsFactors_histHours_set)
    __swig_setmethods__["committedRunTimeFactor"] = _lsf.fsFactors_committedRunTimeFactor_set
    __swig_getmethods__["committedRunTimeFactor"] = _lsf.fsFactors_committedRunTimeFactor_get
    if _newclass:committedRunTimeFactor = property(_lsf.fsFactors_committedRunTimeFactor_get, _lsf.fsFactors_committedRunTimeFactor_set)
    __swig_setmethods__["fairAdjustFactor"] = _lsf.fsFactors_fairAdjustFactor_set
    __swig_getmethods__["fairAdjustFactor"] = _lsf.fsFactors_fairAdjustFactor_get
    if _newclass:fairAdjustFactor = property(_lsf.fsFactors_fairAdjustFactor_get, _lsf.fsFactors_fairAdjustFactor_set)
    __swig_setmethods__["enableHistRunTime"] = _lsf.fsFactors_enableHistRunTime_set
    __swig_getmethods__["enableHistRunTime"] = _lsf.fsFactors_enableHistRunTime_get
    if _newclass:enableHistRunTime = property(_lsf.fsFactors_enableHistRunTime_get, _lsf.fsFactors_enableHistRunTime_set)
    __swig_setmethods__["enableRunTimeDecay"] = _lsf.fsFactors_enableRunTimeDecay_set
    __swig_getmethods__["enableRunTimeDecay"] = _lsf.fsFactors_enableRunTimeDecay_get
    if _newclass:enableRunTimeDecay = property(_lsf.fsFactors_enableRunTimeDecay_get, _lsf.fsFactors_enableRunTimeDecay_set)
    def __init__(self, *args): 
        this = _lsf.new_fsFactors(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _lsf.delete_fsFactors
    __del__ = lambda self : None;
fsFactors_swigregister = _lsf.fsFactors_swigregister
fsFactors_swigregister(fsFactors)

class queueInfoEnt(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, queueInfoEnt, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, queueInfoEnt, name)
    __repr__ = _swig_repr
    __swig_setmethods__["queue"] = _lsf.queueInfoEnt_queue_set
    __swig_getmethods__["queue"] = _lsf.queueInfoEnt_queue_get
    if _newclass:queue = property(_lsf.queueInfoEnt_queue_get, _lsf.queueInfoEnt_queue_set)
    __swig_setmethods__["description"] = _lsf.queueInfoEnt_description_set
    __swig_getmethods__["description"] = _lsf.queueInfoEnt_description_get
    if _newclass:description = property(_lsf.queueInfoEnt_description_get, _lsf.queueInfoEnt_description_set)
    __swig_setmethods__["priority"] = _lsf.queueInfoEnt_priority_set
    __swig_getmethods__["priority"] = _lsf.queueInfoEnt_priority_get
    if _newclass:priority = property(_lsf.queueInfoEnt_priority_get, _lsf.queueInfoEnt_priority_set)
    __swig_setmethods__["nice"] = _lsf.queueInfoEnt_nice_set
    __swig_getmethods__["nice"] = _lsf.queueInfoEnt_nice_get
    if _newclass:nice = property(_lsf.queueInfoEnt_nice_get, _lsf.queueInfoEnt_nice_set)
    __swig_setmethods__["userList"] = _lsf.queueInfoEnt_userList_set
    __swig_getmethods__["userList"] = _lsf.queueInfoEnt_userList_get
    if _newclass:userList = property(_lsf.queueInfoEnt_userList_get, _lsf.queueInfoEnt_userList_set)
    __swig_setmethods__["hostList"] = _lsf.queueInfoEnt_hostList_set
    __swig_getmethods__["hostList"] = _lsf.queueInfoEnt_hostList_get
    if _newclass:hostList = property(_lsf.queueInfoEnt_hostList_get, _lsf.queueInfoEnt_hostList_set)
    __swig_setmethods__["hostStr"] = _lsf.queueInfoEnt_hostStr_set
    __swig_getmethods__["hostStr"] = _lsf.queueInfoEnt_hostStr_get
    if _newclass:hostStr = property(_lsf.queueInfoEnt_hostStr_get, _lsf.queueInfoEnt_hostStr_set)
    __swig_setmethods__["nIdx"] = _lsf.queueInfoEnt_nIdx_set
    __swig_getmethods__["nIdx"] = _lsf.queueInfoEnt_nIdx_get
    if _newclass:nIdx = property(_lsf.queueInfoEnt_nIdx_get, _lsf.queueInfoEnt_nIdx_set)
    __swig_setmethods__["loadSched"] = _lsf.queueInfoEnt_loadSched_set
    __swig_getmethods__["loadSched"] = _lsf.queueInfoEnt_loadSched_get
    if _newclass:loadSched = property(_lsf.queueInfoEnt_loadSched_get, _lsf.queueInfoEnt_loadSched_set)
    __swig_setmethods__["loadStop"] = _lsf.queueInfoEnt_loadStop_set
    __swig_getmethods__["loadStop"] = _lsf.queueInfoEnt_loadStop_get
    if _newclass:loadStop = property(_lsf.queueInfoEnt_loadStop_get, _lsf.queueInfoEnt_loadStop_set)
    __swig_setmethods__["userJobLimit"] = _lsf.queueInfoEnt_userJobLimit_set
    __swig_getmethods__["userJobLimit"] = _lsf.queueInfoEnt_userJobLimit_get
    if _newclass:userJobLimit = property(_lsf.queueInfoEnt_userJobLimit_get, _lsf.queueInfoEnt_userJobLimit_set)
    __swig_setmethods__["procJobLimit"] = _lsf.queueInfoEnt_procJobLimit_set
    __swig_getmethods__["procJobLimit"] = _lsf.queueInfoEnt_procJobLimit_get
    if _newclass:procJobLimit = property(_lsf.queueInfoEnt_procJobLimit_get, _lsf.queueInfoEnt_procJobLimit_set)
    __swig_setmethods__["windows"] = _lsf.queueInfoEnt_windows_set
    __swig_getmethods__["windows"] = _lsf.queueInfoEnt_windows_get
    if _newclass:windows = property(_lsf.queueInfoEnt_windows_get, _lsf.queueInfoEnt_windows_set)
    __swig_setmethods__["rLimits"] = _lsf.queueInfoEnt_rLimits_set
    __swig_getmethods__["rLimits"] = _lsf.queueInfoEnt_rLimits_get
    if _newclass:rLimits = property(_lsf.queueInfoEnt_rLimits_get, _lsf.queueInfoEnt_rLimits_set)
    __swig_setmethods__["hostSpec"] = _lsf.queueInfoEnt_hostSpec_set
    __swig_getmethods__["hostSpec"] = _lsf.queueInfoEnt_hostSpec_get
    if _newclass:hostSpec = property(_lsf.queueInfoEnt_hostSpec_get, _lsf.queueInfoEnt_hostSpec_set)
    __swig_setmethods__["qAttrib"] = _lsf.queueInfoEnt_qAttrib_set
    __swig_getmethods__["qAttrib"] = _lsf.queueInfoEnt_qAttrib_get
    if _newclass:qAttrib = property(_lsf.queueInfoEnt_qAttrib_get, _lsf.queueInfoEnt_qAttrib_set)
    __swig_setmethods__["qStatus"] = _lsf.queueInfoEnt_qStatus_set
    __swig_getmethods__["qStatus"] = _lsf.queueInfoEnt_qStatus_get
    if _newclass:qStatus = property(_lsf.queueInfoEnt_qStatus_get, _lsf.queueInfoEnt_qStatus_set)
    __swig_setmethods__["maxJobs"] = _lsf.queueInfoEnt_maxJobs_set
    __swig_getmethods__["maxJobs"] = _lsf.queueInfoEnt_maxJobs_get
    if _newclass:maxJobs = property(_lsf.queueInfoEnt_maxJobs_get, _lsf.queueInfoEnt_maxJobs_set)
    __swig_setmethods__["numJobs"] = _lsf.queueInfoEnt_numJobs_set
    __swig_getmethods__["numJobs"] = _lsf.queueInfoEnt_numJobs_get
    if _newclass:numJobs = property(_lsf.queueInfoEnt_numJobs_get, _lsf.queueInfoEnt_numJobs_set)
    __swig_setmethods__["numPEND"] = _lsf.queueInfoEnt_numPEND_set
    __swig_getmethods__["numPEND"] = _lsf.queueInfoEnt_numPEND_get
    if _newclass:numPEND = property(_lsf.queueInfoEnt_numPEND_get, _lsf.queueInfoEnt_numPEND_set)
    __swig_setmethods__["numRUN"] = _lsf.queueInfoEnt_numRUN_set
    __swig_getmethods__["numRUN"] = _lsf.queueInfoEnt_numRUN_get
    if _newclass:numRUN = property(_lsf.queueInfoEnt_numRUN_get, _lsf.queueInfoEnt_numRUN_set)
    __swig_setmethods__["numSSUSP"] = _lsf.queueInfoEnt_numSSUSP_set
    __swig_getmethods__["numSSUSP"] = _lsf.queueInfoEnt_numSSUSP_get
    if _newclass:numSSUSP = property(_lsf.queueInfoEnt_numSSUSP_get, _lsf.queueInfoEnt_numSSUSP_set)
    __swig_setmethods__["numUSUSP"] = _lsf.queueInfoEnt_numUSUSP_set
    __swig_getmethods__["numUSUSP"] = _lsf.queueInfoEnt_numUSUSP_get
    if _newclass:numUSUSP = property(_lsf.queueInfoEnt_numUSUSP_get, _lsf.queueInfoEnt_numUSUSP_set)
    __swig_setmethods__["mig"] = _lsf.queueInfoEnt_mig_set
    __swig_getmethods__["mig"] = _lsf.queueInfoEnt_mig_get
    if _newclass:mig = property(_lsf.queueInfoEnt_mig_get, _lsf.queueInfoEnt_mig_set)
    __swig_setmethods__["schedDelay"] = _lsf.queueInfoEnt_schedDelay_set
    __swig_getmethods__["schedDelay"] = _lsf.queueInfoEnt_schedDelay_get
    if _newclass:schedDelay = property(_lsf.queueInfoEnt_schedDelay_get, _lsf.queueInfoEnt_schedDelay_set)
    __swig_setmethods__["acceptIntvl"] = _lsf.queueInfoEnt_acceptIntvl_set
    __swig_getmethods__["acceptIntvl"] = _lsf.queueInfoEnt_acceptIntvl_get
    if _newclass:acceptIntvl = property(_lsf.queueInfoEnt_acceptIntvl_get, _lsf.queueInfoEnt_acceptIntvl_set)
    __swig_setmethods__["windowsD"] = _lsf.queueInfoEnt_windowsD_set
    __swig_getmethods__["windowsD"] = _lsf.queueInfoEnt_windowsD_get
    if _newclass:windowsD = property(_lsf.queueInfoEnt_windowsD_get, _lsf.queueInfoEnt_windowsD_set)
    __swig_setmethods__["nqsQueues"] = _lsf.queueInfoEnt_nqsQueues_set
    __swig_getmethods__["nqsQueues"] = _lsf.queueInfoEnt_nqsQueues_get
    if _newclass:nqsQueues = property(_lsf.queueInfoEnt_nqsQueues_get, _lsf.queueInfoEnt_nqsQueues_set)
    __swig_setmethods__["userShares"] = _lsf.queueInfoEnt_userShares_set
    __swig_getmethods__["userShares"] = _lsf.queueInfoEnt_userShares_get
    if _newclass:userShares = property(_lsf.queueInfoEnt_userShares_get, _lsf.queueInfoEnt_userShares_set)
    __swig_setmethods__["defaultHostSpec"] = _lsf.queueInfoEnt_defaultHostSpec_set
    __swig_getmethods__["defaultHostSpec"] = _lsf.queueInfoEnt_defaultHostSpec_get
    if _newclass:defaultHostSpec = property(_lsf.queueInfoEnt_defaultHostSpec_get, _lsf.queueInfoEnt_defaultHostSpec_set)
    __swig_setmethods__["procLimit"] = _lsf.queueInfoEnt_procLimit_set
    __swig_getmethods__["procLimit"] = _lsf.queueInfoEnt_procLimit_get
    if _newclass:procLimit = property(_lsf.queueInfoEnt_procLimit_get, _lsf.queueInfoEnt_procLimit_set)
    __swig_setmethods__["admins"] = _lsf.queueInfoEnt_admins_set
    __swig_getmethods__["admins"] = _lsf.queueInfoEnt_admins_get
    if _newclass:admins = property(_lsf.queueInfoEnt_admins_get, _lsf.queueInfoEnt_admins_set)
    __swig_setmethods__["preCmd"] = _lsf.queueInfoEnt_preCmd_set
    __swig_getmethods__["preCmd"] = _lsf.queueInfoEnt_preCmd_get
    if _newclass:preCmd = property(_lsf.queueInfoEnt_preCmd_get, _lsf.queueInfoEnt_preCmd_set)
    __swig_setmethods__["postCmd"] = _lsf.queueInfoEnt_postCmd_set
    __swig_getmethods__["postCmd"] = _lsf.queueInfoEnt_postCmd_get
    if _newclass:postCmd = property(_lsf.queueInfoEnt_postCmd_get, _lsf.queueInfoEnt_postCmd_set)
    __swig_setmethods__["requeueEValues"] = _lsf.queueInfoEnt_requeueEValues_set
    __swig_getmethods__["requeueEValues"] = _lsf.queueInfoEnt_requeueEValues_get
    if _newclass:requeueEValues = property(_lsf.queueInfoEnt_requeueEValues_get, _lsf.queueInfoEnt_requeueEValues_set)
    __swig_setmethods__["hostJobLimit"] = _lsf.queueInfoEnt_hostJobLimit_set
    __swig_getmethods__["hostJobLimit"] = _lsf.queueInfoEnt_hostJobLimit_get
    if _newclass:hostJobLimit = property(_lsf.queueInfoEnt_hostJobLimit_get, _lsf.queueInfoEnt_hostJobLimit_set)
    __swig_setmethods__["resReq"] = _lsf.queueInfoEnt_resReq_set
    __swig_getmethods__["resReq"] = _lsf.queueInfoEnt_resReq_get
    if _newclass:resReq = property(_lsf.queueInfoEnt_resReq_get, _lsf.queueInfoEnt_resReq_set)
    __swig_setmethods__["numRESERVE"] = _lsf.queueInfoEnt_numRESERVE_set
    __swig_getmethods__["numRESERVE"] = _lsf.queueInfoEnt_numRESERVE_get
    if _newclass:numRESERVE = property(_lsf.queueInfoEnt_numRESERVE_get, _lsf.queueInfoEnt_numRESERVE_set)
    __swig_setmethods__["slotHoldTime"] = _lsf.queueInfoEnt_slotHoldTime_set
    __swig_getmethods__["slotHoldTime"] = _lsf.queueInfoEnt_slotHoldTime_get
    if _newclass:slotHoldTime = property(_lsf.queueInfoEnt_slotHoldTime_get, _lsf.queueInfoEnt_slotHoldTime_set)
    __swig_setmethods__["sndJobsTo"] = _lsf.queueInfoEnt_sndJobsTo_set
    __swig_getmethods__["sndJobsTo"] = _lsf.queueInfoEnt_sndJobsTo_get
    if _newclass:sndJobsTo = property(_lsf.queueInfoEnt_sndJobsTo_get, _lsf.queueInfoEnt_sndJobsTo_set)
    __swig_setmethods__["rcvJobsFrom"] = _lsf.queueInfoEnt_rcvJobsFrom_set
    __swig_getmethods__["rcvJobsFrom"] = _lsf.queueInfoEnt_rcvJobsFrom_get
    if _newclass:rcvJobsFrom = property(_lsf.queueInfoEnt_rcvJobsFrom_get, _lsf.queueInfoEnt_rcvJobsFrom_set)
    __swig_setmethods__["resumeCond"] = _lsf.queueInfoEnt_resumeCond_set
    __swig_getmethods__["resumeCond"] = _lsf.queueInfoEnt_resumeCond_get
    if _newclass:resumeCond = property(_lsf.queueInfoEnt_resumeCond_get, _lsf.queueInfoEnt_resumeCond_set)
    __swig_setmethods__["stopCond"] = _lsf.queueInfoEnt_stopCond_set
    __swig_getmethods__["stopCond"] = _lsf.queueInfoEnt_stopCond_get
    if _newclass:stopCond = property(_lsf.queueInfoEnt_stopCond_get, _lsf.queueInfoEnt_stopCond_set)
    __swig_setmethods__["jobStarter"] = _lsf.queueInfoEnt_jobStarter_set
    __swig_getmethods__["jobStarter"] = _lsf.queueInfoEnt_jobStarter_get
    if _newclass:jobStarter = property(_lsf.queueInfoEnt_jobStarter_get, _lsf.queueInfoEnt_jobStarter_set)
    __swig_setmethods__["suspendActCmd"] = _lsf.queueInfoEnt_suspendActCmd_set
    __swig_getmethods__["suspendActCmd"] = _lsf.queueInfoEnt_suspendActCmd_get
    if _newclass:suspendActCmd = property(_lsf.queueInfoEnt_suspendActCmd_get, _lsf.queueInfoEnt_suspendActCmd_set)
    __swig_setmethods__["resumeActCmd"] = _lsf.queueInfoEnt_resumeActCmd_set
    __swig_getmethods__["resumeActCmd"] = _lsf.queueInfoEnt_resumeActCmd_get
    if _newclass:resumeActCmd = property(_lsf.queueInfoEnt_resumeActCmd_get, _lsf.queueInfoEnt_resumeActCmd_set)
    __swig_setmethods__["terminateActCmd"] = _lsf.queueInfoEnt_terminateActCmd_set
    __swig_getmethods__["terminateActCmd"] = _lsf.queueInfoEnt_terminateActCmd_get
    if _newclass:terminateActCmd = property(_lsf.queueInfoEnt_terminateActCmd_get, _lsf.queueInfoEnt_terminateActCmd_set)
    __swig_setmethods__["sigMap"] = _lsf.queueInfoEnt_sigMap_set
    __swig_getmethods__["sigMap"] = _lsf.queueInfoEnt_sigMap_get
    if _newclass:sigMap = property(_lsf.queueInfoEnt_sigMap_get, _lsf.queueInfoEnt_sigMap_set)
    __swig_setmethods__["preemption"] = _lsf.queueInfoEnt_preemption_set
    __swig_getmethods__["preemption"] = _lsf.queueInfoEnt_preemption_get
    if _newclass:preemption = property(_lsf.queueInfoEnt_preemption_get, _lsf.queueInfoEnt_preemption_set)
    __swig_setmethods__["maxRschedTime"] = _lsf.queueInfoEnt_maxRschedTime_set
    __swig_getmethods__["maxRschedTime"] = _lsf.queueInfoEnt_maxRschedTime_get
    if _newclass:maxRschedTime = property(_lsf.queueInfoEnt_maxRschedTime_get, _lsf.queueInfoEnt_maxRschedTime_set)
    __swig_setmethods__["numOfSAccts"] = _lsf.queueInfoEnt_numOfSAccts_set
    __swig_getmethods__["numOfSAccts"] = _lsf.queueInfoEnt_numOfSAccts_get
    if _newclass:numOfSAccts = property(_lsf.queueInfoEnt_numOfSAccts_get, _lsf.queueInfoEnt_numOfSAccts_set)
    __swig_setmethods__["shareAccts"] = _lsf.queueInfoEnt_shareAccts_set
    __swig_getmethods__["shareAccts"] = _lsf.queueInfoEnt_shareAccts_get
    if _newclass:shareAccts = property(_lsf.queueInfoEnt_shareAccts_get, _lsf.queueInfoEnt_shareAccts_set)
    __swig_setmethods__["chkpntDir"] = _lsf.queueInfoEnt_chkpntDir_set
    __swig_getmethods__["chkpntDir"] = _lsf.queueInfoEnt_chkpntDir_get
    if _newclass:chkpntDir = property(_lsf.queueInfoEnt_chkpntDir_get, _lsf.queueInfoEnt_chkpntDir_set)
    __swig_setmethods__["chkpntPeriod"] = _lsf.queueInfoEnt_chkpntPeriod_set
    __swig_getmethods__["chkpntPeriod"] = _lsf.queueInfoEnt_chkpntPeriod_get
    if _newclass:chkpntPeriod = property(_lsf.queueInfoEnt_chkpntPeriod_get, _lsf.queueInfoEnt_chkpntPeriod_set)
    __swig_setmethods__["imptJobBklg"] = _lsf.queueInfoEnt_imptJobBklg_set
    __swig_getmethods__["imptJobBklg"] = _lsf.queueInfoEnt_imptJobBklg_get
    if _newclass:imptJobBklg = property(_lsf.queueInfoEnt_imptJobBklg_get, _lsf.queueInfoEnt_imptJobBklg_set)
    __swig_setmethods__["defLimits"] = _lsf.queueInfoEnt_defLimits_set
    __swig_getmethods__["defLimits"] = _lsf.queueInfoEnt_defLimits_get
    if _newclass:defLimits = property(_lsf.queueInfoEnt_defLimits_get, _lsf.queueInfoEnt_defLimits_set)
    __swig_setmethods__["chunkJobSize"] = _lsf.queueInfoEnt_chunkJobSize_set
    __swig_getmethods__["chunkJobSize"] = _lsf.queueInfoEnt_chunkJobSize_get
    if _newclass:chunkJobSize = property(_lsf.queueInfoEnt_chunkJobSize_get, _lsf.queueInfoEnt_chunkJobSize_set)
    __swig_setmethods__["minProcLimit"] = _lsf.queueInfoEnt_minProcLimit_set
    __swig_getmethods__["minProcLimit"] = _lsf.queueInfoEnt_minProcLimit_get
    if _newclass:minProcLimit = property(_lsf.queueInfoEnt_minProcLimit_get, _lsf.queueInfoEnt_minProcLimit_set)
    __swig_setmethods__["defProcLimit"] = _lsf.queueInfoEnt_defProcLimit_set
    __swig_getmethods__["defProcLimit"] = _lsf.queueInfoEnt_defProcLimit_get
    if _newclass:defProcLimit = property(_lsf.queueInfoEnt_defProcLimit_get, _lsf.queueInfoEnt_defProcLimit_set)
    __swig_setmethods__["fairshareQueues"] = _lsf.queueInfoEnt_fairshareQueues_set
    __swig_getmethods__["fairshareQueues"] = _lsf.queueInfoEnt_fairshareQueues_get
    if _newclass:fairshareQueues = property(_lsf.queueInfoEnt_fairshareQueues_get, _lsf.queueInfoEnt_fairshareQueues_set)
    __swig_setmethods__["defExtSched"] = _lsf.queueInfoEnt_defExtSched_set
    __swig_getmethods__["defExtSched"] = _lsf.queueInfoEnt_defExtSched_get
    if _newclass:defExtSched = property(_lsf.queueInfoEnt_defExtSched_get, _lsf.queueInfoEnt_defExtSched_set)
    __swig_setmethods__["mandExtSched"] = _lsf.queueInfoEnt_mandExtSched_set
    __swig_getmethods__["mandExtSched"] = _lsf.queueInfoEnt_mandExtSched_get
    if _newclass:mandExtSched = property(_lsf.queueInfoEnt_mandExtSched_get, _lsf.queueInfoEnt_mandExtSched_set)
    __swig_setmethods__["slotShare"] = _lsf.queueInfoEnt_slotShare_set
    __swig_getmethods__["slotShare"] = _lsf.queueInfoEnt_slotShare_get
    if _newclass:slotShare = property(_lsf.queueInfoEnt_slotShare_get, _lsf.queueInfoEnt_slotShare_set)
    __swig_setmethods__["slotPool"] = _lsf.queueInfoEnt_slotPool_set
    __swig_getmethods__["slotPool"] = _lsf.queueInfoEnt_slotPool_get
    if _newclass:slotPool = property(_lsf.queueInfoEnt_slotPool_get, _lsf.queueInfoEnt_slotPool_set)
    __swig_setmethods__["underRCond"] = _lsf.queueInfoEnt_underRCond_set
    __swig_getmethods__["underRCond"] = _lsf.queueInfoEnt_underRCond_get
    if _newclass:underRCond = property(_lsf.queueInfoEnt_underRCond_get, _lsf.queueInfoEnt_underRCond_set)
    __swig_setmethods__["overRCond"] = _lsf.queueInfoEnt_overRCond_set
    __swig_getmethods__["overRCond"] = _lsf.queueInfoEnt_overRCond_get
    if _newclass:overRCond = property(_lsf.queueInfoEnt_overRCond_get, _lsf.queueInfoEnt_overRCond_set)
    __swig_setmethods__["idleCond"] = _lsf.queueInfoEnt_idleCond_set
    __swig_getmethods__["idleCond"] = _lsf.queueInfoEnt_idleCond_get
    if _newclass:idleCond = property(_lsf.queueInfoEnt_idleCond_get, _lsf.queueInfoEnt_idleCond_set)
    __swig_setmethods__["underRJobs"] = _lsf.queueInfoEnt_underRJobs_set
    __swig_getmethods__["underRJobs"] = _lsf.queueInfoEnt_underRJobs_get
    if _newclass:underRJobs = property(_lsf.queueInfoEnt_underRJobs_get, _lsf.queueInfoEnt_underRJobs_set)
    __swig_setmethods__["overRJobs"] = _lsf.queueInfoEnt_overRJobs_set
    __swig_getmethods__["overRJobs"] = _lsf.queueInfoEnt_overRJobs_get
    if _newclass:overRJobs = property(_lsf.queueInfoEnt_overRJobs_get, _lsf.queueInfoEnt_overRJobs_set)
    __swig_setmethods__["idleJobs"] = _lsf.queueInfoEnt_idleJobs_set
    __swig_getmethods__["idleJobs"] = _lsf.queueInfoEnt_idleJobs_get
    if _newclass:idleJobs = property(_lsf.queueInfoEnt_idleJobs_get, _lsf.queueInfoEnt_idleJobs_set)
    __swig_setmethods__["warningTimePeriod"] = _lsf.queueInfoEnt_warningTimePeriod_set
    __swig_getmethods__["warningTimePeriod"] = _lsf.queueInfoEnt_warningTimePeriod_get
    if _newclass:warningTimePeriod = property(_lsf.queueInfoEnt_warningTimePeriod_get, _lsf.queueInfoEnt_warningTimePeriod_set)
    __swig_setmethods__["warningAction"] = _lsf.queueInfoEnt_warningAction_set
    __swig_getmethods__["warningAction"] = _lsf.queueInfoEnt_warningAction_get
    if _newclass:warningAction = property(_lsf.queueInfoEnt_warningAction_get, _lsf.queueInfoEnt_warningAction_set)
    __swig_setmethods__["qCtrlMsg"] = _lsf.queueInfoEnt_qCtrlMsg_set
    __swig_getmethods__["qCtrlMsg"] = _lsf.queueInfoEnt_qCtrlMsg_get
    if _newclass:qCtrlMsg = property(_lsf.queueInfoEnt_qCtrlMsg_get, _lsf.queueInfoEnt_qCtrlMsg_set)
    __swig_setmethods__["acResReq"] = _lsf.queueInfoEnt_acResReq_set
    __swig_getmethods__["acResReq"] = _lsf.queueInfoEnt_acResReq_get
    if _newclass:acResReq = property(_lsf.queueInfoEnt_acResReq_get, _lsf.queueInfoEnt_acResReq_set)
    __swig_setmethods__["symJobLimit"] = _lsf.queueInfoEnt_symJobLimit_set
    __swig_getmethods__["symJobLimit"] = _lsf.queueInfoEnt_symJobLimit_get
    if _newclass:symJobLimit = property(_lsf.queueInfoEnt_symJobLimit_get, _lsf.queueInfoEnt_symJobLimit_set)
    __swig_setmethods__["cpuReq"] = _lsf.queueInfoEnt_cpuReq_set
    __swig_getmethods__["cpuReq"] = _lsf.queueInfoEnt_cpuReq_get
    if _newclass:cpuReq = property(_lsf.queueInfoEnt_cpuReq_get, _lsf.queueInfoEnt_cpuReq_set)
    __swig_setmethods__["proAttr"] = _lsf.queueInfoEnt_proAttr_set
    __swig_getmethods__["proAttr"] = _lsf.queueInfoEnt_proAttr_get
    if _newclass:proAttr = property(_lsf.queueInfoEnt_proAttr_get, _lsf.queueInfoEnt_proAttr_set)
    __swig_setmethods__["lendLimit"] = _lsf.queueInfoEnt_lendLimit_set
    __swig_getmethods__["lendLimit"] = _lsf.queueInfoEnt_lendLimit_get
    if _newclass:lendLimit = property(_lsf.queueInfoEnt_lendLimit_get, _lsf.queueInfoEnt_lendLimit_set)
    __swig_setmethods__["hostReallocInterval"] = _lsf.queueInfoEnt_hostReallocInterval_set
    __swig_getmethods__["hostReallocInterval"] = _lsf.queueInfoEnt_hostReallocInterval_get
    if _newclass:hostReallocInterval = property(_lsf.queueInfoEnt_hostReallocInterval_get, _lsf.queueInfoEnt_hostReallocInterval_set)
    __swig_setmethods__["numCPURequired"] = _lsf.queueInfoEnt_numCPURequired_set
    __swig_getmethods__["numCPURequired"] = _lsf.queueInfoEnt_numCPURequired_get
    if _newclass:numCPURequired = property(_lsf.queueInfoEnt_numCPURequired_get, _lsf.queueInfoEnt_numCPURequired_set)
    __swig_setmethods__["numCPUAllocated"] = _lsf.queueInfoEnt_numCPUAllocated_set
    __swig_getmethods__["numCPUAllocated"] = _lsf.queueInfoEnt_numCPUAllocated_get
    if _newclass:numCPUAllocated = property(_lsf.queueInfoEnt_numCPUAllocated_get, _lsf.queueInfoEnt_numCPUAllocated_set)
    __swig_setmethods__["numCPUBorrowed"] = _lsf.queueInfoEnt_numCPUBorrowed_set
    __swig_getmethods__["numCPUBorrowed"] = _lsf.queueInfoEnt_numCPUBorrowed_get
    if _newclass:numCPUBorrowed = property(_lsf.queueInfoEnt_numCPUBorrowed_get, _lsf.queueInfoEnt_numCPUBorrowed_set)
    __swig_setmethods__["numCPULent"] = _lsf.queueInfoEnt_numCPULent_set
    __swig_getmethods__["numCPULent"] = _lsf.queueInfoEnt_numCPULent_get
    if _newclass:numCPULent = property(_lsf.queueInfoEnt_numCPULent_get, _lsf.queueInfoEnt_numCPULent_set)
    __swig_setmethods__["schGranularity"] = _lsf.queueInfoEnt_schGranularity_set
    __swig_getmethods__["schGranularity"] = _lsf.queueInfoEnt_schGranularity_get
    if _newclass:schGranularity = property(_lsf.queueInfoEnt_schGranularity_get, _lsf.queueInfoEnt_schGranularity_set)
    __swig_setmethods__["symTaskGracePeriod"] = _lsf.queueInfoEnt_symTaskGracePeriod_set
    __swig_getmethods__["symTaskGracePeriod"] = _lsf.queueInfoEnt_symTaskGracePeriod_get
    if _newclass:symTaskGracePeriod = property(_lsf.queueInfoEnt_symTaskGracePeriod_get, _lsf.queueInfoEnt_symTaskGracePeriod_set)
    __swig_setmethods__["minOfSsm"] = _lsf.queueInfoEnt_minOfSsm_set
    __swig_getmethods__["minOfSsm"] = _lsf.queueInfoEnt_minOfSsm_get
    if _newclass:minOfSsm = property(_lsf.queueInfoEnt_minOfSsm_get, _lsf.queueInfoEnt_minOfSsm_set)
    __swig_setmethods__["maxOfSsm"] = _lsf.queueInfoEnt_maxOfSsm_set
    __swig_getmethods__["maxOfSsm"] = _lsf.queueInfoEnt_maxOfSsm_get
    if _newclass:maxOfSsm = property(_lsf.queueInfoEnt_maxOfSsm_get, _lsf.queueInfoEnt_maxOfSsm_set)
    __swig_setmethods__["numOfAllocSlots"] = _lsf.queueInfoEnt_numOfAllocSlots_set
    __swig_getmethods__["numOfAllocSlots"] = _lsf.queueInfoEnt_numOfAllocSlots_get
    if _newclass:numOfAllocSlots = property(_lsf.queueInfoEnt_numOfAllocSlots_get, _lsf.queueInfoEnt_numOfAllocSlots_set)
    __swig_setmethods__["servicePreemption"] = _lsf.queueInfoEnt_servicePreemption_set
    __swig_getmethods__["servicePreemption"] = _lsf.queueInfoEnt_servicePreemption_get
    if _newclass:servicePreemption = property(_lsf.queueInfoEnt_servicePreemption_get, _lsf.queueInfoEnt_servicePreemption_set)
    __swig_setmethods__["provisionStatus"] = _lsf.queueInfoEnt_provisionStatus_set
    __swig_getmethods__["provisionStatus"] = _lsf.queueInfoEnt_provisionStatus_get
    if _newclass:provisionStatus = property(_lsf.queueInfoEnt_provisionStatus_get, _lsf.queueInfoEnt_provisionStatus_set)
    __swig_setmethods__["minTimeSlice"] = _lsf.queueInfoEnt_minTimeSlice_set
    __swig_getmethods__["minTimeSlice"] = _lsf.queueInfoEnt_minTimeSlice_get
    if _newclass:minTimeSlice = property(_lsf.queueInfoEnt_minTimeSlice_get, _lsf.queueInfoEnt_minTimeSlice_set)
    __swig_setmethods__["queueGroup"] = _lsf.queueInfoEnt_queueGroup_set
    __swig_getmethods__["queueGroup"] = _lsf.queueInfoEnt_queueGroup_get
    if _newclass:queueGroup = property(_lsf.queueInfoEnt_queueGroup_get, _lsf.queueInfoEnt_queueGroup_set)
    __swig_setmethods__["numApsFactors"] = _lsf.queueInfoEnt_numApsFactors_set
    __swig_getmethods__["numApsFactors"] = _lsf.queueInfoEnt_numApsFactors_get
    if _newclass:numApsFactors = property(_lsf.queueInfoEnt_numApsFactors_get, _lsf.queueInfoEnt_numApsFactors_set)
    __swig_setmethods__["apsFactorInfoList"] = _lsf.queueInfoEnt_apsFactorInfoList_set
    __swig_getmethods__["apsFactorInfoList"] = _lsf.queueInfoEnt_apsFactorInfoList_get
    if _newclass:apsFactorInfoList = property(_lsf.queueInfoEnt_apsFactorInfoList_get, _lsf.queueInfoEnt_apsFactorInfoList_set)
    __swig_setmethods__["apsFactorMaps"] = _lsf.queueInfoEnt_apsFactorMaps_set
    __swig_getmethods__["apsFactorMaps"] = _lsf.queueInfoEnt_apsFactorMaps_get
    if _newclass:apsFactorMaps = property(_lsf.queueInfoEnt_apsFactorMaps_get, _lsf.queueInfoEnt_apsFactorMaps_set)
    __swig_setmethods__["apsLongNames"] = _lsf.queueInfoEnt_apsLongNames_set
    __swig_getmethods__["apsLongNames"] = _lsf.queueInfoEnt_apsLongNames_get
    if _newclass:apsLongNames = property(_lsf.queueInfoEnt_apsLongNames_get, _lsf.queueInfoEnt_apsLongNames_set)
    __swig_setmethods__["maxJobPreempt"] = _lsf.queueInfoEnt_maxJobPreempt_set
    __swig_getmethods__["maxJobPreempt"] = _lsf.queueInfoEnt_maxJobPreempt_get
    if _newclass:maxJobPreempt = property(_lsf.queueInfoEnt_maxJobPreempt_get, _lsf.queueInfoEnt_maxJobPreempt_set)
    __swig_setmethods__["maxPreExecRetry"] = _lsf.queueInfoEnt_maxPreExecRetry_set
    __swig_getmethods__["maxPreExecRetry"] = _lsf.queueInfoEnt_maxPreExecRetry_get
    if _newclass:maxPreExecRetry = property(_lsf.queueInfoEnt_maxPreExecRetry_get, _lsf.queueInfoEnt_maxPreExecRetry_set)
    __swig_setmethods__["localMaxPreExecRetry"] = _lsf.queueInfoEnt_localMaxPreExecRetry_set
    __swig_getmethods__["localMaxPreExecRetry"] = _lsf.queueInfoEnt_localMaxPreExecRetry_get
    if _newclass:localMaxPreExecRetry = property(_lsf.queueInfoEnt_localMaxPreExecRetry_get, _lsf.queueInfoEnt_localMaxPreExecRetry_set)
    __swig_setmethods__["maxJobRequeue"] = _lsf.queueInfoEnt_maxJobRequeue_set
    __swig_getmethods__["maxJobRequeue"] = _lsf.queueInfoEnt_maxJobRequeue_get
    if _newclass:maxJobRequeue = property(_lsf.queueInfoEnt_maxJobRequeue_get, _lsf.queueInfoEnt_maxJobRequeue_set)
    __swig_setmethods__["usePam"] = _lsf.queueInfoEnt_usePam_set
    __swig_getmethods__["usePam"] = _lsf.queueInfoEnt_usePam_get
    if _newclass:usePam = property(_lsf.queueInfoEnt_usePam_get, _lsf.queueInfoEnt_usePam_set)
    __swig_setmethods__["cu_type_exclusive"] = _lsf.queueInfoEnt_cu_type_exclusive_set
    __swig_getmethods__["cu_type_exclusive"] = _lsf.queueInfoEnt_cu_type_exclusive_get
    if _newclass:cu_type_exclusive = property(_lsf.queueInfoEnt_cu_type_exclusive_get, _lsf.queueInfoEnt_cu_type_exclusive_set)
    __swig_setmethods__["cu_str_exclusive"] = _lsf.queueInfoEnt_cu_str_exclusive_set
    __swig_getmethods__["cu_str_exclusive"] = _lsf.queueInfoEnt_cu_str_exclusive_get
    if _newclass:cu_str_exclusive = property(_lsf.queueInfoEnt_cu_str_exclusive_get, _lsf.queueInfoEnt_cu_str_exclusive_set)
    __swig_setmethods__["resRsvLimit"] = _lsf.queueInfoEnt_resRsvLimit_set
    __swig_getmethods__["resRsvLimit"] = _lsf.queueInfoEnt_resRsvLimit_get
    if _newclass:resRsvLimit = property(_lsf.queueInfoEnt_resRsvLimit_get, _lsf.queueInfoEnt_resRsvLimit_set)
    __swig_setmethods__["fairFactors"] = _lsf.queueInfoEnt_fairFactors_set
    __swig_getmethods__["fairFactors"] = _lsf.queueInfoEnt_fairFactors_get
    if _newclass:fairFactors = property(_lsf.queueInfoEnt_fairFactors_get, _lsf.queueInfoEnt_fairFactors_set)
    __swig_setmethods__["maxSlotsInPool"] = _lsf.queueInfoEnt_maxSlotsInPool_set
    __swig_getmethods__["maxSlotsInPool"] = _lsf.queueInfoEnt_maxSlotsInPool_get
    if _newclass:maxSlotsInPool = property(_lsf.queueInfoEnt_maxSlotsInPool_get, _lsf.queueInfoEnt_maxSlotsInPool_set)
    __swig_setmethods__["usePriorityInPool"] = _lsf.queueInfoEnt_usePriorityInPool_set
    __swig_getmethods__["usePriorityInPool"] = _lsf.queueInfoEnt_usePriorityInPool_get
    if _newclass:usePriorityInPool = property(_lsf.queueInfoEnt_usePriorityInPool_get, _lsf.queueInfoEnt_usePriorityInPool_set)
    __swig_setmethods__["noPreemptInterval"] = _lsf.queueInfoEnt_noPreemptInterval_set
    __swig_getmethods__["noPreemptInterval"] = _lsf.queueInfoEnt_noPreemptInterval_get
    if _newclass:noPreemptInterval = property(_lsf.queueInfoEnt_noPreemptInterval_get, _lsf.queueInfoEnt_noPreemptInterval_set)
    __swig_setmethods__["maxTotalTimePreempt"] = _lsf.queueInfoEnt_maxTotalTimePreempt_set
    __swig_getmethods__["maxTotalTimePreempt"] = _lsf.queueInfoEnt_maxTotalTimePreempt_get
    if _newclass:maxTotalTimePreempt = property(_lsf.queueInfoEnt_maxTotalTimePreempt_get, _lsf.queueInfoEnt_maxTotalTimePreempt_set)
    __swig_setmethods__["qAttrib2"] = _lsf.queueInfoEnt_qAttrib2_set
    __swig_getmethods__["qAttrib2"] = _lsf.queueInfoEnt_qAttrib2_get
    if _newclass:qAttrib2 = property(_lsf.queueInfoEnt_qAttrib2_get, _lsf.queueInfoEnt_qAttrib2_set)
    __swig_setmethods__["preemptDelayTime"] = _lsf.queueInfoEnt_preemptDelayTime_set
    __swig_getmethods__["preemptDelayTime"] = _lsf.queueInfoEnt_preemptDelayTime_get
    if _newclass:preemptDelayTime = property(_lsf.queueInfoEnt_preemptDelayTime_get, _lsf.queueInfoEnt_preemptDelayTime_set)
    def __init__(self, *args): 
        this = _lsf.new_queueInfoEnt(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _lsf.delete_queueInfoEnt
    __del__ = lambda self : None;
queueInfoEnt_swigregister = _lsf.queueInfoEnt_swigregister
queueInfoEnt_swigregister(queueInfoEnt)

ACT_NO = _lsf.ACT_NO
ACT_START = _lsf.ACT_START
ACT_PREEMPT = _lsf.ACT_PREEMPT
ACT_DONE = _lsf.ACT_DONE
ACT_FAIL = _lsf.ACT_FAIL
class hostInfoEnt(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, hostInfoEnt, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, hostInfoEnt, name)
    __repr__ = _swig_repr
    __swig_setmethods__["host"] = _lsf.hostInfoEnt_host_set
    __swig_getmethods__["host"] = _lsf.hostInfoEnt_host_get
    if _newclass:host = property(_lsf.hostInfoEnt_host_get, _lsf.hostInfoEnt_host_set)
    __swig_setmethods__["hStatus"] = _lsf.hostInfoEnt_hStatus_set
    __swig_getmethods__["hStatus"] = _lsf.hostInfoEnt_hStatus_get
    if _newclass:hStatus = property(_lsf.hostInfoEnt_hStatus_get, _lsf.hostInfoEnt_hStatus_set)
    __swig_setmethods__["busySched"] = _lsf.hostInfoEnt_busySched_set
    __swig_getmethods__["busySched"] = _lsf.hostInfoEnt_busySched_get
    if _newclass:busySched = property(_lsf.hostInfoEnt_busySched_get, _lsf.hostInfoEnt_busySched_set)
    __swig_setmethods__["busyStop"] = _lsf.hostInfoEnt_busyStop_set
    __swig_getmethods__["busyStop"] = _lsf.hostInfoEnt_busyStop_get
    if _newclass:busyStop = property(_lsf.hostInfoEnt_busyStop_get, _lsf.hostInfoEnt_busyStop_set)
    __swig_setmethods__["cpuFactor"] = _lsf.hostInfoEnt_cpuFactor_set
    __swig_getmethods__["cpuFactor"] = _lsf.hostInfoEnt_cpuFactor_get
    if _newclass:cpuFactor = property(_lsf.hostInfoEnt_cpuFactor_get, _lsf.hostInfoEnt_cpuFactor_set)
    __swig_setmethods__["nIdx"] = _lsf.hostInfoEnt_nIdx_set
    __swig_getmethods__["nIdx"] = _lsf.hostInfoEnt_nIdx_get
    if _newclass:nIdx = property(_lsf.hostInfoEnt_nIdx_get, _lsf.hostInfoEnt_nIdx_set)
    __swig_setmethods__["load"] = _lsf.hostInfoEnt_load_set
    __swig_getmethods__["load"] = _lsf.hostInfoEnt_load_get
    if _newclass:load = property(_lsf.hostInfoEnt_load_get, _lsf.hostInfoEnt_load_set)
    __swig_setmethods__["loadSched"] = _lsf.hostInfoEnt_loadSched_set
    __swig_getmethods__["loadSched"] = _lsf.hostInfoEnt_loadSched_get
    if _newclass:loadSched = property(_lsf.hostInfoEnt_loadSched_get, _lsf.hostInfoEnt_loadSched_set)
    __swig_setmethods__["loadStop"] = _lsf.hostInfoEnt_loadStop_set
    __swig_getmethods__["loadStop"] = _lsf.hostInfoEnt_loadStop_get
    if _newclass:loadStop = property(_lsf.hostInfoEnt_loadStop_get, _lsf.hostInfoEnt_loadStop_set)
    __swig_setmethods__["windows"] = _lsf.hostInfoEnt_windows_set
    __swig_getmethods__["windows"] = _lsf.hostInfoEnt_windows_get
    if _newclass:windows = property(_lsf.hostInfoEnt_windows_get, _lsf.hostInfoEnt_windows_set)
    __swig_setmethods__["userJobLimit"] = _lsf.hostInfoEnt_userJobLimit_set
    __swig_getmethods__["userJobLimit"] = _lsf.hostInfoEnt_userJobLimit_get
    if _newclass:userJobLimit = property(_lsf.hostInfoEnt_userJobLimit_get, _lsf.hostInfoEnt_userJobLimit_set)
    __swig_setmethods__["maxJobs"] = _lsf.hostInfoEnt_maxJobs_set
    __swig_getmethods__["maxJobs"] = _lsf.hostInfoEnt_maxJobs_get
    if _newclass:maxJobs = property(_lsf.hostInfoEnt_maxJobs_get, _lsf.hostInfoEnt_maxJobs_set)
    __swig_setmethods__["numJobs"] = _lsf.hostInfoEnt_numJobs_set
    __swig_getmethods__["numJobs"] = _lsf.hostInfoEnt_numJobs_get
    if _newclass:numJobs = property(_lsf.hostInfoEnt_numJobs_get, _lsf.hostInfoEnt_numJobs_set)
    __swig_setmethods__["numRUN"] = _lsf.hostInfoEnt_numRUN_set
    __swig_getmethods__["numRUN"] = _lsf.hostInfoEnt_numRUN_get
    if _newclass:numRUN = property(_lsf.hostInfoEnt_numRUN_get, _lsf.hostInfoEnt_numRUN_set)
    __swig_setmethods__["numSSUSP"] = _lsf.hostInfoEnt_numSSUSP_set
    __swig_getmethods__["numSSUSP"] = _lsf.hostInfoEnt_numSSUSP_get
    if _newclass:numSSUSP = property(_lsf.hostInfoEnt_numSSUSP_get, _lsf.hostInfoEnt_numSSUSP_set)
    __swig_setmethods__["numUSUSP"] = _lsf.hostInfoEnt_numUSUSP_set
    __swig_getmethods__["numUSUSP"] = _lsf.hostInfoEnt_numUSUSP_get
    if _newclass:numUSUSP = property(_lsf.hostInfoEnt_numUSUSP_get, _lsf.hostInfoEnt_numUSUSP_set)
    __swig_setmethods__["mig"] = _lsf.hostInfoEnt_mig_set
    __swig_getmethods__["mig"] = _lsf.hostInfoEnt_mig_get
    if _newclass:mig = property(_lsf.hostInfoEnt_mig_get, _lsf.hostInfoEnt_mig_set)
    __swig_setmethods__["attr"] = _lsf.hostInfoEnt_attr_set
    __swig_getmethods__["attr"] = _lsf.hostInfoEnt_attr_get
    if _newclass:attr = property(_lsf.hostInfoEnt_attr_get, _lsf.hostInfoEnt_attr_set)
    __swig_setmethods__["realLoad"] = _lsf.hostInfoEnt_realLoad_set
    __swig_getmethods__["realLoad"] = _lsf.hostInfoEnt_realLoad_get
    if _newclass:realLoad = property(_lsf.hostInfoEnt_realLoad_get, _lsf.hostInfoEnt_realLoad_set)
    __swig_setmethods__["numRESERVE"] = _lsf.hostInfoEnt_numRESERVE_set
    __swig_getmethods__["numRESERVE"] = _lsf.hostInfoEnt_numRESERVE_get
    if _newclass:numRESERVE = property(_lsf.hostInfoEnt_numRESERVE_get, _lsf.hostInfoEnt_numRESERVE_set)
    __swig_setmethods__["chkSig"] = _lsf.hostInfoEnt_chkSig_set
    __swig_getmethods__["chkSig"] = _lsf.hostInfoEnt_chkSig_get
    if _newclass:chkSig = property(_lsf.hostInfoEnt_chkSig_get, _lsf.hostInfoEnt_chkSig_set)
    __swig_setmethods__["cnsmrUsage"] = _lsf.hostInfoEnt_cnsmrUsage_set
    __swig_getmethods__["cnsmrUsage"] = _lsf.hostInfoEnt_cnsmrUsage_get
    if _newclass:cnsmrUsage = property(_lsf.hostInfoEnt_cnsmrUsage_get, _lsf.hostInfoEnt_cnsmrUsage_set)
    __swig_setmethods__["prvdrUsage"] = _lsf.hostInfoEnt_prvdrUsage_set
    __swig_getmethods__["prvdrUsage"] = _lsf.hostInfoEnt_prvdrUsage_get
    if _newclass:prvdrUsage = property(_lsf.hostInfoEnt_prvdrUsage_get, _lsf.hostInfoEnt_prvdrUsage_set)
    __swig_setmethods__["cnsmrAvail"] = _lsf.hostInfoEnt_cnsmrAvail_set
    __swig_getmethods__["cnsmrAvail"] = _lsf.hostInfoEnt_cnsmrAvail_get
    if _newclass:cnsmrAvail = property(_lsf.hostInfoEnt_cnsmrAvail_get, _lsf.hostInfoEnt_cnsmrAvail_set)
    __swig_setmethods__["prvdrAvail"] = _lsf.hostInfoEnt_prvdrAvail_set
    __swig_getmethods__["prvdrAvail"] = _lsf.hostInfoEnt_prvdrAvail_get
    if _newclass:prvdrAvail = property(_lsf.hostInfoEnt_prvdrAvail_get, _lsf.hostInfoEnt_prvdrAvail_set)
    __swig_setmethods__["maxAvail"] = _lsf.hostInfoEnt_maxAvail_set
    __swig_getmethods__["maxAvail"] = _lsf.hostInfoEnt_maxAvail_get
    if _newclass:maxAvail = property(_lsf.hostInfoEnt_maxAvail_get, _lsf.hostInfoEnt_maxAvail_set)
    __swig_setmethods__["maxExitRate"] = _lsf.hostInfoEnt_maxExitRate_set
    __swig_getmethods__["maxExitRate"] = _lsf.hostInfoEnt_maxExitRate_get
    if _newclass:maxExitRate = property(_lsf.hostInfoEnt_maxExitRate_get, _lsf.hostInfoEnt_maxExitRate_set)
    __swig_setmethods__["numExitRate"] = _lsf.hostInfoEnt_numExitRate_set
    __swig_getmethods__["numExitRate"] = _lsf.hostInfoEnt_numExitRate_get
    if _newclass:numExitRate = property(_lsf.hostInfoEnt_numExitRate_get, _lsf.hostInfoEnt_numExitRate_set)
    __swig_setmethods__["hCtrlMsg"] = _lsf.hostInfoEnt_hCtrlMsg_set
    __swig_getmethods__["hCtrlMsg"] = _lsf.hostInfoEnt_hCtrlMsg_get
    if _newclass:hCtrlMsg = property(_lsf.hostInfoEnt_hCtrlMsg_get, _lsf.hostInfoEnt_hCtrlMsg_set)
    def __init__(self, *args): 
        this = _lsf.new_hostInfoEnt(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _lsf.delete_hostInfoEnt
    __del__ = lambda self : None;
hostInfoEnt_swigregister = _lsf.hostInfoEnt_swigregister
hostInfoEnt_swigregister(hostInfoEnt)
H_ATTR_CHKPNTABLE = _lsf.H_ATTR_CHKPNTABLE
H_ATTR_CHKPNT_COPY = _lsf.H_ATTR_CHKPNT_COPY

class condHostInfoEnt(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, condHostInfoEnt, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, condHostInfoEnt, name)
    __repr__ = _swig_repr
    __swig_setmethods__["name"] = _lsf.condHostInfoEnt_name_set
    __swig_getmethods__["name"] = _lsf.condHostInfoEnt_name_get
    if _newclass:name = property(_lsf.condHostInfoEnt_name_get, _lsf.condHostInfoEnt_name_set)
    __swig_setmethods__["howManyOk"] = _lsf.condHostInfoEnt_howManyOk_set
    __swig_getmethods__["howManyOk"] = _lsf.condHostInfoEnt_howManyOk_get
    if _newclass:howManyOk = property(_lsf.condHostInfoEnt_howManyOk_get, _lsf.condHostInfoEnt_howManyOk_set)
    __swig_setmethods__["howManyBusy"] = _lsf.condHostInfoEnt_howManyBusy_set
    __swig_getmethods__["howManyBusy"] = _lsf.condHostInfoEnt_howManyBusy_get
    if _newclass:howManyBusy = property(_lsf.condHostInfoEnt_howManyBusy_get, _lsf.condHostInfoEnt_howManyBusy_set)
    __swig_setmethods__["howManyClosed"] = _lsf.condHostInfoEnt_howManyClosed_set
    __swig_getmethods__["howManyClosed"] = _lsf.condHostInfoEnt_howManyClosed_get
    if _newclass:howManyClosed = property(_lsf.condHostInfoEnt_howManyClosed_get, _lsf.condHostInfoEnt_howManyClosed_set)
    __swig_setmethods__["howManyFull"] = _lsf.condHostInfoEnt_howManyFull_set
    __swig_getmethods__["howManyFull"] = _lsf.condHostInfoEnt_howManyFull_get
    if _newclass:howManyFull = property(_lsf.condHostInfoEnt_howManyFull_get, _lsf.condHostInfoEnt_howManyFull_set)
    __swig_setmethods__["howManyUnreach"] = _lsf.condHostInfoEnt_howManyUnreach_set
    __swig_getmethods__["howManyUnreach"] = _lsf.condHostInfoEnt_howManyUnreach_get
    if _newclass:howManyUnreach = property(_lsf.condHostInfoEnt_howManyUnreach_get, _lsf.condHostInfoEnt_howManyUnreach_set)
    __swig_setmethods__["howManyUnavail"] = _lsf.condHostInfoEnt_howManyUnavail_set
    __swig_getmethods__["howManyUnavail"] = _lsf.condHostInfoEnt_howManyUnavail_get
    if _newclass:howManyUnavail = property(_lsf.condHostInfoEnt_howManyUnavail_get, _lsf.condHostInfoEnt_howManyUnavail_set)
    __swig_setmethods__["hostInfo"] = _lsf.condHostInfoEnt_hostInfo_set
    __swig_getmethods__["hostInfo"] = _lsf.condHostInfoEnt_hostInfo_get
    if _newclass:hostInfo = property(_lsf.condHostInfoEnt_hostInfo_get, _lsf.condHostInfoEnt_hostInfo_set)
    def __init__(self, *args): 
        this = _lsf.new_condHostInfoEnt(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _lsf.delete_condHostInfoEnt
    __del__ = lambda self : None;
condHostInfoEnt_swigregister = _lsf.condHostInfoEnt_swigregister
condHostInfoEnt_swigregister(condHostInfoEnt)

class adjustParam(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, adjustParam, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, adjustParam, name)
    __repr__ = _swig_repr
    __swig_setmethods__["key"] = _lsf.adjustParam_key_set
    __swig_getmethods__["key"] = _lsf.adjustParam_key_get
    if _newclass:key = property(_lsf.adjustParam_key_get, _lsf.adjustParam_key_set)
    __swig_setmethods__["value"] = _lsf.adjustParam_value_set
    __swig_getmethods__["value"] = _lsf.adjustParam_value_get
    if _newclass:value = property(_lsf.adjustParam_value_get, _lsf.adjustParam_value_set)
    def __init__(self, *args): 
        this = _lsf.new_adjustParam(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _lsf.delete_adjustParam
    __del__ = lambda self : None;
adjustParam_swigregister = _lsf.adjustParam_swigregister
adjustParam_swigregister(adjustParam)

FAIR_ADJUST_CPU_TIME_FACTOR = _lsf.FAIR_ADJUST_CPU_TIME_FACTOR
FAIR_ADJUST_RUN_TIME_FACTOR = _lsf.FAIR_ADJUST_RUN_TIME_FACTOR
FAIR_ADJUST_RUN_JOB_FACTOR = _lsf.FAIR_ADJUST_RUN_JOB_FACTOR
FAIR_ADJUST_COMMITTED_RUN_TIME_FACTOR = _lsf.FAIR_ADJUST_COMMITTED_RUN_TIME_FACTOR
FAIR_ADJUST_ENABLE_HIST_RUN_TIME = _lsf.FAIR_ADJUST_ENABLE_HIST_RUN_TIME
FAIR_ADJUST_HIST_CPU_TIME = _lsf.FAIR_ADJUST_HIST_CPU_TIME
FAIR_ADJUST_NEW_USED_CPU_TIME = _lsf.FAIR_ADJUST_NEW_USED_CPU_TIME
FAIR_ADJUST_RUN_TIME = _lsf.FAIR_ADJUST_RUN_TIME
FAIR_ADJUST_HIST_RUN_TIME = _lsf.FAIR_ADJUST_HIST_RUN_TIME
FAIR_ADJUST_COMMITTED_RUN_TIME = _lsf.FAIR_ADJUST_COMMITTED_RUN_TIME
FAIR_ADJUST_NUM_START_JOBS = _lsf.FAIR_ADJUST_NUM_START_JOBS
FAIR_ADJUST_NUM_RESERVE_JOBS = _lsf.FAIR_ADJUST_NUM_RESERVE_JOBS
FAIR_ADJUST_MEM_USED = _lsf.FAIR_ADJUST_MEM_USED
FAIR_ADJUST_MEM_ALLOCATED = _lsf.FAIR_ADJUST_MEM_ALLOCATED
FAIR_ADJUST_ENABLE_RUN_TIME_DECAY = _lsf.FAIR_ADJUST_ENABLE_RUN_TIME_DECAY
FAIR_ADJUST_DECAYED_RUN_TIME = _lsf.FAIR_ADJUST_DECAYED_RUN_TIME
FAIR_ADJUST_KVPS_SUM = _lsf.FAIR_ADJUST_KVPS_SUM
class shareAdjustPair(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, shareAdjustPair, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, shareAdjustPair, name)
    __repr__ = _swig_repr
    __swig_setmethods__["shareAcctType"] = _lsf.shareAdjustPair_shareAcctType_set
    __swig_getmethods__["shareAcctType"] = _lsf.shareAdjustPair_shareAcctType_get
    if _newclass:shareAcctType = property(_lsf.shareAdjustPair_shareAcctType_get, _lsf.shareAdjustPair_shareAcctType_set)
    __swig_setmethods__["holderName"] = _lsf.shareAdjustPair_holderName_set
    __swig_getmethods__["holderName"] = _lsf.shareAdjustPair_holderName_get
    if _newclass:holderName = property(_lsf.shareAdjustPair_holderName_get, _lsf.shareAdjustPair_holderName_set)
    __swig_setmethods__["providerName"] = _lsf.shareAdjustPair_providerName_set
    __swig_getmethods__["providerName"] = _lsf.shareAdjustPair_providerName_get
    if _newclass:providerName = property(_lsf.shareAdjustPair_providerName_get, _lsf.shareAdjustPair_providerName_set)
    __swig_setmethods__["numPair"] = _lsf.shareAdjustPair_numPair_set
    __swig_getmethods__["numPair"] = _lsf.shareAdjustPair_numPair_get
    if _newclass:numPair = property(_lsf.shareAdjustPair_numPair_get, _lsf.shareAdjustPair_numPair_set)
    __swig_setmethods__["adjustParam"] = _lsf.shareAdjustPair_adjustParam_set
    __swig_getmethods__["adjustParam"] = _lsf.shareAdjustPair_adjustParam_get
    if _newclass:adjustParam = property(_lsf.shareAdjustPair_adjustParam_get, _lsf.shareAdjustPair_adjustParam_set)
    def __init__(self, *args): 
        this = _lsf.new_shareAdjustPair(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _lsf.delete_shareAdjustPair
    __del__ = lambda self : None;
shareAdjustPair_swigregister = _lsf.shareAdjustPair_swigregister
shareAdjustPair_swigregister(shareAdjustPair)
SHAREACCTTYPEQUEUE = _lsf.SHAREACCTTYPEQUEUE
SHAREACCTTYPEHP = _lsf.SHAREACCTTYPEHP
SHAREACCTTYPESLA = _lsf.SHAREACCTTYPESLA

fairshare_adjustment = _lsf.fairshare_adjustment
class hostPartUserInfo(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, hostPartUserInfo, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, hostPartUserInfo, name)
    __repr__ = _swig_repr
    __swig_setmethods__["user"] = _lsf.hostPartUserInfo_user_set
    __swig_getmethods__["user"] = _lsf.hostPartUserInfo_user_get
    if _newclass:user = property(_lsf.hostPartUserInfo_user_get, _lsf.hostPartUserInfo_user_set)
    __swig_setmethods__["shares"] = _lsf.hostPartUserInfo_shares_set
    __swig_getmethods__["shares"] = _lsf.hostPartUserInfo_shares_get
    if _newclass:shares = property(_lsf.hostPartUserInfo_shares_get, _lsf.hostPartUserInfo_shares_set)
    __swig_setmethods__["priority"] = _lsf.hostPartUserInfo_priority_set
    __swig_getmethods__["priority"] = _lsf.hostPartUserInfo_priority_get
    if _newclass:priority = property(_lsf.hostPartUserInfo_priority_get, _lsf.hostPartUserInfo_priority_set)
    __swig_setmethods__["numStartJobs"] = _lsf.hostPartUserInfo_numStartJobs_set
    __swig_getmethods__["numStartJobs"] = _lsf.hostPartUserInfo_numStartJobs_get
    if _newclass:numStartJobs = property(_lsf.hostPartUserInfo_numStartJobs_get, _lsf.hostPartUserInfo_numStartJobs_set)
    __swig_setmethods__["histCpuTime"] = _lsf.hostPartUserInfo_histCpuTime_set
    __swig_getmethods__["histCpuTime"] = _lsf.hostPartUserInfo_histCpuTime_get
    if _newclass:histCpuTime = property(_lsf.hostPartUserInfo_histCpuTime_get, _lsf.hostPartUserInfo_histCpuTime_set)
    __swig_setmethods__["numReserveJobs"] = _lsf.hostPartUserInfo_numReserveJobs_set
    __swig_getmethods__["numReserveJobs"] = _lsf.hostPartUserInfo_numReserveJobs_get
    if _newclass:numReserveJobs = property(_lsf.hostPartUserInfo_numReserveJobs_get, _lsf.hostPartUserInfo_numReserveJobs_set)
    __swig_setmethods__["runTime"] = _lsf.hostPartUserInfo_runTime_set
    __swig_getmethods__["runTime"] = _lsf.hostPartUserInfo_runTime_get
    if _newclass:runTime = property(_lsf.hostPartUserInfo_runTime_get, _lsf.hostPartUserInfo_runTime_set)
    __swig_setmethods__["shareAdjustment"] = _lsf.hostPartUserInfo_shareAdjustment_set
    __swig_getmethods__["shareAdjustment"] = _lsf.hostPartUserInfo_shareAdjustment_get
    if _newclass:shareAdjustment = property(_lsf.hostPartUserInfo_shareAdjustment_get, _lsf.hostPartUserInfo_shareAdjustment_set)
    def __init__(self, *args): 
        this = _lsf.new_hostPartUserInfo(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _lsf.delete_hostPartUserInfo
    __del__ = lambda self : None;
hostPartUserInfo_swigregister = _lsf.hostPartUserInfo_swigregister
hostPartUserInfo_swigregister(hostPartUserInfo)

class hostPartInfoEnt(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, hostPartInfoEnt, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, hostPartInfoEnt, name)
    __repr__ = _swig_repr
    __swig_setmethods__["hostPart"] = _lsf.hostPartInfoEnt_hostPart_set
    __swig_getmethods__["hostPart"] = _lsf.hostPartInfoEnt_hostPart_get
    if _newclass:hostPart = property(_lsf.hostPartInfoEnt_hostPart_get, _lsf.hostPartInfoEnt_hostPart_set)
    __swig_setmethods__["hostList"] = _lsf.hostPartInfoEnt_hostList_set
    __swig_getmethods__["hostList"] = _lsf.hostPartInfoEnt_hostList_get
    if _newclass:hostList = property(_lsf.hostPartInfoEnt_hostList_get, _lsf.hostPartInfoEnt_hostList_set)
    __swig_setmethods__["numUsers"] = _lsf.hostPartInfoEnt_numUsers_set
    __swig_getmethods__["numUsers"] = _lsf.hostPartInfoEnt_numUsers_get
    if _newclass:numUsers = property(_lsf.hostPartInfoEnt_numUsers_get, _lsf.hostPartInfoEnt_numUsers_set)
    __swig_setmethods__["users"] = _lsf.hostPartInfoEnt_users_set
    __swig_getmethods__["users"] = _lsf.hostPartInfoEnt_users_get
    if _newclass:users = property(_lsf.hostPartInfoEnt_users_get, _lsf.hostPartInfoEnt_users_set)
    __swig_setmethods__["hostStr"] = _lsf.hostPartInfoEnt_hostStr_set
    __swig_getmethods__["hostStr"] = _lsf.hostPartInfoEnt_hostStr_get
    if _newclass:hostStr = property(_lsf.hostPartInfoEnt_hostStr_get, _lsf.hostPartInfoEnt_hostStr_set)
    def __init__(self, *args): 
        this = _lsf.new_hostPartInfoEnt(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _lsf.delete_hostPartInfoEnt
    __del__ = lambda self : None;
hostPartInfoEnt_swigregister = _lsf.hostPartInfoEnt_swigregister
hostPartInfoEnt_swigregister(hostPartInfoEnt)

class shareAcctInfoEnt(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, shareAcctInfoEnt, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, shareAcctInfoEnt, name)
    __repr__ = _swig_repr
    __swig_setmethods__["shareAcctPath"] = _lsf.shareAcctInfoEnt_shareAcctPath_set
    __swig_getmethods__["shareAcctPath"] = _lsf.shareAcctInfoEnt_shareAcctPath_get
    if _newclass:shareAcctPath = property(_lsf.shareAcctInfoEnt_shareAcctPath_get, _lsf.shareAcctInfoEnt_shareAcctPath_set)
    __swig_setmethods__["shares"] = _lsf.shareAcctInfoEnt_shares_set
    __swig_getmethods__["shares"] = _lsf.shareAcctInfoEnt_shares_get
    if _newclass:shares = property(_lsf.shareAcctInfoEnt_shares_get, _lsf.shareAcctInfoEnt_shares_set)
    __swig_setmethods__["priority"] = _lsf.shareAcctInfoEnt_priority_set
    __swig_getmethods__["priority"] = _lsf.shareAcctInfoEnt_priority_get
    if _newclass:priority = property(_lsf.shareAcctInfoEnt_priority_get, _lsf.shareAcctInfoEnt_priority_set)
    __swig_setmethods__["numStartJobs"] = _lsf.shareAcctInfoEnt_numStartJobs_set
    __swig_getmethods__["numStartJobs"] = _lsf.shareAcctInfoEnt_numStartJobs_get
    if _newclass:numStartJobs = property(_lsf.shareAcctInfoEnt_numStartJobs_get, _lsf.shareAcctInfoEnt_numStartJobs_set)
    __swig_setmethods__["histCpuTime"] = _lsf.shareAcctInfoEnt_histCpuTime_set
    __swig_getmethods__["histCpuTime"] = _lsf.shareAcctInfoEnt_histCpuTime_get
    if _newclass:histCpuTime = property(_lsf.shareAcctInfoEnt_histCpuTime_get, _lsf.shareAcctInfoEnt_histCpuTime_set)
    __swig_setmethods__["numReserveJobs"] = _lsf.shareAcctInfoEnt_numReserveJobs_set
    __swig_getmethods__["numReserveJobs"] = _lsf.shareAcctInfoEnt_numReserveJobs_get
    if _newclass:numReserveJobs = property(_lsf.shareAcctInfoEnt_numReserveJobs_get, _lsf.shareAcctInfoEnt_numReserveJobs_set)
    __swig_setmethods__["runTime"] = _lsf.shareAcctInfoEnt_runTime_set
    __swig_getmethods__["runTime"] = _lsf.shareAcctInfoEnt_runTime_get
    if _newclass:runTime = property(_lsf.shareAcctInfoEnt_runTime_get, _lsf.shareAcctInfoEnt_runTime_set)
    __swig_setmethods__["shareAdjustment"] = _lsf.shareAcctInfoEnt_shareAdjustment_set
    __swig_getmethods__["shareAdjustment"] = _lsf.shareAcctInfoEnt_shareAdjustment_get
    if _newclass:shareAdjustment = property(_lsf.shareAcctInfoEnt_shareAdjustment_get, _lsf.shareAcctInfoEnt_shareAdjustment_set)
    def __init__(self, *args): 
        this = _lsf.new_shareAcctInfoEnt(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _lsf.delete_shareAcctInfoEnt
    __del__ = lambda self : None;
shareAcctInfoEnt_swigregister = _lsf.shareAcctInfoEnt_swigregister
shareAcctInfoEnt_swigregister(shareAcctInfoEnt)

DEF_MAX_JOBID = _lsf.DEF_MAX_JOBID
MAX_JOBID_LOW = _lsf.MAX_JOBID_LOW
MAX_JOBID_HIGH = _lsf.MAX_JOBID_HIGH
DEF_PREEMPTION_WAIT_TIME = _lsf.DEF_PREEMPTION_WAIT_TIME
DEF_MAX_ASKED_HOSTS = _lsf.DEF_MAX_ASKED_HOSTS
class parameterInfo(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, parameterInfo, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, parameterInfo, name)
    __repr__ = _swig_repr
    __swig_setmethods__["defaultQueues"] = _lsf.parameterInfo_defaultQueues_set
    __swig_getmethods__["defaultQueues"] = _lsf.parameterInfo_defaultQueues_get
    if _newclass:defaultQueues = property(_lsf.parameterInfo_defaultQueues_get, _lsf.parameterInfo_defaultQueues_set)
    __swig_setmethods__["defaultHostSpec"] = _lsf.parameterInfo_defaultHostSpec_set
    __swig_getmethods__["defaultHostSpec"] = _lsf.parameterInfo_defaultHostSpec_get
    if _newclass:defaultHostSpec = property(_lsf.parameterInfo_defaultHostSpec_get, _lsf.parameterInfo_defaultHostSpec_set)
    __swig_setmethods__["mbatchdInterval"] = _lsf.parameterInfo_mbatchdInterval_set
    __swig_getmethods__["mbatchdInterval"] = _lsf.parameterInfo_mbatchdInterval_get
    if _newclass:mbatchdInterval = property(_lsf.parameterInfo_mbatchdInterval_get, _lsf.parameterInfo_mbatchdInterval_set)
    __swig_setmethods__["sbatchdInterval"] = _lsf.parameterInfo_sbatchdInterval_set
    __swig_getmethods__["sbatchdInterval"] = _lsf.parameterInfo_sbatchdInterval_get
    if _newclass:sbatchdInterval = property(_lsf.parameterInfo_sbatchdInterval_get, _lsf.parameterInfo_sbatchdInterval_set)
    __swig_setmethods__["jobAcceptInterval"] = _lsf.parameterInfo_jobAcceptInterval_set
    __swig_getmethods__["jobAcceptInterval"] = _lsf.parameterInfo_jobAcceptInterval_get
    if _newclass:jobAcceptInterval = property(_lsf.parameterInfo_jobAcceptInterval_get, _lsf.parameterInfo_jobAcceptInterval_set)
    __swig_setmethods__["maxDispRetries"] = _lsf.parameterInfo_maxDispRetries_set
    __swig_getmethods__["maxDispRetries"] = _lsf.parameterInfo_maxDispRetries_get
    if _newclass:maxDispRetries = property(_lsf.parameterInfo_maxDispRetries_get, _lsf.parameterInfo_maxDispRetries_set)
    __swig_setmethods__["maxSbdRetries"] = _lsf.parameterInfo_maxSbdRetries_set
    __swig_getmethods__["maxSbdRetries"] = _lsf.parameterInfo_maxSbdRetries_get
    if _newclass:maxSbdRetries = property(_lsf.parameterInfo_maxSbdRetries_get, _lsf.parameterInfo_maxSbdRetries_set)
    __swig_setmethods__["preemptPeriod"] = _lsf.parameterInfo_preemptPeriod_set
    __swig_getmethods__["preemptPeriod"] = _lsf.parameterInfo_preemptPeriod_get
    if _newclass:preemptPeriod = property(_lsf.parameterInfo_preemptPeriod_get, _lsf.parameterInfo_preemptPeriod_set)
    __swig_setmethods__["cleanPeriod"] = _lsf.parameterInfo_cleanPeriod_set
    __swig_getmethods__["cleanPeriod"] = _lsf.parameterInfo_cleanPeriod_get
    if _newclass:cleanPeriod = property(_lsf.parameterInfo_cleanPeriod_get, _lsf.parameterInfo_cleanPeriod_set)
    __swig_setmethods__["maxNumJobs"] = _lsf.parameterInfo_maxNumJobs_set
    __swig_getmethods__["maxNumJobs"] = _lsf.parameterInfo_maxNumJobs_get
    if _newclass:maxNumJobs = property(_lsf.parameterInfo_maxNumJobs_get, _lsf.parameterInfo_maxNumJobs_set)
    __swig_setmethods__["historyHours"] = _lsf.parameterInfo_historyHours_set
    __swig_getmethods__["historyHours"] = _lsf.parameterInfo_historyHours_get
    if _newclass:historyHours = property(_lsf.parameterInfo_historyHours_get, _lsf.parameterInfo_historyHours_set)
    __swig_setmethods__["pgSuspendIt"] = _lsf.parameterInfo_pgSuspendIt_set
    __swig_getmethods__["pgSuspendIt"] = _lsf.parameterInfo_pgSuspendIt_get
    if _newclass:pgSuspendIt = property(_lsf.parameterInfo_pgSuspendIt_get, _lsf.parameterInfo_pgSuspendIt_set)
    __swig_setmethods__["defaultProject"] = _lsf.parameterInfo_defaultProject_set
    __swig_getmethods__["defaultProject"] = _lsf.parameterInfo_defaultProject_get
    if _newclass:defaultProject = property(_lsf.parameterInfo_defaultProject_get, _lsf.parameterInfo_defaultProject_set)
    __swig_setmethods__["retryIntvl"] = _lsf.parameterInfo_retryIntvl_set
    __swig_getmethods__["retryIntvl"] = _lsf.parameterInfo_retryIntvl_get
    if _newclass:retryIntvl = property(_lsf.parameterInfo_retryIntvl_get, _lsf.parameterInfo_retryIntvl_set)
    __swig_setmethods__["nqsQueuesFlags"] = _lsf.parameterInfo_nqsQueuesFlags_set
    __swig_getmethods__["nqsQueuesFlags"] = _lsf.parameterInfo_nqsQueuesFlags_get
    if _newclass:nqsQueuesFlags = property(_lsf.parameterInfo_nqsQueuesFlags_get, _lsf.parameterInfo_nqsQueuesFlags_set)
    __swig_setmethods__["nqsRequestsFlags"] = _lsf.parameterInfo_nqsRequestsFlags_set
    __swig_getmethods__["nqsRequestsFlags"] = _lsf.parameterInfo_nqsRequestsFlags_get
    if _newclass:nqsRequestsFlags = property(_lsf.parameterInfo_nqsRequestsFlags_get, _lsf.parameterInfo_nqsRequestsFlags_set)
    __swig_setmethods__["maxPreExecRetry"] = _lsf.parameterInfo_maxPreExecRetry_set
    __swig_getmethods__["maxPreExecRetry"] = _lsf.parameterInfo_maxPreExecRetry_get
    if _newclass:maxPreExecRetry = property(_lsf.parameterInfo_maxPreExecRetry_get, _lsf.parameterInfo_maxPreExecRetry_set)
    __swig_setmethods__["localMaxPreExecRetry"] = _lsf.parameterInfo_localMaxPreExecRetry_set
    __swig_getmethods__["localMaxPreExecRetry"] = _lsf.parameterInfo_localMaxPreExecRetry_get
    if _newclass:localMaxPreExecRetry = property(_lsf.parameterInfo_localMaxPreExecRetry_get, _lsf.parameterInfo_localMaxPreExecRetry_set)
    __swig_setmethods__["eventWatchTime"] = _lsf.parameterInfo_eventWatchTime_set
    __swig_getmethods__["eventWatchTime"] = _lsf.parameterInfo_eventWatchTime_get
    if _newclass:eventWatchTime = property(_lsf.parameterInfo_eventWatchTime_get, _lsf.parameterInfo_eventWatchTime_set)
    __swig_setmethods__["runTimeFactor"] = _lsf.parameterInfo_runTimeFactor_set
    __swig_getmethods__["runTimeFactor"] = _lsf.parameterInfo_runTimeFactor_get
    if _newclass:runTimeFactor = property(_lsf.parameterInfo_runTimeFactor_get, _lsf.parameterInfo_runTimeFactor_set)
    __swig_setmethods__["waitTimeFactor"] = _lsf.parameterInfo_waitTimeFactor_set
    __swig_getmethods__["waitTimeFactor"] = _lsf.parameterInfo_waitTimeFactor_get
    if _newclass:waitTimeFactor = property(_lsf.parameterInfo_waitTimeFactor_get, _lsf.parameterInfo_waitTimeFactor_set)
    __swig_setmethods__["runJobFactor"] = _lsf.parameterInfo_runJobFactor_set
    __swig_getmethods__["runJobFactor"] = _lsf.parameterInfo_runJobFactor_get
    if _newclass:runJobFactor = property(_lsf.parameterInfo_runJobFactor_get, _lsf.parameterInfo_runJobFactor_set)
    __swig_setmethods__["eEventCheckIntvl"] = _lsf.parameterInfo_eEventCheckIntvl_set
    __swig_getmethods__["eEventCheckIntvl"] = _lsf.parameterInfo_eEventCheckIntvl_get
    if _newclass:eEventCheckIntvl = property(_lsf.parameterInfo_eEventCheckIntvl_get, _lsf.parameterInfo_eEventCheckIntvl_set)
    __swig_setmethods__["rusageUpdateRate"] = _lsf.parameterInfo_rusageUpdateRate_set
    __swig_getmethods__["rusageUpdateRate"] = _lsf.parameterInfo_rusageUpdateRate_get
    if _newclass:rusageUpdateRate = property(_lsf.parameterInfo_rusageUpdateRate_get, _lsf.parameterInfo_rusageUpdateRate_set)
    __swig_setmethods__["rusageUpdatePercent"] = _lsf.parameterInfo_rusageUpdatePercent_set
    __swig_getmethods__["rusageUpdatePercent"] = _lsf.parameterInfo_rusageUpdatePercent_get
    if _newclass:rusageUpdatePercent = property(_lsf.parameterInfo_rusageUpdatePercent_get, _lsf.parameterInfo_rusageUpdatePercent_set)
    __swig_setmethods__["condCheckTime"] = _lsf.parameterInfo_condCheckTime_set
    __swig_getmethods__["condCheckTime"] = _lsf.parameterInfo_condCheckTime_get
    if _newclass:condCheckTime = property(_lsf.parameterInfo_condCheckTime_get, _lsf.parameterInfo_condCheckTime_set)
    __swig_setmethods__["maxSbdConnections"] = _lsf.parameterInfo_maxSbdConnections_set
    __swig_getmethods__["maxSbdConnections"] = _lsf.parameterInfo_maxSbdConnections_get
    if _newclass:maxSbdConnections = property(_lsf.parameterInfo_maxSbdConnections_get, _lsf.parameterInfo_maxSbdConnections_set)
    __swig_setmethods__["rschedInterval"] = _lsf.parameterInfo_rschedInterval_set
    __swig_getmethods__["rschedInterval"] = _lsf.parameterInfo_rschedInterval_get
    if _newclass:rschedInterval = property(_lsf.parameterInfo_rschedInterval_get, _lsf.parameterInfo_rschedInterval_set)
    __swig_setmethods__["maxSchedStay"] = _lsf.parameterInfo_maxSchedStay_set
    __swig_getmethods__["maxSchedStay"] = _lsf.parameterInfo_maxSchedStay_get
    if _newclass:maxSchedStay = property(_lsf.parameterInfo_maxSchedStay_get, _lsf.parameterInfo_maxSchedStay_set)
    __swig_setmethods__["freshPeriod"] = _lsf.parameterInfo_freshPeriod_set
    __swig_getmethods__["freshPeriod"] = _lsf.parameterInfo_freshPeriod_get
    if _newclass:freshPeriod = property(_lsf.parameterInfo_freshPeriod_get, _lsf.parameterInfo_freshPeriod_set)
    __swig_setmethods__["preemptFor"] = _lsf.parameterInfo_preemptFor_set
    __swig_getmethods__["preemptFor"] = _lsf.parameterInfo_preemptFor_get
    if _newclass:preemptFor = property(_lsf.parameterInfo_preemptFor_get, _lsf.parameterInfo_preemptFor_set)
    __swig_setmethods__["adminSuspend"] = _lsf.parameterInfo_adminSuspend_set
    __swig_getmethods__["adminSuspend"] = _lsf.parameterInfo_adminSuspend_get
    if _newclass:adminSuspend = property(_lsf.parameterInfo_adminSuspend_get, _lsf.parameterInfo_adminSuspend_set)
    __swig_setmethods__["userReservation"] = _lsf.parameterInfo_userReservation_set
    __swig_getmethods__["userReservation"] = _lsf.parameterInfo_userReservation_get
    if _newclass:userReservation = property(_lsf.parameterInfo_userReservation_get, _lsf.parameterInfo_userReservation_set)
    __swig_setmethods__["cpuTimeFactor"] = _lsf.parameterInfo_cpuTimeFactor_set
    __swig_getmethods__["cpuTimeFactor"] = _lsf.parameterInfo_cpuTimeFactor_get
    if _newclass:cpuTimeFactor = property(_lsf.parameterInfo_cpuTimeFactor_get, _lsf.parameterInfo_cpuTimeFactor_set)
    __swig_setmethods__["fyStart"] = _lsf.parameterInfo_fyStart_set
    __swig_getmethods__["fyStart"] = _lsf.parameterInfo_fyStart_get
    if _newclass:fyStart = property(_lsf.parameterInfo_fyStart_get, _lsf.parameterInfo_fyStart_set)
    __swig_setmethods__["maxJobArraySize"] = _lsf.parameterInfo_maxJobArraySize_set
    __swig_getmethods__["maxJobArraySize"] = _lsf.parameterInfo_maxJobArraySize_get
    if _newclass:maxJobArraySize = property(_lsf.parameterInfo_maxJobArraySize_get, _lsf.parameterInfo_maxJobArraySize_set)
    __swig_setmethods__["exceptReplayPeriod"] = _lsf.parameterInfo_exceptReplayPeriod_set
    __swig_getmethods__["exceptReplayPeriod"] = _lsf.parameterInfo_exceptReplayPeriod_get
    if _newclass:exceptReplayPeriod = property(_lsf.parameterInfo_exceptReplayPeriod_get, _lsf.parameterInfo_exceptReplayPeriod_set)
    __swig_setmethods__["jobTerminateInterval"] = _lsf.parameterInfo_jobTerminateInterval_set
    __swig_getmethods__["jobTerminateInterval"] = _lsf.parameterInfo_jobTerminateInterval_get
    if _newclass:jobTerminateInterval = property(_lsf.parameterInfo_jobTerminateInterval_get, _lsf.parameterInfo_jobTerminateInterval_set)
    __swig_setmethods__["disableUAcctMap"] = _lsf.parameterInfo_disableUAcctMap_set
    __swig_getmethods__["disableUAcctMap"] = _lsf.parameterInfo_disableUAcctMap_get
    if _newclass:disableUAcctMap = property(_lsf.parameterInfo_disableUAcctMap_get, _lsf.parameterInfo_disableUAcctMap_set)
    __swig_setmethods__["enforceFSProj"] = _lsf.parameterInfo_enforceFSProj_set
    __swig_getmethods__["enforceFSProj"] = _lsf.parameterInfo_enforceFSProj_get
    if _newclass:enforceFSProj = property(_lsf.parameterInfo_enforceFSProj_get, _lsf.parameterInfo_enforceFSProj_set)
    __swig_setmethods__["enforceProjCheck"] = _lsf.parameterInfo_enforceProjCheck_set
    __swig_getmethods__["enforceProjCheck"] = _lsf.parameterInfo_enforceProjCheck_get
    if _newclass:enforceProjCheck = property(_lsf.parameterInfo_enforceProjCheck_get, _lsf.parameterInfo_enforceProjCheck_set)
    __swig_setmethods__["jobRunTimes"] = _lsf.parameterInfo_jobRunTimes_set
    __swig_getmethods__["jobRunTimes"] = _lsf.parameterInfo_jobRunTimes_get
    if _newclass:jobRunTimes = property(_lsf.parameterInfo_jobRunTimes_get, _lsf.parameterInfo_jobRunTimes_set)
    __swig_setmethods__["dbDefaultIntval"] = _lsf.parameterInfo_dbDefaultIntval_set
    __swig_getmethods__["dbDefaultIntval"] = _lsf.parameterInfo_dbDefaultIntval_get
    if _newclass:dbDefaultIntval = property(_lsf.parameterInfo_dbDefaultIntval_get, _lsf.parameterInfo_dbDefaultIntval_set)
    __swig_setmethods__["dbHjobCountIntval"] = _lsf.parameterInfo_dbHjobCountIntval_set
    __swig_getmethods__["dbHjobCountIntval"] = _lsf.parameterInfo_dbHjobCountIntval_get
    if _newclass:dbHjobCountIntval = property(_lsf.parameterInfo_dbHjobCountIntval_get, _lsf.parameterInfo_dbHjobCountIntval_set)
    __swig_setmethods__["dbQjobCountIntval"] = _lsf.parameterInfo_dbQjobCountIntval_set
    __swig_getmethods__["dbQjobCountIntval"] = _lsf.parameterInfo_dbQjobCountIntval_get
    if _newclass:dbQjobCountIntval = property(_lsf.parameterInfo_dbQjobCountIntval_get, _lsf.parameterInfo_dbQjobCountIntval_set)
    __swig_setmethods__["dbUjobCountIntval"] = _lsf.parameterInfo_dbUjobCountIntval_set
    __swig_getmethods__["dbUjobCountIntval"] = _lsf.parameterInfo_dbUjobCountIntval_get
    if _newclass:dbUjobCountIntval = property(_lsf.parameterInfo_dbUjobCountIntval_get, _lsf.parameterInfo_dbUjobCountIntval_set)
    __swig_setmethods__["dbJobResUsageIntval"] = _lsf.parameterInfo_dbJobResUsageIntval_set
    __swig_getmethods__["dbJobResUsageIntval"] = _lsf.parameterInfo_dbJobResUsageIntval_get
    if _newclass:dbJobResUsageIntval = property(_lsf.parameterInfo_dbJobResUsageIntval_get, _lsf.parameterInfo_dbJobResUsageIntval_set)
    __swig_setmethods__["dbLoadIntval"] = _lsf.parameterInfo_dbLoadIntval_set
    __swig_getmethods__["dbLoadIntval"] = _lsf.parameterInfo_dbLoadIntval_get
    if _newclass:dbLoadIntval = property(_lsf.parameterInfo_dbLoadIntval_get, _lsf.parameterInfo_dbLoadIntval_set)
    __swig_setmethods__["dbJobInfoIntval"] = _lsf.parameterInfo_dbJobInfoIntval_set
    __swig_getmethods__["dbJobInfoIntval"] = _lsf.parameterInfo_dbJobInfoIntval_get
    if _newclass:dbJobInfoIntval = property(_lsf.parameterInfo_dbJobInfoIntval_get, _lsf.parameterInfo_dbJobInfoIntval_set)
    __swig_setmethods__["jobDepLastSub"] = _lsf.parameterInfo_jobDepLastSub_set
    __swig_getmethods__["jobDepLastSub"] = _lsf.parameterInfo_jobDepLastSub_get
    if _newclass:jobDepLastSub = property(_lsf.parameterInfo_jobDepLastSub_get, _lsf.parameterInfo_jobDepLastSub_set)
    __swig_setmethods__["maxJobNameDep"] = _lsf.parameterInfo_maxJobNameDep_set
    __swig_getmethods__["maxJobNameDep"] = _lsf.parameterInfo_maxJobNameDep_get
    if _newclass:maxJobNameDep = property(_lsf.parameterInfo_maxJobNameDep_get, _lsf.parameterInfo_maxJobNameDep_set)
    __swig_setmethods__["dbSelectLoad"] = _lsf.parameterInfo_dbSelectLoad_set
    __swig_getmethods__["dbSelectLoad"] = _lsf.parameterInfo_dbSelectLoad_get
    if _newclass:dbSelectLoad = property(_lsf.parameterInfo_dbSelectLoad_get, _lsf.parameterInfo_dbSelectLoad_set)
    __swig_setmethods__["jobSynJgrp"] = _lsf.parameterInfo_jobSynJgrp_set
    __swig_getmethods__["jobSynJgrp"] = _lsf.parameterInfo_jobSynJgrp_get
    if _newclass:jobSynJgrp = property(_lsf.parameterInfo_jobSynJgrp_get, _lsf.parameterInfo_jobSynJgrp_set)
    __swig_setmethods__["pjobSpoolDir"] = _lsf.parameterInfo_pjobSpoolDir_set
    __swig_getmethods__["pjobSpoolDir"] = _lsf.parameterInfo_pjobSpoolDir_get
    if _newclass:pjobSpoolDir = property(_lsf.parameterInfo_pjobSpoolDir_get, _lsf.parameterInfo_pjobSpoolDir_set)
    __swig_setmethods__["maxUserPriority"] = _lsf.parameterInfo_maxUserPriority_set
    __swig_getmethods__["maxUserPriority"] = _lsf.parameterInfo_maxUserPriority_get
    if _newclass:maxUserPriority = property(_lsf.parameterInfo_maxUserPriority_get, _lsf.parameterInfo_maxUserPriority_set)
    __swig_setmethods__["jobPriorityValue"] = _lsf.parameterInfo_jobPriorityValue_set
    __swig_getmethods__["jobPriorityValue"] = _lsf.parameterInfo_jobPriorityValue_get
    if _newclass:jobPriorityValue = property(_lsf.parameterInfo_jobPriorityValue_get, _lsf.parameterInfo_jobPriorityValue_set)
    __swig_setmethods__["jobPriorityTime"] = _lsf.parameterInfo_jobPriorityTime_set
    __swig_getmethods__["jobPriorityTime"] = _lsf.parameterInfo_jobPriorityTime_get
    if _newclass:jobPriorityTime = property(_lsf.parameterInfo_jobPriorityTime_get, _lsf.parameterInfo_jobPriorityTime_set)
    __swig_setmethods__["enableAutoAdjust"] = _lsf.parameterInfo_enableAutoAdjust_set
    __swig_getmethods__["enableAutoAdjust"] = _lsf.parameterInfo_enableAutoAdjust_get
    if _newclass:enableAutoAdjust = property(_lsf.parameterInfo_enableAutoAdjust_get, _lsf.parameterInfo_enableAutoAdjust_set)
    __swig_setmethods__["autoAdjustAtNumPend"] = _lsf.parameterInfo_autoAdjustAtNumPend_set
    __swig_getmethods__["autoAdjustAtNumPend"] = _lsf.parameterInfo_autoAdjustAtNumPend_get
    if _newclass:autoAdjustAtNumPend = property(_lsf.parameterInfo_autoAdjustAtNumPend_get, _lsf.parameterInfo_autoAdjustAtNumPend_set)
    __swig_setmethods__["autoAdjustAtPercent"] = _lsf.parameterInfo_autoAdjustAtPercent_set
    __swig_getmethods__["autoAdjustAtPercent"] = _lsf.parameterInfo_autoAdjustAtPercent_get
    if _newclass:autoAdjustAtPercent = property(_lsf.parameterInfo_autoAdjustAtPercent_get, _lsf.parameterInfo_autoAdjustAtPercent_set)
    __swig_setmethods__["sharedResourceUpdFactor"] = _lsf.parameterInfo_sharedResourceUpdFactor_set
    __swig_getmethods__["sharedResourceUpdFactor"] = _lsf.parameterInfo_sharedResourceUpdFactor_get
    if _newclass:sharedResourceUpdFactor = property(_lsf.parameterInfo_sharedResourceUpdFactor_get, _lsf.parameterInfo_sharedResourceUpdFactor_set)
    __swig_setmethods__["scheRawLoad"] = _lsf.parameterInfo_scheRawLoad_set
    __swig_getmethods__["scheRawLoad"] = _lsf.parameterInfo_scheRawLoad_get
    if _newclass:scheRawLoad = property(_lsf.parameterInfo_scheRawLoad_get, _lsf.parameterInfo_scheRawLoad_set)
    __swig_setmethods__["jobAttaDir"] = _lsf.parameterInfo_jobAttaDir_set
    __swig_getmethods__["jobAttaDir"] = _lsf.parameterInfo_jobAttaDir_get
    if _newclass:jobAttaDir = property(_lsf.parameterInfo_jobAttaDir_get, _lsf.parameterInfo_jobAttaDir_set)
    __swig_setmethods__["maxJobMsgNum"] = _lsf.parameterInfo_maxJobMsgNum_set
    __swig_getmethods__["maxJobMsgNum"] = _lsf.parameterInfo_maxJobMsgNum_get
    if _newclass:maxJobMsgNum = property(_lsf.parameterInfo_maxJobMsgNum_get, _lsf.parameterInfo_maxJobMsgNum_set)
    __swig_setmethods__["maxJobAttaSize"] = _lsf.parameterInfo_maxJobAttaSize_set
    __swig_getmethods__["maxJobAttaSize"] = _lsf.parameterInfo_maxJobAttaSize_get
    if _newclass:maxJobAttaSize = property(_lsf.parameterInfo_maxJobAttaSize_get, _lsf.parameterInfo_maxJobAttaSize_set)
    __swig_setmethods__["mbdRefreshTime"] = _lsf.parameterInfo_mbdRefreshTime_set
    __swig_getmethods__["mbdRefreshTime"] = _lsf.parameterInfo_mbdRefreshTime_get
    if _newclass:mbdRefreshTime = property(_lsf.parameterInfo_mbdRefreshTime_get, _lsf.parameterInfo_mbdRefreshTime_set)
    __swig_setmethods__["updJobRusageInterval"] = _lsf.parameterInfo_updJobRusageInterval_set
    __swig_getmethods__["updJobRusageInterval"] = _lsf.parameterInfo_updJobRusageInterval_get
    if _newclass:updJobRusageInterval = property(_lsf.parameterInfo_updJobRusageInterval_get, _lsf.parameterInfo_updJobRusageInterval_set)
    __swig_setmethods__["sysMapAcct"] = _lsf.parameterInfo_sysMapAcct_set
    __swig_getmethods__["sysMapAcct"] = _lsf.parameterInfo_sysMapAcct_get
    if _newclass:sysMapAcct = property(_lsf.parameterInfo_sysMapAcct_get, _lsf.parameterInfo_sysMapAcct_set)
    __swig_setmethods__["preExecDelay"] = _lsf.parameterInfo_preExecDelay_set
    __swig_getmethods__["preExecDelay"] = _lsf.parameterInfo_preExecDelay_get
    if _newclass:preExecDelay = property(_lsf.parameterInfo_preExecDelay_get, _lsf.parameterInfo_preExecDelay_set)
    __swig_setmethods__["updEventUpdateInterval"] = _lsf.parameterInfo_updEventUpdateInterval_set
    __swig_getmethods__["updEventUpdateInterval"] = _lsf.parameterInfo_updEventUpdateInterval_get
    if _newclass:updEventUpdateInterval = property(_lsf.parameterInfo_updEventUpdateInterval_get, _lsf.parameterInfo_updEventUpdateInterval_set)
    __swig_setmethods__["resourceReservePerSlot"] = _lsf.parameterInfo_resourceReservePerSlot_set
    __swig_getmethods__["resourceReservePerSlot"] = _lsf.parameterInfo_resourceReservePerSlot_get
    if _newclass:resourceReservePerSlot = property(_lsf.parameterInfo_resourceReservePerSlot_get, _lsf.parameterInfo_resourceReservePerSlot_set)
    __swig_setmethods__["maxJobId"] = _lsf.parameterInfo_maxJobId_set
    __swig_getmethods__["maxJobId"] = _lsf.parameterInfo_maxJobId_get
    if _newclass:maxJobId = property(_lsf.parameterInfo_maxJobId_get, _lsf.parameterInfo_maxJobId_set)
    __swig_setmethods__["preemptResourceList"] = _lsf.parameterInfo_preemptResourceList_set
    __swig_getmethods__["preemptResourceList"] = _lsf.parameterInfo_preemptResourceList_get
    if _newclass:preemptResourceList = property(_lsf.parameterInfo_preemptResourceList_get, _lsf.parameterInfo_preemptResourceList_set)
    __swig_setmethods__["preemptionWaitTime"] = _lsf.parameterInfo_preemptionWaitTime_set
    __swig_getmethods__["preemptionWaitTime"] = _lsf.parameterInfo_preemptionWaitTime_get
    if _newclass:preemptionWaitTime = property(_lsf.parameterInfo_preemptionWaitTime_get, _lsf.parameterInfo_preemptionWaitTime_set)
    __swig_setmethods__["maxAcctArchiveNum"] = _lsf.parameterInfo_maxAcctArchiveNum_set
    __swig_getmethods__["maxAcctArchiveNum"] = _lsf.parameterInfo_maxAcctArchiveNum_get
    if _newclass:maxAcctArchiveNum = property(_lsf.parameterInfo_maxAcctArchiveNum_get, _lsf.parameterInfo_maxAcctArchiveNum_set)
    __swig_setmethods__["acctArchiveInDays"] = _lsf.parameterInfo_acctArchiveInDays_set
    __swig_getmethods__["acctArchiveInDays"] = _lsf.parameterInfo_acctArchiveInDays_get
    if _newclass:acctArchiveInDays = property(_lsf.parameterInfo_acctArchiveInDays_get, _lsf.parameterInfo_acctArchiveInDays_set)
    __swig_setmethods__["acctArchiveInSize"] = _lsf.parameterInfo_acctArchiveInSize_set
    __swig_getmethods__["acctArchiveInSize"] = _lsf.parameterInfo_acctArchiveInSize_get
    if _newclass:acctArchiveInSize = property(_lsf.parameterInfo_acctArchiveInSize_get, _lsf.parameterInfo_acctArchiveInSize_set)
    __swig_setmethods__["committedRunTimeFactor"] = _lsf.parameterInfo_committedRunTimeFactor_set
    __swig_getmethods__["committedRunTimeFactor"] = _lsf.parameterInfo_committedRunTimeFactor_get
    if _newclass:committedRunTimeFactor = property(_lsf.parameterInfo_committedRunTimeFactor_get, _lsf.parameterInfo_committedRunTimeFactor_set)
    __swig_setmethods__["enableHistRunTime"] = _lsf.parameterInfo_enableHistRunTime_set
    __swig_getmethods__["enableHistRunTime"] = _lsf.parameterInfo_enableHistRunTime_get
    if _newclass:enableHistRunTime = property(_lsf.parameterInfo_enableHistRunTime_get, _lsf.parameterInfo_enableHistRunTime_set)
    __swig_setmethods__["mcbOlmReclaimTimeDelay"] = _lsf.parameterInfo_mcbOlmReclaimTimeDelay_set
    __swig_getmethods__["mcbOlmReclaimTimeDelay"] = _lsf.parameterInfo_mcbOlmReclaimTimeDelay_get
    if _newclass:mcbOlmReclaimTimeDelay = property(_lsf.parameterInfo_mcbOlmReclaimTimeDelay_get, _lsf.parameterInfo_mcbOlmReclaimTimeDelay_set)
    __swig_setmethods__["chunkJobDuration"] = _lsf.parameterInfo_chunkJobDuration_set
    __swig_getmethods__["chunkJobDuration"] = _lsf.parameterInfo_chunkJobDuration_get
    if _newclass:chunkJobDuration = property(_lsf.parameterInfo_chunkJobDuration_get, _lsf.parameterInfo_chunkJobDuration_set)
    __swig_setmethods__["sessionInterval"] = _lsf.parameterInfo_sessionInterval_set
    __swig_getmethods__["sessionInterval"] = _lsf.parameterInfo_sessionInterval_get
    if _newclass:sessionInterval = property(_lsf.parameterInfo_sessionInterval_get, _lsf.parameterInfo_sessionInterval_set)
    __swig_setmethods__["publishReasonJobNum"] = _lsf.parameterInfo_publishReasonJobNum_set
    __swig_getmethods__["publishReasonJobNum"] = _lsf.parameterInfo_publishReasonJobNum_get
    if _newclass:publishReasonJobNum = property(_lsf.parameterInfo_publishReasonJobNum_get, _lsf.parameterInfo_publishReasonJobNum_set)
    __swig_setmethods__["publishReasonInterval"] = _lsf.parameterInfo_publishReasonInterval_set
    __swig_getmethods__["publishReasonInterval"] = _lsf.parameterInfo_publishReasonInterval_get
    if _newclass:publishReasonInterval = property(_lsf.parameterInfo_publishReasonInterval_get, _lsf.parameterInfo_publishReasonInterval_set)
    __swig_setmethods__["publishReason4AllJobInterval"] = _lsf.parameterInfo_publishReason4AllJobInterval_set
    __swig_getmethods__["publishReason4AllJobInterval"] = _lsf.parameterInfo_publishReason4AllJobInterval_get
    if _newclass:publishReason4AllJobInterval = property(_lsf.parameterInfo_publishReason4AllJobInterval_get, _lsf.parameterInfo_publishReason4AllJobInterval_set)
    __swig_setmethods__["mcUpdPendingReasonInterval"] = _lsf.parameterInfo_mcUpdPendingReasonInterval_set
    __swig_getmethods__["mcUpdPendingReasonInterval"] = _lsf.parameterInfo_mcUpdPendingReasonInterval_get
    if _newclass:mcUpdPendingReasonInterval = property(_lsf.parameterInfo_mcUpdPendingReasonInterval_get, _lsf.parameterInfo_mcUpdPendingReasonInterval_set)
    __swig_setmethods__["mcUpdPendingReasonPkgSize"] = _lsf.parameterInfo_mcUpdPendingReasonPkgSize_set
    __swig_getmethods__["mcUpdPendingReasonPkgSize"] = _lsf.parameterInfo_mcUpdPendingReasonPkgSize_get
    if _newclass:mcUpdPendingReasonPkgSize = property(_lsf.parameterInfo_mcUpdPendingReasonPkgSize_get, _lsf.parameterInfo_mcUpdPendingReasonPkgSize_set)
    __swig_setmethods__["noPreemptRunTime"] = _lsf.parameterInfo_noPreemptRunTime_set
    __swig_getmethods__["noPreemptRunTime"] = _lsf.parameterInfo_noPreemptRunTime_get
    if _newclass:noPreemptRunTime = property(_lsf.parameterInfo_noPreemptRunTime_get, _lsf.parameterInfo_noPreemptRunTime_set)
    __swig_setmethods__["noPreemptFinishTime"] = _lsf.parameterInfo_noPreemptFinishTime_set
    __swig_getmethods__["noPreemptFinishTime"] = _lsf.parameterInfo_noPreemptFinishTime_get
    if _newclass:noPreemptFinishTime = property(_lsf.parameterInfo_noPreemptFinishTime_get, _lsf.parameterInfo_noPreemptFinishTime_set)
    __swig_setmethods__["acctArchiveAt"] = _lsf.parameterInfo_acctArchiveAt_set
    __swig_getmethods__["acctArchiveAt"] = _lsf.parameterInfo_acctArchiveAt_get
    if _newclass:acctArchiveAt = property(_lsf.parameterInfo_acctArchiveAt_get, _lsf.parameterInfo_acctArchiveAt_set)
    __swig_setmethods__["absoluteRunLimit"] = _lsf.parameterInfo_absoluteRunLimit_set
    __swig_getmethods__["absoluteRunLimit"] = _lsf.parameterInfo_absoluteRunLimit_get
    if _newclass:absoluteRunLimit = property(_lsf.parameterInfo_absoluteRunLimit_get, _lsf.parameterInfo_absoluteRunLimit_set)
    __swig_setmethods__["lsbExitRateDuration"] = _lsf.parameterInfo_lsbExitRateDuration_set
    __swig_getmethods__["lsbExitRateDuration"] = _lsf.parameterInfo_lsbExitRateDuration_get
    if _newclass:lsbExitRateDuration = property(_lsf.parameterInfo_lsbExitRateDuration_get, _lsf.parameterInfo_lsbExitRateDuration_set)
    __swig_setmethods__["lsbTriggerDuration"] = _lsf.parameterInfo_lsbTriggerDuration_set
    __swig_getmethods__["lsbTriggerDuration"] = _lsf.parameterInfo_lsbTriggerDuration_get
    if _newclass:lsbTriggerDuration = property(_lsf.parameterInfo_lsbTriggerDuration_get, _lsf.parameterInfo_lsbTriggerDuration_set)
    __swig_setmethods__["maxJobinfoQueryPeriod"] = _lsf.parameterInfo_maxJobinfoQueryPeriod_set
    __swig_getmethods__["maxJobinfoQueryPeriod"] = _lsf.parameterInfo_maxJobinfoQueryPeriod_get
    if _newclass:maxJobinfoQueryPeriod = property(_lsf.parameterInfo_maxJobinfoQueryPeriod_get, _lsf.parameterInfo_maxJobinfoQueryPeriod_set)
    __swig_setmethods__["jobSubRetryInterval"] = _lsf.parameterInfo_jobSubRetryInterval_set
    __swig_getmethods__["jobSubRetryInterval"] = _lsf.parameterInfo_jobSubRetryInterval_get
    if _newclass:jobSubRetryInterval = property(_lsf.parameterInfo_jobSubRetryInterval_get, _lsf.parameterInfo_jobSubRetryInterval_set)
    __swig_setmethods__["pendingJobThreshold"] = _lsf.parameterInfo_pendingJobThreshold_set
    __swig_getmethods__["pendingJobThreshold"] = _lsf.parameterInfo_pendingJobThreshold_get
    if _newclass:pendingJobThreshold = property(_lsf.parameterInfo_pendingJobThreshold_get, _lsf.parameterInfo_pendingJobThreshold_set)
    __swig_setmethods__["maxConcurrentJobQuery"] = _lsf.parameterInfo_maxConcurrentJobQuery_set
    __swig_getmethods__["maxConcurrentJobQuery"] = _lsf.parameterInfo_maxConcurrentJobQuery_get
    if _newclass:maxConcurrentJobQuery = property(_lsf.parameterInfo_maxConcurrentJobQuery_get, _lsf.parameterInfo_maxConcurrentJobQuery_set)
    __swig_setmethods__["minSwitchPeriod"] = _lsf.parameterInfo_minSwitchPeriod_set
    __swig_getmethods__["minSwitchPeriod"] = _lsf.parameterInfo_minSwitchPeriod_get
    if _newclass:minSwitchPeriod = property(_lsf.parameterInfo_minSwitchPeriod_get, _lsf.parameterInfo_minSwitchPeriod_set)
    __swig_setmethods__["condensePendingReasons"] = _lsf.parameterInfo_condensePendingReasons_set
    __swig_getmethods__["condensePendingReasons"] = _lsf.parameterInfo_condensePendingReasons_get
    if _newclass:condensePendingReasons = property(_lsf.parameterInfo_condensePendingReasons_get, _lsf.parameterInfo_condensePendingReasons_set)
    __swig_setmethods__["slotBasedParallelSched"] = _lsf.parameterInfo_slotBasedParallelSched_set
    __swig_getmethods__["slotBasedParallelSched"] = _lsf.parameterInfo_slotBasedParallelSched_get
    if _newclass:slotBasedParallelSched = property(_lsf.parameterInfo_slotBasedParallelSched_get, _lsf.parameterInfo_slotBasedParallelSched_set)
    __swig_setmethods__["disableUserJobMovement"] = _lsf.parameterInfo_disableUserJobMovement_set
    __swig_getmethods__["disableUserJobMovement"] = _lsf.parameterInfo_disableUserJobMovement_get
    if _newclass:disableUserJobMovement = property(_lsf.parameterInfo_disableUserJobMovement_get, _lsf.parameterInfo_disableUserJobMovement_set)
    __swig_setmethods__["detectIdleJobAfter"] = _lsf.parameterInfo_detectIdleJobAfter_set
    __swig_getmethods__["detectIdleJobAfter"] = _lsf.parameterInfo_detectIdleJobAfter_get
    if _newclass:detectIdleJobAfter = property(_lsf.parameterInfo_detectIdleJobAfter_get, _lsf.parameterInfo_detectIdleJobAfter_set)
    __swig_setmethods__["useSymbolPriority"] = _lsf.parameterInfo_useSymbolPriority_set
    __swig_getmethods__["useSymbolPriority"] = _lsf.parameterInfo_useSymbolPriority_get
    if _newclass:useSymbolPriority = property(_lsf.parameterInfo_useSymbolPriority_get, _lsf.parameterInfo_useSymbolPriority_set)
    __swig_setmethods__["JobPriorityRound"] = _lsf.parameterInfo_JobPriorityRound_set
    __swig_getmethods__["JobPriorityRound"] = _lsf.parameterInfo_JobPriorityRound_get
    if _newclass:JobPriorityRound = property(_lsf.parameterInfo_JobPriorityRound_get, _lsf.parameterInfo_JobPriorityRound_set)
    __swig_setmethods__["priorityMapping"] = _lsf.parameterInfo_priorityMapping_set
    __swig_getmethods__["priorityMapping"] = _lsf.parameterInfo_priorityMapping_get
    if _newclass:priorityMapping = property(_lsf.parameterInfo_priorityMapping_get, _lsf.parameterInfo_priorityMapping_set)
    __swig_setmethods__["maxInfoDirs"] = _lsf.parameterInfo_maxInfoDirs_set
    __swig_getmethods__["maxInfoDirs"] = _lsf.parameterInfo_maxInfoDirs_get
    if _newclass:maxInfoDirs = property(_lsf.parameterInfo_maxInfoDirs_get, _lsf.parameterInfo_maxInfoDirs_set)
    __swig_setmethods__["minMbdRefreshTime"] = _lsf.parameterInfo_minMbdRefreshTime_set
    __swig_getmethods__["minMbdRefreshTime"] = _lsf.parameterInfo_minMbdRefreshTime_get
    if _newclass:minMbdRefreshTime = property(_lsf.parameterInfo_minMbdRefreshTime_get, _lsf.parameterInfo_minMbdRefreshTime_set)
    __swig_setmethods__["enableStopAskingLicenses2LS"] = _lsf.parameterInfo_enableStopAskingLicenses2LS_set
    __swig_getmethods__["enableStopAskingLicenses2LS"] = _lsf.parameterInfo_enableStopAskingLicenses2LS_get
    if _newclass:enableStopAskingLicenses2LS = property(_lsf.parameterInfo_enableStopAskingLicenses2LS_get, _lsf.parameterInfo_enableStopAskingLicenses2LS_set)
    __swig_setmethods__["expiredTime"] = _lsf.parameterInfo_expiredTime_set
    __swig_getmethods__["expiredTime"] = _lsf.parameterInfo_expiredTime_get
    if _newclass:expiredTime = property(_lsf.parameterInfo_expiredTime_get, _lsf.parameterInfo_expiredTime_set)
    __swig_setmethods__["mbdQueryCPUs"] = _lsf.parameterInfo_mbdQueryCPUs_set
    __swig_getmethods__["mbdQueryCPUs"] = _lsf.parameterInfo_mbdQueryCPUs_get
    if _newclass:mbdQueryCPUs = property(_lsf.parameterInfo_mbdQueryCPUs_get, _lsf.parameterInfo_mbdQueryCPUs_set)
    __swig_setmethods__["defaultApp"] = _lsf.parameterInfo_defaultApp_set
    __swig_getmethods__["defaultApp"] = _lsf.parameterInfo_defaultApp_get
    if _newclass:defaultApp = property(_lsf.parameterInfo_defaultApp_get, _lsf.parameterInfo_defaultApp_set)
    __swig_setmethods__["enableStream"] = _lsf.parameterInfo_enableStream_set
    __swig_getmethods__["enableStream"] = _lsf.parameterInfo_enableStream_get
    if _newclass:enableStream = property(_lsf.parameterInfo_enableStream_get, _lsf.parameterInfo_enableStream_set)
    __swig_setmethods__["streamFile"] = _lsf.parameterInfo_streamFile_set
    __swig_getmethods__["streamFile"] = _lsf.parameterInfo_streamFile_get
    if _newclass:streamFile = property(_lsf.parameterInfo_streamFile_get, _lsf.parameterInfo_streamFile_set)
    __swig_setmethods__["streamSize"] = _lsf.parameterInfo_streamSize_set
    __swig_getmethods__["streamSize"] = _lsf.parameterInfo_streamSize_get
    if _newclass:streamSize = property(_lsf.parameterInfo_streamSize_get, _lsf.parameterInfo_streamSize_set)
    __swig_setmethods__["syncUpHostStatusWithLIM"] = _lsf.parameterInfo_syncUpHostStatusWithLIM_set
    __swig_getmethods__["syncUpHostStatusWithLIM"] = _lsf.parameterInfo_syncUpHostStatusWithLIM_get
    if _newclass:syncUpHostStatusWithLIM = property(_lsf.parameterInfo_syncUpHostStatusWithLIM_get, _lsf.parameterInfo_syncUpHostStatusWithLIM_set)
    __swig_setmethods__["defaultSLA"] = _lsf.parameterInfo_defaultSLA_set
    __swig_getmethods__["defaultSLA"] = _lsf.parameterInfo_defaultSLA_get
    if _newclass:defaultSLA = property(_lsf.parameterInfo_defaultSLA_get, _lsf.parameterInfo_defaultSLA_set)
    __swig_setmethods__["slaTimer"] = _lsf.parameterInfo_slaTimer_set
    __swig_getmethods__["slaTimer"] = _lsf.parameterInfo_slaTimer_get
    if _newclass:slaTimer = property(_lsf.parameterInfo_slaTimer_get, _lsf.parameterInfo_slaTimer_set)
    __swig_setmethods__["mbdEgoTtl"] = _lsf.parameterInfo_mbdEgoTtl_set
    __swig_getmethods__["mbdEgoTtl"] = _lsf.parameterInfo_mbdEgoTtl_get
    if _newclass:mbdEgoTtl = property(_lsf.parameterInfo_mbdEgoTtl_get, _lsf.parameterInfo_mbdEgoTtl_set)
    __swig_setmethods__["mbdEgoConnTimeout"] = _lsf.parameterInfo_mbdEgoConnTimeout_set
    __swig_getmethods__["mbdEgoConnTimeout"] = _lsf.parameterInfo_mbdEgoConnTimeout_get
    if _newclass:mbdEgoConnTimeout = property(_lsf.parameterInfo_mbdEgoConnTimeout_get, _lsf.parameterInfo_mbdEgoConnTimeout_set)
    __swig_setmethods__["mbdEgoReadTimeout"] = _lsf.parameterInfo_mbdEgoReadTimeout_set
    __swig_getmethods__["mbdEgoReadTimeout"] = _lsf.parameterInfo_mbdEgoReadTimeout_get
    if _newclass:mbdEgoReadTimeout = property(_lsf.parameterInfo_mbdEgoReadTimeout_get, _lsf.parameterInfo_mbdEgoReadTimeout_set)
    __swig_setmethods__["mbdUseEgoMXJ"] = _lsf.parameterInfo_mbdUseEgoMXJ_set
    __swig_getmethods__["mbdUseEgoMXJ"] = _lsf.parameterInfo_mbdUseEgoMXJ_get
    if _newclass:mbdUseEgoMXJ = property(_lsf.parameterInfo_mbdUseEgoMXJ_get, _lsf.parameterInfo_mbdUseEgoMXJ_set)
    __swig_setmethods__["mbdEgoReclaimByQueue"] = _lsf.parameterInfo_mbdEgoReclaimByQueue_set
    __swig_getmethods__["mbdEgoReclaimByQueue"] = _lsf.parameterInfo_mbdEgoReclaimByQueue_get
    if _newclass:mbdEgoReclaimByQueue = property(_lsf.parameterInfo_mbdEgoReclaimByQueue_get, _lsf.parameterInfo_mbdEgoReclaimByQueue_set)
    __swig_setmethods__["defaultSLAvelocity"] = _lsf.parameterInfo_defaultSLAvelocity_set
    __swig_getmethods__["defaultSLAvelocity"] = _lsf.parameterInfo_defaultSLAvelocity_get
    if _newclass:defaultSLAvelocity = property(_lsf.parameterInfo_defaultSLAvelocity_get, _lsf.parameterInfo_defaultSLAvelocity_set)
    __swig_setmethods__["exitRateTypes"] = _lsf.parameterInfo_exitRateTypes_set
    __swig_getmethods__["exitRateTypes"] = _lsf.parameterInfo_exitRateTypes_get
    if _newclass:exitRateTypes = property(_lsf.parameterInfo_exitRateTypes_get, _lsf.parameterInfo_exitRateTypes_set)
    __swig_setmethods__["globalJobExitRate"] = _lsf.parameterInfo_globalJobExitRate_set
    __swig_getmethods__["globalJobExitRate"] = _lsf.parameterInfo_globalJobExitRate_get
    if _newclass:globalJobExitRate = property(_lsf.parameterInfo_globalJobExitRate_get, _lsf.parameterInfo_globalJobExitRate_set)
    __swig_setmethods__["enableJobExitRatePerSlot"] = _lsf.parameterInfo_enableJobExitRatePerSlot_set
    __swig_getmethods__["enableJobExitRatePerSlot"] = _lsf.parameterInfo_enableJobExitRatePerSlot_get
    if _newclass:enableJobExitRatePerSlot = property(_lsf.parameterInfo_enableJobExitRatePerSlot_get, _lsf.parameterInfo_enableJobExitRatePerSlot_set)
    __swig_setmethods__["enableMetric"] = _lsf.parameterInfo_enableMetric_set
    __swig_getmethods__["enableMetric"] = _lsf.parameterInfo_enableMetric_get
    if _newclass:enableMetric = property(_lsf.parameterInfo_enableMetric_get, _lsf.parameterInfo_enableMetric_set)
    __swig_setmethods__["schMetricsSample"] = _lsf.parameterInfo_schMetricsSample_set
    __swig_getmethods__["schMetricsSample"] = _lsf.parameterInfo_schMetricsSample_get
    if _newclass:schMetricsSample = property(_lsf.parameterInfo_schMetricsSample_get, _lsf.parameterInfo_schMetricsSample_set)
    __swig_setmethods__["maxApsValue"] = _lsf.parameterInfo_maxApsValue_set
    __swig_getmethods__["maxApsValue"] = _lsf.parameterInfo_maxApsValue_get
    if _newclass:maxApsValue = property(_lsf.parameterInfo_maxApsValue_get, _lsf.parameterInfo_maxApsValue_set)
    __swig_setmethods__["newjobRefresh"] = _lsf.parameterInfo_newjobRefresh_set
    __swig_getmethods__["newjobRefresh"] = _lsf.parameterInfo_newjobRefresh_get
    if _newclass:newjobRefresh = property(_lsf.parameterInfo_newjobRefresh_get, _lsf.parameterInfo_newjobRefresh_set)
    __swig_setmethods__["preemptJobType"] = _lsf.parameterInfo_preemptJobType_set
    __swig_getmethods__["preemptJobType"] = _lsf.parameterInfo_preemptJobType_get
    if _newclass:preemptJobType = property(_lsf.parameterInfo_preemptJobType_get, _lsf.parameterInfo_preemptJobType_set)
    __swig_setmethods__["defaultJgrp"] = _lsf.parameterInfo_defaultJgrp_set
    __swig_getmethods__["defaultJgrp"] = _lsf.parameterInfo_defaultJgrp_get
    if _newclass:defaultJgrp = property(_lsf.parameterInfo_defaultJgrp_get, _lsf.parameterInfo_defaultJgrp_set)
    __swig_setmethods__["jobRunlimitRatio"] = _lsf.parameterInfo_jobRunlimitRatio_set
    __swig_getmethods__["jobRunlimitRatio"] = _lsf.parameterInfo_jobRunlimitRatio_get
    if _newclass:jobRunlimitRatio = property(_lsf.parameterInfo_jobRunlimitRatio_get, _lsf.parameterInfo_jobRunlimitRatio_set)
    __swig_setmethods__["jobIncludePostproc"] = _lsf.parameterInfo_jobIncludePostproc_set
    __swig_getmethods__["jobIncludePostproc"] = _lsf.parameterInfo_jobIncludePostproc_get
    if _newclass:jobIncludePostproc = property(_lsf.parameterInfo_jobIncludePostproc_get, _lsf.parameterInfo_jobIncludePostproc_set)
    __swig_setmethods__["jobPostprocTimeout"] = _lsf.parameterInfo_jobPostprocTimeout_set
    __swig_getmethods__["jobPostprocTimeout"] = _lsf.parameterInfo_jobPostprocTimeout_get
    if _newclass:jobPostprocTimeout = property(_lsf.parameterInfo_jobPostprocTimeout_get, _lsf.parameterInfo_jobPostprocTimeout_set)
    __swig_setmethods__["sschedUpdateSummaryInterval"] = _lsf.parameterInfo_sschedUpdateSummaryInterval_set
    __swig_getmethods__["sschedUpdateSummaryInterval"] = _lsf.parameterInfo_sschedUpdateSummaryInterval_get
    if _newclass:sschedUpdateSummaryInterval = property(_lsf.parameterInfo_sschedUpdateSummaryInterval_get, _lsf.parameterInfo_sschedUpdateSummaryInterval_set)
    __swig_setmethods__["sschedUpdateSummaryByTask"] = _lsf.parameterInfo_sschedUpdateSummaryByTask_set
    __swig_getmethods__["sschedUpdateSummaryByTask"] = _lsf.parameterInfo_sschedUpdateSummaryByTask_get
    if _newclass:sschedUpdateSummaryByTask = property(_lsf.parameterInfo_sschedUpdateSummaryByTask_get, _lsf.parameterInfo_sschedUpdateSummaryByTask_set)
    __swig_setmethods__["sschedRequeueLimit"] = _lsf.parameterInfo_sschedRequeueLimit_set
    __swig_getmethods__["sschedRequeueLimit"] = _lsf.parameterInfo_sschedRequeueLimit_get
    if _newclass:sschedRequeueLimit = property(_lsf.parameterInfo_sschedRequeueLimit_get, _lsf.parameterInfo_sschedRequeueLimit_set)
    __swig_setmethods__["sschedRetryLimit"] = _lsf.parameterInfo_sschedRetryLimit_set
    __swig_getmethods__["sschedRetryLimit"] = _lsf.parameterInfo_sschedRetryLimit_get
    if _newclass:sschedRetryLimit = property(_lsf.parameterInfo_sschedRetryLimit_get, _lsf.parameterInfo_sschedRetryLimit_set)
    __swig_setmethods__["sschedMaxTasks"] = _lsf.parameterInfo_sschedMaxTasks_set
    __swig_getmethods__["sschedMaxTasks"] = _lsf.parameterInfo_sschedMaxTasks_get
    if _newclass:sschedMaxTasks = property(_lsf.parameterInfo_sschedMaxTasks_get, _lsf.parameterInfo_sschedMaxTasks_set)
    __swig_setmethods__["sschedMaxRuntime"] = _lsf.parameterInfo_sschedMaxRuntime_set
    __swig_getmethods__["sschedMaxRuntime"] = _lsf.parameterInfo_sschedMaxRuntime_get
    if _newclass:sschedMaxRuntime = property(_lsf.parameterInfo_sschedMaxRuntime_get, _lsf.parameterInfo_sschedMaxRuntime_set)
    __swig_setmethods__["sschedAcctDir"] = _lsf.parameterInfo_sschedAcctDir_set
    __swig_getmethods__["sschedAcctDir"] = _lsf.parameterInfo_sschedAcctDir_get
    if _newclass:sschedAcctDir = property(_lsf.parameterInfo_sschedAcctDir_get, _lsf.parameterInfo_sschedAcctDir_set)
    __swig_setmethods__["jgrpAutoDel"] = _lsf.parameterInfo_jgrpAutoDel_set
    __swig_getmethods__["jgrpAutoDel"] = _lsf.parameterInfo_jgrpAutoDel_get
    if _newclass:jgrpAutoDel = property(_lsf.parameterInfo_jgrpAutoDel_get, _lsf.parameterInfo_jgrpAutoDel_set)
    __swig_setmethods__["maxJobPreempt"] = _lsf.parameterInfo_maxJobPreempt_set
    __swig_getmethods__["maxJobPreempt"] = _lsf.parameterInfo_maxJobPreempt_get
    if _newclass:maxJobPreempt = property(_lsf.parameterInfo_maxJobPreempt_get, _lsf.parameterInfo_maxJobPreempt_set)
    __swig_setmethods__["maxJobRequeue"] = _lsf.parameterInfo_maxJobRequeue_set
    __swig_getmethods__["maxJobRequeue"] = _lsf.parameterInfo_maxJobRequeue_get
    if _newclass:maxJobRequeue = property(_lsf.parameterInfo_maxJobRequeue_get, _lsf.parameterInfo_maxJobRequeue_set)
    __swig_setmethods__["noPreemptRunTimePercent"] = _lsf.parameterInfo_noPreemptRunTimePercent_set
    __swig_getmethods__["noPreemptRunTimePercent"] = _lsf.parameterInfo_noPreemptRunTimePercent_get
    if _newclass:noPreemptRunTimePercent = property(_lsf.parameterInfo_noPreemptRunTimePercent_get, _lsf.parameterInfo_noPreemptRunTimePercent_set)
    __swig_setmethods__["noPreemptFinishTimePercent"] = _lsf.parameterInfo_noPreemptFinishTimePercent_set
    __swig_getmethods__["noPreemptFinishTimePercent"] = _lsf.parameterInfo_noPreemptFinishTimePercent_get
    if _newclass:noPreemptFinishTimePercent = property(_lsf.parameterInfo_noPreemptFinishTimePercent_get, _lsf.parameterInfo_noPreemptFinishTimePercent_set)
    __swig_setmethods__["slotReserveQueueLimit"] = _lsf.parameterInfo_slotReserveQueueLimit_set
    __swig_getmethods__["slotReserveQueueLimit"] = _lsf.parameterInfo_slotReserveQueueLimit_get
    if _newclass:slotReserveQueueLimit = property(_lsf.parameterInfo_slotReserveQueueLimit_get, _lsf.parameterInfo_slotReserveQueueLimit_set)
    __swig_setmethods__["maxJobPercentagePerSession"] = _lsf.parameterInfo_maxJobPercentagePerSession_set
    __swig_getmethods__["maxJobPercentagePerSession"] = _lsf.parameterInfo_maxJobPercentagePerSession_get
    if _newclass:maxJobPercentagePerSession = property(_lsf.parameterInfo_maxJobPercentagePerSession_get, _lsf.parameterInfo_maxJobPercentagePerSession_set)
    __swig_setmethods__["useSuspSlots"] = _lsf.parameterInfo_useSuspSlots_set
    __swig_getmethods__["useSuspSlots"] = _lsf.parameterInfo_useSuspSlots_get
    if _newclass:useSuspSlots = property(_lsf.parameterInfo_useSuspSlots_get, _lsf.parameterInfo_useSuspSlots_set)
    __swig_setmethods__["maxStreamFileNum"] = _lsf.parameterInfo_maxStreamFileNum_set
    __swig_getmethods__["maxStreamFileNum"] = _lsf.parameterInfo_maxStreamFileNum_get
    if _newclass:maxStreamFileNum = property(_lsf.parameterInfo_maxStreamFileNum_get, _lsf.parameterInfo_maxStreamFileNum_set)
    __swig_setmethods__["privilegedUserForceBkill"] = _lsf.parameterInfo_privilegedUserForceBkill_set
    __swig_getmethods__["privilegedUserForceBkill"] = _lsf.parameterInfo_privilegedUserForceBkill_get
    if _newclass:privilegedUserForceBkill = property(_lsf.parameterInfo_privilegedUserForceBkill_get, _lsf.parameterInfo_privilegedUserForceBkill_set)
    __swig_setmethods__["mcSchedulingEnhance"] = _lsf.parameterInfo_mcSchedulingEnhance_set
    __swig_getmethods__["mcSchedulingEnhance"] = _lsf.parameterInfo_mcSchedulingEnhance_get
    if _newclass:mcSchedulingEnhance = property(_lsf.parameterInfo_mcSchedulingEnhance_get, _lsf.parameterInfo_mcSchedulingEnhance_set)
    __swig_setmethods__["mcUpdateInterval"] = _lsf.parameterInfo_mcUpdateInterval_set
    __swig_getmethods__["mcUpdateInterval"] = _lsf.parameterInfo_mcUpdateInterval_get
    if _newclass:mcUpdateInterval = property(_lsf.parameterInfo_mcUpdateInterval_get, _lsf.parameterInfo_mcUpdateInterval_set)
    __swig_setmethods__["intersectCandidateHosts"] = _lsf.parameterInfo_intersectCandidateHosts_set
    __swig_getmethods__["intersectCandidateHosts"] = _lsf.parameterInfo_intersectCandidateHosts_get
    if _newclass:intersectCandidateHosts = property(_lsf.parameterInfo_intersectCandidateHosts_get, _lsf.parameterInfo_intersectCandidateHosts_set)
    __swig_setmethods__["enforceOneUGLimit"] = _lsf.parameterInfo_enforceOneUGLimit_set
    __swig_getmethods__["enforceOneUGLimit"] = _lsf.parameterInfo_enforceOneUGLimit_get
    if _newclass:enforceOneUGLimit = property(_lsf.parameterInfo_enforceOneUGLimit_get, _lsf.parameterInfo_enforceOneUGLimit_set)
    __swig_setmethods__["logRuntimeESTExceeded"] = _lsf.parameterInfo_logRuntimeESTExceeded_set
    __swig_getmethods__["logRuntimeESTExceeded"] = _lsf.parameterInfo_logRuntimeESTExceeded_get
    if _newclass:logRuntimeESTExceeded = property(_lsf.parameterInfo_logRuntimeESTExceeded_get, _lsf.parameterInfo_logRuntimeESTExceeded_set)
    __swig_setmethods__["computeUnitTypes"] = _lsf.parameterInfo_computeUnitTypes_set
    __swig_getmethods__["computeUnitTypes"] = _lsf.parameterInfo_computeUnitTypes_get
    if _newclass:computeUnitTypes = property(_lsf.parameterInfo_computeUnitTypes_get, _lsf.parameterInfo_computeUnitTypes_set)
    __swig_setmethods__["fairAdjustFactor"] = _lsf.parameterInfo_fairAdjustFactor_set
    __swig_getmethods__["fairAdjustFactor"] = _lsf.parameterInfo_fairAdjustFactor_get
    if _newclass:fairAdjustFactor = property(_lsf.parameterInfo_fairAdjustFactor_get, _lsf.parameterInfo_fairAdjustFactor_set)
    __swig_setmethods__["simEnableCpuFactor"] = _lsf.parameterInfo_simEnableCpuFactor_set
    __swig_getmethods__["simEnableCpuFactor"] = _lsf.parameterInfo_simEnableCpuFactor_get
    if _newclass:simEnableCpuFactor = property(_lsf.parameterInfo_simEnableCpuFactor_get, _lsf.parameterInfo_simEnableCpuFactor_set)
    __swig_setmethods__["extendJobException"] = _lsf.parameterInfo_extendJobException_set
    __swig_getmethods__["extendJobException"] = _lsf.parameterInfo_extendJobException_get
    if _newclass:extendJobException = property(_lsf.parameterInfo_extendJobException_get, _lsf.parameterInfo_extendJobException_set)
    __swig_setmethods__["preExecExitValues"] = _lsf.parameterInfo_preExecExitValues_set
    __swig_getmethods__["preExecExitValues"] = _lsf.parameterInfo_preExecExitValues_get
    if _newclass:preExecExitValues = property(_lsf.parameterInfo_preExecExitValues_get, _lsf.parameterInfo_preExecExitValues_set)
    __swig_setmethods__["enableRunTimeDecay"] = _lsf.parameterInfo_enableRunTimeDecay_set
    __swig_getmethods__["enableRunTimeDecay"] = _lsf.parameterInfo_enableRunTimeDecay_get
    if _newclass:enableRunTimeDecay = property(_lsf.parameterInfo_enableRunTimeDecay_get, _lsf.parameterInfo_enableRunTimeDecay_set)
    __swig_setmethods__["advResUserLimit"] = _lsf.parameterInfo_advResUserLimit_set
    __swig_getmethods__["advResUserLimit"] = _lsf.parameterInfo_advResUserLimit_get
    if _newclass:advResUserLimit = property(_lsf.parameterInfo_advResUserLimit_get, _lsf.parameterInfo_advResUserLimit_set)
    __swig_setmethods__["noPreemptInterval"] = _lsf.parameterInfo_noPreemptInterval_set
    __swig_getmethods__["noPreemptInterval"] = _lsf.parameterInfo_noPreemptInterval_get
    if _newclass:noPreemptInterval = property(_lsf.parameterInfo_noPreemptInterval_get, _lsf.parameterInfo_noPreemptInterval_set)
    __swig_setmethods__["maxTotalTimePreempt"] = _lsf.parameterInfo_maxTotalTimePreempt_set
    __swig_getmethods__["maxTotalTimePreempt"] = _lsf.parameterInfo_maxTotalTimePreempt_get
    if _newclass:maxTotalTimePreempt = property(_lsf.parameterInfo_maxTotalTimePreempt_get, _lsf.parameterInfo_maxTotalTimePreempt_set)
    __swig_setmethods__["strictUGCtrl"] = _lsf.parameterInfo_strictUGCtrl_set
    __swig_getmethods__["strictUGCtrl"] = _lsf.parameterInfo_strictUGCtrl_get
    if _newclass:strictUGCtrl = property(_lsf.parameterInfo_strictUGCtrl_get, _lsf.parameterInfo_strictUGCtrl_set)
    __swig_setmethods__["defaultUserGroup"] = _lsf.parameterInfo_defaultUserGroup_set
    __swig_getmethods__["defaultUserGroup"] = _lsf.parameterInfo_defaultUserGroup_get
    if _newclass:defaultUserGroup = property(_lsf.parameterInfo_defaultUserGroup_get, _lsf.parameterInfo_defaultUserGroup_set)
    __swig_setmethods__["enforceUGTree"] = _lsf.parameterInfo_enforceUGTree_set
    __swig_getmethods__["enforceUGTree"] = _lsf.parameterInfo_enforceUGTree_get
    if _newclass:enforceUGTree = property(_lsf.parameterInfo_enforceUGTree_get, _lsf.parameterInfo_enforceUGTree_set)
    __swig_setmethods__["preemptDelayTime"] = _lsf.parameterInfo_preemptDelayTime_set
    __swig_getmethods__["preemptDelayTime"] = _lsf.parameterInfo_preemptDelayTime_get
    if _newclass:preemptDelayTime = property(_lsf.parameterInfo_preemptDelayTime_get, _lsf.parameterInfo_preemptDelayTime_set)
    __swig_setmethods__["jobPreprocTimeout"] = _lsf.parameterInfo_jobPreprocTimeout_set
    __swig_getmethods__["jobPreprocTimeout"] = _lsf.parameterInfo_jobPreprocTimeout_get
    if _newclass:jobPreprocTimeout = property(_lsf.parameterInfo_jobPreprocTimeout_get, _lsf.parameterInfo_jobPreprocTimeout_set)
    __swig_setmethods__["allowEventType"] = _lsf.parameterInfo_allowEventType_set
    __swig_getmethods__["allowEventType"] = _lsf.parameterInfo_allowEventType_get
    if _newclass:allowEventType = property(_lsf.parameterInfo_allowEventType_get, _lsf.parameterInfo_allowEventType_set)
    __swig_setmethods__["runtimeLogInterval"] = _lsf.parameterInfo_runtimeLogInterval_set
    __swig_getmethods__["runtimeLogInterval"] = _lsf.parameterInfo_runtimeLogInterval_get
    if _newclass:runtimeLogInterval = property(_lsf.parameterInfo_runtimeLogInterval_get, _lsf.parameterInfo_runtimeLogInterval_set)
    __swig_setmethods__["groupPendJobsBy"] = _lsf.parameterInfo_groupPendJobsBy_set
    __swig_getmethods__["groupPendJobsBy"] = _lsf.parameterInfo_groupPendJobsBy_get
    if _newclass:groupPendJobsBy = property(_lsf.parameterInfo_groupPendJobsBy_get, _lsf.parameterInfo_groupPendJobsBy_set)
    __swig_setmethods__["pendingReasonsExclude"] = _lsf.parameterInfo_pendingReasonsExclude_set
    __swig_getmethods__["pendingReasonsExclude"] = _lsf.parameterInfo_pendingReasonsExclude_get
    if _newclass:pendingReasonsExclude = property(_lsf.parameterInfo_pendingReasonsExclude_get, _lsf.parameterInfo_pendingReasonsExclude_set)
    __swig_setmethods__["pendingTimeRanking"] = _lsf.parameterInfo_pendingTimeRanking_set
    __swig_getmethods__["pendingTimeRanking"] = _lsf.parameterInfo_pendingTimeRanking_get
    if _newclass:pendingTimeRanking = property(_lsf.parameterInfo_pendingTimeRanking_get, _lsf.parameterInfo_pendingTimeRanking_set)
    __swig_setmethods__["includeDetailReasons"] = _lsf.parameterInfo_includeDetailReasons_set
    __swig_getmethods__["includeDetailReasons"] = _lsf.parameterInfo_includeDetailReasons_get
    if _newclass:includeDetailReasons = property(_lsf.parameterInfo_includeDetailReasons_get, _lsf.parameterInfo_includeDetailReasons_set)
    __swig_setmethods__["pendingReasonDir"] = _lsf.parameterInfo_pendingReasonDir_set
    __swig_getmethods__["pendingReasonDir"] = _lsf.parameterInfo_pendingReasonDir_get
    if _newclass:pendingReasonDir = property(_lsf.parameterInfo_pendingReasonDir_get, _lsf.parameterInfo_pendingReasonDir_set)
    def __init__(self, *args): 
        this = _lsf.new_parameterInfo(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _lsf.delete_parameterInfo
    __del__ = lambda self : None;
parameterInfo_swigregister = _lsf.parameterInfo_swigregister
parameterInfo_swigregister(parameterInfo)

ADMIN_USERSHARES = _lsf.ADMIN_USERSHARES
ADMIN_FULL = _lsf.ADMIN_FULL
GROUP_MAX = _lsf.GROUP_MAX
GROUP_JLP = _lsf.GROUP_JLP
USER_JLP = _lsf.USER_JLP
HOST_JLU = _lsf.HOST_JLU
MINI_JOB = _lsf.MINI_JOB
LEAST_RUN_TIME = _lsf.LEAST_RUN_TIME
OPTIMAL_MINI_JOB = _lsf.OPTIMAL_MINI_JOB
RESOURCE_ONLY = _lsf.RESOURCE_ONLY
COUNT_PREEMPTABLE = _lsf.COUNT_PREEMPTABLE
HIGH_QUEUE_PRIORITY = _lsf.HIGH_QUEUE_PRIORITY
PREEMPTABLE_QUEUE_PRIORITY = _lsf.PREEMPTABLE_QUEUE_PRIORITY
PENDING_WHEN_NOSLOTS = _lsf.PENDING_WHEN_NOSLOTS
CAL_FORCE = _lsf.CAL_FORCE
PREEMPT_JOBTYPE_EXCLUSIVE = _lsf.PREEMPT_JOBTYPE_EXCLUSIVE
PREEMPT_JOBTYPE_BACKFILL = _lsf.PREEMPT_JOBTYPE_BACKFILL
class calendarInfoEnt(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, calendarInfoEnt, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, calendarInfoEnt, name)
    __repr__ = _swig_repr
    __swig_setmethods__["name"] = _lsf.calendarInfoEnt_name_set
    __swig_getmethods__["name"] = _lsf.calendarInfoEnt_name_get
    if _newclass:name = property(_lsf.calendarInfoEnt_name_get, _lsf.calendarInfoEnt_name_set)
    __swig_setmethods__["desc"] = _lsf.calendarInfoEnt_desc_set
    __swig_getmethods__["desc"] = _lsf.calendarInfoEnt_desc_get
    if _newclass:desc = property(_lsf.calendarInfoEnt_desc_get, _lsf.calendarInfoEnt_desc_set)
    __swig_setmethods__["calExpr"] = _lsf.calendarInfoEnt_calExpr_set
    __swig_getmethods__["calExpr"] = _lsf.calendarInfoEnt_calExpr_get
    if _newclass:calExpr = property(_lsf.calendarInfoEnt_calExpr_get, _lsf.calendarInfoEnt_calExpr_set)
    __swig_setmethods__["userName"] = _lsf.calendarInfoEnt_userName_set
    __swig_getmethods__["userName"] = _lsf.calendarInfoEnt_userName_get
    if _newclass:userName = property(_lsf.calendarInfoEnt_userName_get, _lsf.calendarInfoEnt_userName_set)
    __swig_setmethods__["status"] = _lsf.calendarInfoEnt_status_set
    __swig_getmethods__["status"] = _lsf.calendarInfoEnt_status_get
    if _newclass:status = property(_lsf.calendarInfoEnt_status_get, _lsf.calendarInfoEnt_status_set)
    __swig_setmethods__["options"] = _lsf.calendarInfoEnt_options_set
    __swig_getmethods__["options"] = _lsf.calendarInfoEnt_options_get
    if _newclass:options = property(_lsf.calendarInfoEnt_options_get, _lsf.calendarInfoEnt_options_set)
    __swig_setmethods__["lastDay"] = _lsf.calendarInfoEnt_lastDay_set
    __swig_getmethods__["lastDay"] = _lsf.calendarInfoEnt_lastDay_get
    if _newclass:lastDay = property(_lsf.calendarInfoEnt_lastDay_get, _lsf.calendarInfoEnt_lastDay_set)
    __swig_setmethods__["nextDay"] = _lsf.calendarInfoEnt_nextDay_set
    __swig_getmethods__["nextDay"] = _lsf.calendarInfoEnt_nextDay_get
    if _newclass:nextDay = property(_lsf.calendarInfoEnt_nextDay_get, _lsf.calendarInfoEnt_nextDay_set)
    __swig_setmethods__["creatTime"] = _lsf.calendarInfoEnt_creatTime_set
    __swig_getmethods__["creatTime"] = _lsf.calendarInfoEnt_creatTime_get
    if _newclass:creatTime = property(_lsf.calendarInfoEnt_creatTime_get, _lsf.calendarInfoEnt_creatTime_set)
    __swig_setmethods__["lastModifyTime"] = _lsf.calendarInfoEnt_lastModifyTime_set
    __swig_getmethods__["lastModifyTime"] = _lsf.calendarInfoEnt_lastModifyTime_get
    if _newclass:lastModifyTime = property(_lsf.calendarInfoEnt_lastModifyTime_get, _lsf.calendarInfoEnt_lastModifyTime_set)
    __swig_setmethods__["flags"] = _lsf.calendarInfoEnt_flags_set
    __swig_getmethods__["flags"] = _lsf.calendarInfoEnt_flags_get
    if _newclass:flags = property(_lsf.calendarInfoEnt_flags_get, _lsf.calendarInfoEnt_flags_set)
    def __init__(self, *args): 
        this = _lsf.new_calendarInfoEnt(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _lsf.delete_calendarInfoEnt
    __del__ = lambda self : None;
calendarInfoEnt_swigregister = _lsf.calendarInfoEnt_swigregister
calendarInfoEnt_swigregister(calendarInfoEnt)

ALL_CALENDARS = _lsf.ALL_CALENDARS
EVE_HIST = _lsf.EVE_HIST
EVENT_ACTIVE = _lsf.EVENT_ACTIVE
EVENT_INACTIVE = _lsf.EVENT_INACTIVE
EVENT_REJECT = _lsf.EVENT_REJECT
EVENT_TYPE_UNKNOWN = _lsf.EVENT_TYPE_UNKNOWN
EVENT_TYPE_LATCHED = _lsf.EVENT_TYPE_LATCHED
EVENT_TYPE_PULSEALL = _lsf.EVENT_TYPE_PULSEALL
EVENT_TYPE_PULSE = _lsf.EVENT_TYPE_PULSE
EVENT_TYPE_EXCLUSIVE = _lsf.EVENT_TYPE_EXCLUSIVE
EV_UNDEF = _lsf.EV_UNDEF
EV_FILE = _lsf.EV_FILE
EV_EXCEPT = _lsf.EV_EXCEPT
EV_USER = _lsf.EV_USER
class loadInfoEnt(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, loadInfoEnt, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, loadInfoEnt, name)
    __repr__ = _swig_repr
    __swig_setmethods__["hostName"] = _lsf.loadInfoEnt_hostName_set
    __swig_getmethods__["hostName"] = _lsf.loadInfoEnt_hostName_get
    if _newclass:hostName = property(_lsf.loadInfoEnt_hostName_get, _lsf.loadInfoEnt_hostName_set)
    __swig_setmethods__["status"] = _lsf.loadInfoEnt_status_set
    __swig_getmethods__["status"] = _lsf.loadInfoEnt_status_get
    if _newclass:status = property(_lsf.loadInfoEnt_status_get, _lsf.loadInfoEnt_status_set)
    __swig_setmethods__["load"] = _lsf.loadInfoEnt_load_set
    __swig_getmethods__["load"] = _lsf.loadInfoEnt_load_get
    if _newclass:load = property(_lsf.loadInfoEnt_load_get, _lsf.loadInfoEnt_load_set)
    def __init__(self, *args): 
        this = _lsf.new_loadInfoEnt(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _lsf.delete_loadInfoEnt
    __del__ = lambda self : None;
loadInfoEnt_swigregister = _lsf.loadInfoEnt_swigregister
loadInfoEnt_swigregister(loadInfoEnt)

class queuePairEnt(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, queuePairEnt, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, queuePairEnt, name)
    __repr__ = _swig_repr
    __swig_setmethods__["local"] = _lsf.queuePairEnt_local_set
    __swig_getmethods__["local"] = _lsf.queuePairEnt_local_get
    if _newclass:local = property(_lsf.queuePairEnt_local_get, _lsf.queuePairEnt_local_set)
    __swig_setmethods__["remote"] = _lsf.queuePairEnt_remote_set
    __swig_getmethods__["remote"] = _lsf.queuePairEnt_remote_get
    if _newclass:remote = property(_lsf.queuePairEnt_remote_get, _lsf.queuePairEnt_remote_set)
    __swig_setmethods__["send"] = _lsf.queuePairEnt_send_set
    __swig_getmethods__["send"] = _lsf.queuePairEnt_send_get
    if _newclass:send = property(_lsf.queuePairEnt_send_get, _lsf.queuePairEnt_send_set)
    __swig_setmethods__["status"] = _lsf.queuePairEnt_status_set
    __swig_getmethods__["status"] = _lsf.queuePairEnt_status_get
    if _newclass:status = property(_lsf.queuePairEnt_status_get, _lsf.queuePairEnt_status_set)
    def __init__(self, *args): 
        this = _lsf.new_queuePairEnt(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _lsf.delete_queuePairEnt
    __del__ = lambda self : None;
queuePairEnt_swigregister = _lsf.queuePairEnt_swigregister
queuePairEnt_swigregister(queuePairEnt)

class rmbCluAppEnt(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, rmbCluAppEnt, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, rmbCluAppEnt, name)
    __repr__ = _swig_repr
    __swig_setmethods__["name"] = _lsf.rmbCluAppEnt_name_set
    __swig_getmethods__["name"] = _lsf.rmbCluAppEnt_name_get
    if _newclass:name = property(_lsf.rmbCluAppEnt_name_get, _lsf.rmbCluAppEnt_name_set)
    __swig_setmethods__["description"] = _lsf.rmbCluAppEnt_description_set
    __swig_getmethods__["description"] = _lsf.rmbCluAppEnt_description_get
    if _newclass:description = property(_lsf.rmbCluAppEnt_description_get, _lsf.rmbCluAppEnt_description_set)
    def __init__(self, *args): 
        this = _lsf.new_rmbCluAppEnt(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _lsf.delete_rmbCluAppEnt
    __del__ = lambda self : None;
rmbCluAppEnt_swigregister = _lsf.rmbCluAppEnt_swigregister
rmbCluAppEnt_swigregister(rmbCluAppEnt)

LEASE_CLU_STAT_DISC = _lsf.LEASE_CLU_STAT_DISC
LEASE_CLU_STAT_CONN = _lsf.LEASE_CLU_STAT_CONN
LEASE_CLU_STAT_OK = _lsf.LEASE_CLU_STAT_OK
LEASE_CLU_STAT_NUMBER = _lsf.LEASE_CLU_STAT_NUMBER
class consumerCluEnt(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, consumerCluEnt, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, consumerCluEnt, name)
    __repr__ = _swig_repr
    __swig_setmethods__["cluName"] = _lsf.consumerCluEnt_cluName_set
    __swig_getmethods__["cluName"] = _lsf.consumerCluEnt_cluName_get
    if _newclass:cluName = property(_lsf.consumerCluEnt_cluName_get, _lsf.consumerCluEnt_cluName_set)
    __swig_setmethods__["status"] = _lsf.consumerCluEnt_status_set
    __swig_getmethods__["status"] = _lsf.consumerCluEnt_status_get
    if _newclass:status = property(_lsf.consumerCluEnt_status_get, _lsf.consumerCluEnt_status_set)
    def __init__(self, *args): 
        this = _lsf.new_consumerCluEnt(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _lsf.delete_consumerCluEnt
    __del__ = lambda self : None;
consumerCluEnt_swigregister = _lsf.consumerCluEnt_swigregister
consumerCluEnt_swigregister(consumerCluEnt)

class providerCluEnt(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, providerCluEnt, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, providerCluEnt, name)
    __repr__ = _swig_repr
    __swig_setmethods__["cluName"] = _lsf.providerCluEnt_cluName_set
    __swig_getmethods__["cluName"] = _lsf.providerCluEnt_cluName_get
    if _newclass:cluName = property(_lsf.providerCluEnt_cluName_get, _lsf.providerCluEnt_cluName_set)
    __swig_setmethods__["status"] = _lsf.providerCluEnt_status_set
    __swig_getmethods__["status"] = _lsf.providerCluEnt_status_get
    if _newclass:status = property(_lsf.providerCluEnt_status_get, _lsf.providerCluEnt_status_set)
    def __init__(self, *args): 
        this = _lsf.new_providerCluEnt(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _lsf.delete_providerCluEnt
    __del__ = lambda self : None;
providerCluEnt_swigregister = _lsf.providerCluEnt_swigregister
providerCluEnt_swigregister(providerCluEnt)

class rmbCluInfoEnt(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, rmbCluInfoEnt, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, rmbCluInfoEnt, name)
    __repr__ = _swig_repr
    __swig_setmethods__["cluster"] = _lsf.rmbCluInfoEnt_cluster_set
    __swig_getmethods__["cluster"] = _lsf.rmbCluInfoEnt_cluster_get
    if _newclass:cluster = property(_lsf.rmbCluInfoEnt_cluster_get, _lsf.rmbCluInfoEnt_cluster_set)
    __swig_setmethods__["numPairs"] = _lsf.rmbCluInfoEnt_numPairs_set
    __swig_getmethods__["numPairs"] = _lsf.rmbCluInfoEnt_numPairs_get
    if _newclass:numPairs = property(_lsf.rmbCluInfoEnt_numPairs_get, _lsf.rmbCluInfoEnt_numPairs_set)
    __swig_setmethods__["queues"] = _lsf.rmbCluInfoEnt_queues_set
    __swig_getmethods__["queues"] = _lsf.rmbCluInfoEnt_queues_get
    if _newclass:queues = property(_lsf.rmbCluInfoEnt_queues_get, _lsf.rmbCluInfoEnt_queues_set)
    __swig_setmethods__["numApps"] = _lsf.rmbCluInfoEnt_numApps_set
    __swig_getmethods__["numApps"] = _lsf.rmbCluInfoEnt_numApps_get
    if _newclass:numApps = property(_lsf.rmbCluInfoEnt_numApps_get, _lsf.rmbCluInfoEnt_numApps_set)
    __swig_setmethods__["apps"] = _lsf.rmbCluInfoEnt_apps_set
    __swig_getmethods__["apps"] = _lsf.rmbCluInfoEnt_apps_get
    if _newclass:apps = property(_lsf.rmbCluInfoEnt_apps_get, _lsf.rmbCluInfoEnt_apps_set)
    def __init__(self, *args): 
        this = _lsf.new_rmbCluInfoEnt(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _lsf.delete_rmbCluInfoEnt
    __del__ = lambda self : None;
rmbCluInfoEnt_swigregister = _lsf.rmbCluInfoEnt_swigregister
rmbCluInfoEnt_swigregister(rmbCluInfoEnt)

class leaseCluInfoEnt(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, leaseCluInfoEnt, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, leaseCluInfoEnt, name)
    __repr__ = _swig_repr
    __swig_setmethods__["flags"] = _lsf.leaseCluInfoEnt_flags_set
    __swig_getmethods__["flags"] = _lsf.leaseCluInfoEnt_flags_get
    if _newclass:flags = property(_lsf.leaseCluInfoEnt_flags_get, _lsf.leaseCluInfoEnt_flags_set)
    __swig_setmethods__["numConsumer"] = _lsf.leaseCluInfoEnt_numConsumer_set
    __swig_getmethods__["numConsumer"] = _lsf.leaseCluInfoEnt_numConsumer_get
    if _newclass:numConsumer = property(_lsf.leaseCluInfoEnt_numConsumer_get, _lsf.leaseCluInfoEnt_numConsumer_set)
    __swig_setmethods__["consumerClus"] = _lsf.leaseCluInfoEnt_consumerClus_set
    __swig_getmethods__["consumerClus"] = _lsf.leaseCluInfoEnt_consumerClus_get
    if _newclass:consumerClus = property(_lsf.leaseCluInfoEnt_consumerClus_get, _lsf.leaseCluInfoEnt_consumerClus_set)
    __swig_setmethods__["numProvider"] = _lsf.leaseCluInfoEnt_numProvider_set
    __swig_getmethods__["numProvider"] = _lsf.leaseCluInfoEnt_numProvider_get
    if _newclass:numProvider = property(_lsf.leaseCluInfoEnt_numProvider_get, _lsf.leaseCluInfoEnt_numProvider_set)
    __swig_setmethods__["providerClus"] = _lsf.leaseCluInfoEnt_providerClus_set
    __swig_getmethods__["providerClus"] = _lsf.leaseCluInfoEnt_providerClus_get
    if _newclass:providerClus = property(_lsf.leaseCluInfoEnt_providerClus_get, _lsf.leaseCluInfoEnt_providerClus_set)
    def __init__(self, *args): 
        this = _lsf.new_leaseCluInfoEnt(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _lsf.delete_leaseCluInfoEnt
    __del__ = lambda self : None;
leaseCluInfoEnt_swigregister = _lsf.leaseCluInfoEnt_swigregister
leaseCluInfoEnt_swigregister(leaseCluInfoEnt)

class clusterInfoEnt(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, clusterInfoEnt, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, clusterInfoEnt, name)
    __repr__ = _swig_repr
    __swig_setmethods__["cluster"] = _lsf.clusterInfoEnt_cluster_set
    __swig_getmethods__["cluster"] = _lsf.clusterInfoEnt_cluster_get
    if _newclass:cluster = property(_lsf.clusterInfoEnt_cluster_get, _lsf.clusterInfoEnt_cluster_set)
    __swig_setmethods__["numPairs"] = _lsf.clusterInfoEnt_numPairs_set
    __swig_getmethods__["numPairs"] = _lsf.clusterInfoEnt_numPairs_get
    if _newclass:numPairs = property(_lsf.clusterInfoEnt_numPairs_get, _lsf.clusterInfoEnt_numPairs_set)
    __swig_setmethods__["queues"] = _lsf.clusterInfoEnt_queues_set
    __swig_getmethods__["queues"] = _lsf.clusterInfoEnt_queues_get
    if _newclass:queues = property(_lsf.clusterInfoEnt_queues_get, _lsf.clusterInfoEnt_queues_set)
    __swig_setmethods__["numApps"] = _lsf.clusterInfoEnt_numApps_set
    __swig_getmethods__["numApps"] = _lsf.clusterInfoEnt_numApps_get
    if _newclass:numApps = property(_lsf.clusterInfoEnt_numApps_get, _lsf.clusterInfoEnt_numApps_set)
    __swig_setmethods__["apps"] = _lsf.clusterInfoEnt_apps_set
    __swig_getmethods__["apps"] = _lsf.clusterInfoEnt_apps_get
    if _newclass:apps = property(_lsf.clusterInfoEnt_apps_get, _lsf.clusterInfoEnt_apps_set)
    def __init__(self, *args): 
        this = _lsf.new_clusterInfoEnt(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _lsf.delete_clusterInfoEnt
    __del__ = lambda self : None;
clusterInfoEnt_swigregister = _lsf.clusterInfoEnt_swigregister
clusterInfoEnt_swigregister(clusterInfoEnt)

class clusterInfoEntEx(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, clusterInfoEntEx, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, clusterInfoEntEx, name)
    __repr__ = _swig_repr
    __swig_setmethods__["rmbCluInfo"] = _lsf.clusterInfoEntEx_rmbCluInfo_set
    __swig_getmethods__["rmbCluInfo"] = _lsf.clusterInfoEntEx_rmbCluInfo_get
    if _newclass:rmbCluInfo = property(_lsf.clusterInfoEntEx_rmbCluInfo_get, _lsf.clusterInfoEntEx_rmbCluInfo_set)
    __swig_setmethods__["leaseCluInfo"] = _lsf.clusterInfoEntEx_leaseCluInfo_set
    __swig_getmethods__["leaseCluInfo"] = _lsf.clusterInfoEntEx_leaseCluInfo_get
    if _newclass:leaseCluInfo = property(_lsf.clusterInfoEntEx_leaseCluInfo_get, _lsf.clusterInfoEntEx_leaseCluInfo_set)
    def __init__(self, *args): 
        this = _lsf.new_clusterInfoEntEx(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _lsf.delete_clusterInfoEntEx
    __del__ = lambda self : None;
clusterInfoEntEx_swigregister = _lsf.clusterInfoEntEx_swigregister
clusterInfoEntEx_swigregister(clusterInfoEntEx)

class eventInfoEnt(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, eventInfoEnt, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, eventInfoEnt, name)
    __repr__ = _swig_repr
    __swig_setmethods__["name"] = _lsf.eventInfoEnt_name_set
    __swig_getmethods__["name"] = _lsf.eventInfoEnt_name_get
    if _newclass:name = property(_lsf.eventInfoEnt_name_get, _lsf.eventInfoEnt_name_set)
    __swig_setmethods__["status"] = _lsf.eventInfoEnt_status_set
    __swig_getmethods__["status"] = _lsf.eventInfoEnt_status_get
    if _newclass:status = property(_lsf.eventInfoEnt_status_get, _lsf.eventInfoEnt_status_set)
    __swig_setmethods__["type"] = _lsf.eventInfoEnt_type_set
    __swig_getmethods__["type"] = _lsf.eventInfoEnt_type_get
    if _newclass:type = property(_lsf.eventInfoEnt_type_get, _lsf.eventInfoEnt_type_set)
    __swig_setmethods__["eType"] = _lsf.eventInfoEnt_eType_set
    __swig_getmethods__["eType"] = _lsf.eventInfoEnt_eType_get
    if _newclass:eType = property(_lsf.eventInfoEnt_eType_get, _lsf.eventInfoEnt_eType_set)
    __swig_setmethods__["userName"] = _lsf.eventInfoEnt_userName_set
    __swig_getmethods__["userName"] = _lsf.eventInfoEnt_userName_get
    if _newclass:userName = property(_lsf.eventInfoEnt_userName_get, _lsf.eventInfoEnt_userName_set)
    __swig_setmethods__["attributes"] = _lsf.eventInfoEnt_attributes_set
    __swig_getmethods__["attributes"] = _lsf.eventInfoEnt_attributes_get
    if _newclass:attributes = property(_lsf.eventInfoEnt_attributes_get, _lsf.eventInfoEnt_attributes_set)
    __swig_setmethods__["numDependents"] = _lsf.eventInfoEnt_numDependents_set
    __swig_getmethods__["numDependents"] = _lsf.eventInfoEnt_numDependents_get
    if _newclass:numDependents = property(_lsf.eventInfoEnt_numDependents_get, _lsf.eventInfoEnt_numDependents_set)
    __swig_setmethods__["updateTime"] = _lsf.eventInfoEnt_updateTime_set
    __swig_getmethods__["updateTime"] = _lsf.eventInfoEnt_updateTime_get
    if _newclass:updateTime = property(_lsf.eventInfoEnt_updateTime_get, _lsf.eventInfoEnt_updateTime_set)
    __swig_setmethods__["lastDisJob"] = _lsf.eventInfoEnt_lastDisJob_set
    __swig_getmethods__["lastDisJob"] = _lsf.eventInfoEnt_lastDisJob_get
    if _newclass:lastDisJob = property(_lsf.eventInfoEnt_lastDisJob_get, _lsf.eventInfoEnt_lastDisJob_set)
    __swig_setmethods__["lastDisTime"] = _lsf.eventInfoEnt_lastDisTime_set
    __swig_getmethods__["lastDisTime"] = _lsf.eventInfoEnt_lastDisTime_get
    if _newclass:lastDisTime = property(_lsf.eventInfoEnt_lastDisTime_get, _lsf.eventInfoEnt_lastDisTime_set)
    def __init__(self, *args): 
        this = _lsf.new_eventInfoEnt(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _lsf.delete_eventInfoEnt
    __del__ = lambda self : None;
eventInfoEnt_swigregister = _lsf.eventInfoEnt_swigregister
eventInfoEnt_swigregister(eventInfoEnt)

ALL_EVENTS = _lsf.ALL_EVENTS
USER_GRP = _lsf.USER_GRP
HOST_GRP = _lsf.HOST_GRP
HPART_HGRP = _lsf.HPART_HGRP
GRP_RECURSIVE = _lsf.GRP_RECURSIVE
GRP_ALL = _lsf.GRP_ALL
NQSQ_GRP = _lsf.NQSQ_GRP
GRP_SHARES = _lsf.GRP_SHARES
DYNAMIC_GRP = _lsf.DYNAMIC_GRP
GRP_CU = _lsf.GRP_CU
class userShares(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, userShares, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, userShares, name)
    __repr__ = _swig_repr
    __swig_setmethods__["user"] = _lsf.userShares_user_set
    __swig_getmethods__["user"] = _lsf.userShares_user_get
    if _newclass:user = property(_lsf.userShares_user_get, _lsf.userShares_user_set)
    __swig_setmethods__["shares"] = _lsf.userShares_shares_set
    __swig_getmethods__["shares"] = _lsf.userShares_shares_get
    if _newclass:shares = property(_lsf.userShares_shares_get, _lsf.userShares_shares_set)
    def __init__(self, *args): 
        this = _lsf.new_userShares(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _lsf.delete_userShares
    __del__ = lambda self : None;
userShares_swigregister = _lsf.userShares_swigregister
userShares_swigregister(userShares)

class adminRight(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, adminRight, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, adminRight, name)
    __repr__ = _swig_repr
    __swig_setmethods__["value"] = _lsf.adminRight_value_set
    __swig_getmethods__["value"] = _lsf.adminRight_value_get
    if _newclass:value = property(_lsf.adminRight_value_get, _lsf.adminRight_value_set)
    __swig_setmethods__["string"] = _lsf.adminRight_string_set
    __swig_getmethods__["string"] = _lsf.adminRight_string_get
    if _newclass:string = property(_lsf.adminRight_string_get, _lsf.adminRight_string_set)
    def __init__(self, *args): 
        this = _lsf.new_adminRight(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _lsf.delete_adminRight
    __del__ = lambda self : None;
adminRight_swigregister = _lsf.adminRight_swigregister
adminRight_swigregister(adminRight)

class groupInfoEnt(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, groupInfoEnt, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, groupInfoEnt, name)
    __repr__ = _swig_repr
    __swig_setmethods__["group"] = _lsf.groupInfoEnt_group_set
    __swig_getmethods__["group"] = _lsf.groupInfoEnt_group_get
    if _newclass:group = property(_lsf.groupInfoEnt_group_get, _lsf.groupInfoEnt_group_set)
    __swig_setmethods__["memberList"] = _lsf.groupInfoEnt_memberList_set
    __swig_getmethods__["memberList"] = _lsf.groupInfoEnt_memberList_get
    if _newclass:memberList = property(_lsf.groupInfoEnt_memberList_get, _lsf.groupInfoEnt_memberList_set)
    __swig_setmethods__["adminMemberList"] = _lsf.groupInfoEnt_adminMemberList_set
    __swig_getmethods__["adminMemberList"] = _lsf.groupInfoEnt_adminMemberList_get
    if _newclass:adminMemberList = property(_lsf.groupInfoEnt_adminMemberList_get, _lsf.groupInfoEnt_adminMemberList_set)
    __swig_setmethods__["numUserShares"] = _lsf.groupInfoEnt_numUserShares_set
    __swig_getmethods__["numUserShares"] = _lsf.groupInfoEnt_numUserShares_get
    if _newclass:numUserShares = property(_lsf.groupInfoEnt_numUserShares_get, _lsf.groupInfoEnt_numUserShares_set)
    __swig_setmethods__["userShares"] = _lsf.groupInfoEnt_userShares_set
    __swig_getmethods__["userShares"] = _lsf.groupInfoEnt_userShares_get
    if _newclass:userShares = property(_lsf.groupInfoEnt_userShares_get, _lsf.groupInfoEnt_userShares_set)
    __swig_setmethods__["hostStr"] = _lsf.groupInfoEnt_hostStr_set
    __swig_getmethods__["hostStr"] = _lsf.groupInfoEnt_hostStr_get
    if _newclass:hostStr = property(_lsf.groupInfoEnt_hostStr_get, _lsf.groupInfoEnt_hostStr_set)
    __swig_setmethods__["options"] = _lsf.groupInfoEnt_options_set
    __swig_getmethods__["options"] = _lsf.groupInfoEnt_options_get
    if _newclass:options = property(_lsf.groupInfoEnt_options_get, _lsf.groupInfoEnt_options_set)
    __swig_setmethods__["pattern"] = _lsf.groupInfoEnt_pattern_set
    __swig_getmethods__["pattern"] = _lsf.groupInfoEnt_pattern_get
    if _newclass:pattern = property(_lsf.groupInfoEnt_pattern_get, _lsf.groupInfoEnt_pattern_set)
    __swig_setmethods__["neg_pattern"] = _lsf.groupInfoEnt_neg_pattern_set
    __swig_getmethods__["neg_pattern"] = _lsf.groupInfoEnt_neg_pattern_get
    if _newclass:neg_pattern = property(_lsf.groupInfoEnt_neg_pattern_get, _lsf.groupInfoEnt_neg_pattern_set)
    __swig_setmethods__["cu_type"] = _lsf.groupInfoEnt_cu_type_set
    __swig_getmethods__["cu_type"] = _lsf.groupInfoEnt_cu_type_get
    if _newclass:cu_type = property(_lsf.groupInfoEnt_cu_type_get, _lsf.groupInfoEnt_cu_type_set)
    def __init__(self, *args): 
        this = _lsf.new_groupInfoEnt(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _lsf.delete_groupInfoEnt
    __del__ = lambda self : None;
groupInfoEnt_swigregister = _lsf.groupInfoEnt_swigregister
groupInfoEnt_swigregister(groupInfoEnt)
GRP_NO_CONDENSE_OUTPUT = _lsf.GRP_NO_CONDENSE_OUTPUT
GRP_CONDENSE_OUTPUT = _lsf.GRP_CONDENSE_OUTPUT
GRP_HAVE_REG_EXP = _lsf.GRP_HAVE_REG_EXP
GRP_SERVICE_CLASS = _lsf.GRP_SERVICE_CLASS
GRP_IS_CU = _lsf.GRP_IS_CU
GRP_IS_EGROUP = _lsf.GRP_IS_EGROUP
GRP_IS_HP = _lsf.GRP_IS_HP
GRP_IS_QUEUE = _lsf.GRP_IS_QUEUE
GRP_IS_UGRP = _lsf.GRP_IS_UGRP
GRP_HAS_PARENT = _lsf.GRP_HAS_PARENT
GRP_CACHE_UGINFO = _lsf.GRP_CACHE_UGINFO
GRP_CACHE_UGDATA = _lsf.GRP_CACHE_UGDATA
GRP_DELETED = _lsf.GRP_DELETED
GRP_SLA_NAME = _lsf.GRP_SLA_NAME

class runJobRequest(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, runJobRequest, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, runJobRequest, name)
    __repr__ = _swig_repr
    __swig_setmethods__["jobId"] = _lsf.runJobRequest_jobId_set
    __swig_getmethods__["jobId"] = _lsf.runJobRequest_jobId_get
    if _newclass:jobId = property(_lsf.runJobRequest_jobId_get, _lsf.runJobRequest_jobId_set)
    __swig_setmethods__["numHosts"] = _lsf.runJobRequest_numHosts_set
    __swig_getmethods__["numHosts"] = _lsf.runJobRequest_numHosts_get
    if _newclass:numHosts = property(_lsf.runJobRequest_numHosts_get, _lsf.runJobRequest_numHosts_set)
    __swig_setmethods__["hostname"] = _lsf.runJobRequest_hostname_set
    __swig_getmethods__["hostname"] = _lsf.runJobRequest_hostname_get
    if _newclass:hostname = property(_lsf.runJobRequest_hostname_get, _lsf.runJobRequest_hostname_set)
    __swig_setmethods__["options"] = _lsf.runJobRequest_options_set
    __swig_getmethods__["options"] = _lsf.runJobRequest_options_get
    if _newclass:options = property(_lsf.runJobRequest_options_get, _lsf.runJobRequest_options_set)
    __swig_setmethods__["slots"] = _lsf.runJobRequest_slots_set
    __swig_getmethods__["slots"] = _lsf.runJobRequest_slots_get
    if _newclass:slots = property(_lsf.runJobRequest_slots_get, _lsf.runJobRequest_slots_set)
    def __init__(self, *args): 
        this = _lsf.new_runJobRequest(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _lsf.delete_runJobRequest
    __del__ = lambda self : None;
runJobRequest_swigregister = _lsf.runJobRequest_swigregister
runJobRequest_swigregister(runJobRequest)
RUNJOB_OPT_NORMAL = _lsf.RUNJOB_OPT_NORMAL
RUNJOB_OPT_NOSTOP = _lsf.RUNJOB_OPT_NOSTOP
RUNJOB_OPT_PENDONLY = _lsf.RUNJOB_OPT_PENDONLY
RUNJOB_OPT_FROM_BEGIN = _lsf.RUNJOB_OPT_FROM_BEGIN
RUNJOB_OPT_FREE = _lsf.RUNJOB_OPT_FREE
RUNJOB_OPT_IGNORE_RUSAGE = _lsf.RUNJOB_OPT_IGNORE_RUSAGE

EXT_MSG_POST = _lsf.EXT_MSG_POST
EXT_ATTA_POST = _lsf.EXT_ATTA_POST
EXT_MSG_READ = _lsf.EXT_MSG_READ
EXT_ATTA_READ = _lsf.EXT_ATTA_READ
EXT_MSG_REPLAY = _lsf.EXT_MSG_REPLAY
EXT_MSG_POST_NOEVENT = _lsf.EXT_MSG_POST_NOEVENT
class jobExternalMsgReq(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, jobExternalMsgReq, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, jobExternalMsgReq, name)
    __repr__ = _swig_repr
    __swig_setmethods__["options"] = _lsf.jobExternalMsgReq_options_set
    __swig_getmethods__["options"] = _lsf.jobExternalMsgReq_options_get
    if _newclass:options = property(_lsf.jobExternalMsgReq_options_get, _lsf.jobExternalMsgReq_options_set)
    __swig_setmethods__["jobId"] = _lsf.jobExternalMsgReq_jobId_set
    __swig_getmethods__["jobId"] = _lsf.jobExternalMsgReq_jobId_get
    if _newclass:jobId = property(_lsf.jobExternalMsgReq_jobId_get, _lsf.jobExternalMsgReq_jobId_set)
    __swig_setmethods__["jobName"] = _lsf.jobExternalMsgReq_jobName_set
    __swig_getmethods__["jobName"] = _lsf.jobExternalMsgReq_jobName_get
    if _newclass:jobName = property(_lsf.jobExternalMsgReq_jobName_get, _lsf.jobExternalMsgReq_jobName_set)
    __swig_setmethods__["msgIdx"] = _lsf.jobExternalMsgReq_msgIdx_set
    __swig_getmethods__["msgIdx"] = _lsf.jobExternalMsgReq_msgIdx_get
    if _newclass:msgIdx = property(_lsf.jobExternalMsgReq_msgIdx_get, _lsf.jobExternalMsgReq_msgIdx_set)
    __swig_setmethods__["desc"] = _lsf.jobExternalMsgReq_desc_set
    __swig_getmethods__["desc"] = _lsf.jobExternalMsgReq_desc_get
    if _newclass:desc = property(_lsf.jobExternalMsgReq_desc_get, _lsf.jobExternalMsgReq_desc_set)
    __swig_setmethods__["userId"] = _lsf.jobExternalMsgReq_userId_set
    __swig_getmethods__["userId"] = _lsf.jobExternalMsgReq_userId_get
    if _newclass:userId = property(_lsf.jobExternalMsgReq_userId_get, _lsf.jobExternalMsgReq_userId_set)
    __swig_setmethods__["dataSize"] = _lsf.jobExternalMsgReq_dataSize_set
    __swig_getmethods__["dataSize"] = _lsf.jobExternalMsgReq_dataSize_get
    if _newclass:dataSize = property(_lsf.jobExternalMsgReq_dataSize_get, _lsf.jobExternalMsgReq_dataSize_set)
    __swig_setmethods__["postTime"] = _lsf.jobExternalMsgReq_postTime_set
    __swig_getmethods__["postTime"] = _lsf.jobExternalMsgReq_postTime_get
    if _newclass:postTime = property(_lsf.jobExternalMsgReq_postTime_get, _lsf.jobExternalMsgReq_postTime_set)
    __swig_setmethods__["userName"] = _lsf.jobExternalMsgReq_userName_set
    __swig_getmethods__["userName"] = _lsf.jobExternalMsgReq_userName_get
    if _newclass:userName = property(_lsf.jobExternalMsgReq_userName_get, _lsf.jobExternalMsgReq_userName_set)
    def __init__(self, *args): 
        this = _lsf.new_jobExternalMsgReq(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _lsf.delete_jobExternalMsgReq
    __del__ = lambda self : None;
jobExternalMsgReq_swigregister = _lsf.jobExternalMsgReq_swigregister
jobExternalMsgReq_swigregister(jobExternalMsgReq)

EXT_DATA_UNKNOWN = _lsf.EXT_DATA_UNKNOWN
EXT_DATA_NOEXIST = _lsf.EXT_DATA_NOEXIST
EXT_DATA_AVAIL = _lsf.EXT_DATA_AVAIL
EXT_DATA_UNAVAIL = _lsf.EXT_DATA_UNAVAIL
class jobExternalMsgReply(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, jobExternalMsgReply, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, jobExternalMsgReply, name)
    __repr__ = _swig_repr
    __swig_setmethods__["jobId"] = _lsf.jobExternalMsgReply_jobId_set
    __swig_getmethods__["jobId"] = _lsf.jobExternalMsgReply_jobId_get
    if _newclass:jobId = property(_lsf.jobExternalMsgReply_jobId_get, _lsf.jobExternalMsgReply_jobId_set)
    __swig_setmethods__["msgIdx"] = _lsf.jobExternalMsgReply_msgIdx_set
    __swig_getmethods__["msgIdx"] = _lsf.jobExternalMsgReply_msgIdx_get
    if _newclass:msgIdx = property(_lsf.jobExternalMsgReply_msgIdx_get, _lsf.jobExternalMsgReply_msgIdx_set)
    __swig_setmethods__["desc"] = _lsf.jobExternalMsgReply_desc_set
    __swig_getmethods__["desc"] = _lsf.jobExternalMsgReply_desc_get
    if _newclass:desc = property(_lsf.jobExternalMsgReply_desc_get, _lsf.jobExternalMsgReply_desc_set)
    __swig_setmethods__["userId"] = _lsf.jobExternalMsgReply_userId_set
    __swig_getmethods__["userId"] = _lsf.jobExternalMsgReply_userId_get
    if _newclass:userId = property(_lsf.jobExternalMsgReply_userId_get, _lsf.jobExternalMsgReply_userId_set)
    __swig_setmethods__["dataSize"] = _lsf.jobExternalMsgReply_dataSize_set
    __swig_getmethods__["dataSize"] = _lsf.jobExternalMsgReply_dataSize_get
    if _newclass:dataSize = property(_lsf.jobExternalMsgReply_dataSize_get, _lsf.jobExternalMsgReply_dataSize_set)
    __swig_setmethods__["postTime"] = _lsf.jobExternalMsgReply_postTime_set
    __swig_getmethods__["postTime"] = _lsf.jobExternalMsgReply_postTime_get
    if _newclass:postTime = property(_lsf.jobExternalMsgReply_postTime_get, _lsf.jobExternalMsgReply_postTime_set)
    __swig_setmethods__["dataStatus"] = _lsf.jobExternalMsgReply_dataStatus_set
    __swig_getmethods__["dataStatus"] = _lsf.jobExternalMsgReply_dataStatus_get
    if _newclass:dataStatus = property(_lsf.jobExternalMsgReply_dataStatus_get, _lsf.jobExternalMsgReply_dataStatus_set)
    __swig_setmethods__["userName"] = _lsf.jobExternalMsgReply_userName_set
    __swig_getmethods__["userName"] = _lsf.jobExternalMsgReply_userName_get
    if _newclass:userName = property(_lsf.jobExternalMsgReply_userName_get, _lsf.jobExternalMsgReply_userName_set)
    def __init__(self, *args): 
        this = _lsf.new_jobExternalMsgReply(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _lsf.delete_jobExternalMsgReply
    __del__ = lambda self : None;
jobExternalMsgReply_swigregister = _lsf.jobExternalMsgReply_swigregister
jobExternalMsgReply_swigregister(jobExternalMsgReply)

class symJobInfo(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, symJobInfo, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, symJobInfo, name)
    __repr__ = _swig_repr
    __swig_setmethods__["partition"] = _lsf.symJobInfo_partition_set
    __swig_getmethods__["partition"] = _lsf.symJobInfo_partition_get
    if _newclass:partition = property(_lsf.symJobInfo_partition_get, _lsf.symJobInfo_partition_set)
    __swig_setmethods__["priority"] = _lsf.symJobInfo_priority_set
    __swig_getmethods__["priority"] = _lsf.symJobInfo_priority_get
    if _newclass:priority = property(_lsf.symJobInfo_priority_get, _lsf.symJobInfo_priority_set)
    __swig_setmethods__["jobFullName"] = _lsf.symJobInfo_jobFullName_set
    __swig_getmethods__["jobFullName"] = _lsf.symJobInfo_jobFullName_get
    if _newclass:jobFullName = property(_lsf.symJobInfo_jobFullName_get, _lsf.symJobInfo_jobFullName_set)
    __swig_setmethods__["auxCmdDesc"] = _lsf.symJobInfo_auxCmdDesc_set
    __swig_getmethods__["auxCmdDesc"] = _lsf.symJobInfo_auxCmdDesc_get
    if _newclass:auxCmdDesc = property(_lsf.symJobInfo_auxCmdDesc_get, _lsf.symJobInfo_auxCmdDesc_set)
    __swig_setmethods__["auxJobDesc"] = _lsf.symJobInfo_auxJobDesc_set
    __swig_getmethods__["auxJobDesc"] = _lsf.symJobInfo_auxJobDesc_get
    if _newclass:auxJobDesc = property(_lsf.symJobInfo_auxJobDesc_get, _lsf.symJobInfo_auxJobDesc_set)
    def __init__(self, *args): 
        this = _lsf.new_symJobInfo(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _lsf.delete_symJobInfo
    __del__ = lambda self : None;
symJobInfo_swigregister = _lsf.symJobInfo_swigregister
symJobInfo_swigregister(symJobInfo)

class symJobStatus(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, symJobStatus, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, symJobStatus, name)
    __repr__ = _swig_repr
    __swig_setmethods__["desc"] = _lsf.symJobStatus_desc_set
    __swig_getmethods__["desc"] = _lsf.symJobStatus_desc_get
    if _newclass:desc = property(_lsf.symJobStatus_desc_get, _lsf.symJobStatus_desc_set)
    def __init__(self, *args): 
        this = _lsf.new_symJobStatus(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _lsf.delete_symJobStatus
    __del__ = lambda self : None;
symJobStatus_swigregister = _lsf.symJobStatus_swigregister
symJobStatus_swigregister(symJobStatus)

class symJobProgress(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, symJobProgress, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, symJobProgress, name)
    __repr__ = _swig_repr
    __swig_setmethods__["desc"] = _lsf.symJobProgress_desc_set
    __swig_getmethods__["desc"] = _lsf.symJobProgress_desc_get
    if _newclass:desc = property(_lsf.symJobProgress_desc_get, _lsf.symJobProgress_desc_set)
    def __init__(self, *args): 
        this = _lsf.new_symJobProgress(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _lsf.delete_symJobProgress
    __del__ = lambda self : None;
symJobProgress_swigregister = _lsf.symJobProgress_swigregister
symJobProgress_swigregister(symJobProgress)

class symJobStatusUpdateReq(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, symJobStatusUpdateReq, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, symJobStatusUpdateReq, name)
    __repr__ = _swig_repr
    __swig_setmethods__["jobId"] = _lsf.symJobStatusUpdateReq_jobId_set
    __swig_getmethods__["jobId"] = _lsf.symJobStatusUpdateReq_jobId_get
    if _newclass:jobId = property(_lsf.symJobStatusUpdateReq_jobId_get, _lsf.symJobStatusUpdateReq_jobId_set)
    __swig_setmethods__["bitOption"] = _lsf.symJobStatusUpdateReq_bitOption_set
    __swig_getmethods__["bitOption"] = _lsf.symJobStatusUpdateReq_bitOption_get
    if _newclass:bitOption = property(_lsf.symJobStatusUpdateReq_bitOption_get, _lsf.symJobStatusUpdateReq_bitOption_set)
    __swig_setmethods__["info"] = _lsf.symJobStatusUpdateReq_info_set
    __swig_getmethods__["info"] = _lsf.symJobStatusUpdateReq_info_get
    if _newclass:info = property(_lsf.symJobStatusUpdateReq_info_get, _lsf.symJobStatusUpdateReq_info_set)
    __swig_setmethods__["numOfJobStatus"] = _lsf.symJobStatusUpdateReq_numOfJobStatus_set
    __swig_getmethods__["numOfJobStatus"] = _lsf.symJobStatusUpdateReq_numOfJobStatus_get
    if _newclass:numOfJobStatus = property(_lsf.symJobStatusUpdateReq_numOfJobStatus_get, _lsf.symJobStatusUpdateReq_numOfJobStatus_set)
    __swig_setmethods__["status"] = _lsf.symJobStatusUpdateReq_status_set
    __swig_getmethods__["status"] = _lsf.symJobStatusUpdateReq_status_get
    if _newclass:status = property(_lsf.symJobStatusUpdateReq_status_get, _lsf.symJobStatusUpdateReq_status_set)
    __swig_setmethods__["progress"] = _lsf.symJobStatusUpdateReq_progress_set
    __swig_getmethods__["progress"] = _lsf.symJobStatusUpdateReq_progress_get
    if _newclass:progress = property(_lsf.symJobStatusUpdateReq_progress_get, _lsf.symJobStatusUpdateReq_progress_set)
    def __init__(self, *args): 
        this = _lsf.new_symJobStatusUpdateReq(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _lsf.delete_symJobStatusUpdateReq
    __del__ = lambda self : None;
symJobStatusUpdateReq_swigregister = _lsf.symJobStatusUpdateReq_swigregister
symJobStatusUpdateReq_swigregister(symJobStatusUpdateReq)
SYM_JOB_UPDATE_NONE = _lsf.SYM_JOB_UPDATE_NONE
SYM_JOB_UPDATE_INFO = _lsf.SYM_JOB_UPDATE_INFO
SYM_JOB_UPDATE_STATUS = _lsf.SYM_JOB_UPDATE_STATUS
SYM_JOB_UPDATE_PROGRESS = _lsf.SYM_JOB_UPDATE_PROGRESS

class symJobStatusUpdateReqArray(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, symJobStatusUpdateReqArray, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, symJobStatusUpdateReqArray, name)
    __repr__ = _swig_repr
    __swig_setmethods__["numOfJobReq"] = _lsf.symJobStatusUpdateReqArray_numOfJobReq_set
    __swig_getmethods__["numOfJobReq"] = _lsf.symJobStatusUpdateReqArray_numOfJobReq_get
    if _newclass:numOfJobReq = property(_lsf.symJobStatusUpdateReqArray_numOfJobReq_get, _lsf.symJobStatusUpdateReqArray_numOfJobReq_set)
    __swig_setmethods__["symJobReqs"] = _lsf.symJobStatusUpdateReqArray_symJobReqs_set
    __swig_getmethods__["symJobReqs"] = _lsf.symJobStatusUpdateReqArray_symJobReqs_get
    if _newclass:symJobReqs = property(_lsf.symJobStatusUpdateReqArray_symJobReqs_get, _lsf.symJobStatusUpdateReqArray_symJobReqs_set)
    def __init__(self, *args): 
        this = _lsf.new_symJobStatusUpdateReqArray(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _lsf.delete_symJobStatusUpdateReqArray
    __del__ = lambda self : None;
symJobStatusUpdateReqArray_swigregister = _lsf.symJobStatusUpdateReqArray_swigregister
symJobStatusUpdateReqArray_swigregister(symJobStatusUpdateReqArray)

class symJobUpdateAck(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, symJobUpdateAck, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, symJobUpdateAck, name)
    __repr__ = _swig_repr
    __swig_setmethods__["ackCode"] = _lsf.symJobUpdateAck_ackCode_set
    __swig_getmethods__["ackCode"] = _lsf.symJobUpdateAck_ackCode_get
    if _newclass:ackCode = property(_lsf.symJobUpdateAck_ackCode_get, _lsf.symJobUpdateAck_ackCode_set)
    __swig_setmethods__["desc"] = _lsf.symJobUpdateAck_desc_set
    __swig_getmethods__["desc"] = _lsf.symJobUpdateAck_desc_get
    if _newclass:desc = property(_lsf.symJobUpdateAck_desc_get, _lsf.symJobUpdateAck_desc_set)
    def __init__(self, *args): 
        this = _lsf.new_symJobUpdateAck(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _lsf.delete_symJobUpdateAck
    __del__ = lambda self : None;
symJobUpdateAck_swigregister = _lsf.symJobUpdateAck_swigregister
symJobUpdateAck_swigregister(symJobUpdateAck)
SYM_UPDATE_ACK_OK = _lsf.SYM_UPDATE_ACK_OK
SYM_UPDATE_ACK_ERR = _lsf.SYM_UPDATE_ACK_ERR

class symJobStatusUpdateReply(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, symJobStatusUpdateReply, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, symJobStatusUpdateReply, name)
    __repr__ = _swig_repr
    __swig_setmethods__["jobId"] = _lsf.symJobStatusUpdateReply_jobId_set
    __swig_getmethods__["jobId"] = _lsf.symJobStatusUpdateReply_jobId_get
    if _newclass:jobId = property(_lsf.symJobStatusUpdateReply_jobId_get, _lsf.symJobStatusUpdateReply_jobId_set)
    __swig_setmethods__["acks"] = _lsf.symJobStatusUpdateReply_acks_set
    __swig_getmethods__["acks"] = _lsf.symJobStatusUpdateReply_acks_get
    if _newclass:acks = property(_lsf.symJobStatusUpdateReply_acks_get, _lsf.symJobStatusUpdateReply_acks_set)
    def __init__(self, *args): 
        this = _lsf.new_symJobStatusUpdateReply(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _lsf.delete_symJobStatusUpdateReply
    __del__ = lambda self : None;
symJobStatusUpdateReply_swigregister = _lsf.symJobStatusUpdateReply_swigregister
symJobStatusUpdateReply_swigregister(symJobStatusUpdateReply)
SYM_UPDATE_INFO_IDX = _lsf.SYM_UPDATE_INFO_IDX
SYM_UPDATE_STATUS_IDX = _lsf.SYM_UPDATE_STATUS_IDX
SYM_UPDATE_PROGRESS_IDX = _lsf.SYM_UPDATE_PROGRESS_IDX
NUM_SYM_UPDATE_ACK = _lsf.NUM_SYM_UPDATE_ACK

class symJobStatusUpdateReplyArray(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, symJobStatusUpdateReplyArray, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, symJobStatusUpdateReplyArray, name)
    __repr__ = _swig_repr
    __swig_setmethods__["numOfJobReply"] = _lsf.symJobStatusUpdateReplyArray_numOfJobReply_set
    __swig_getmethods__["numOfJobReply"] = _lsf.symJobStatusUpdateReplyArray_numOfJobReply_get
    if _newclass:numOfJobReply = property(_lsf.symJobStatusUpdateReplyArray_numOfJobReply_get, _lsf.symJobStatusUpdateReplyArray_numOfJobReply_set)
    __swig_setmethods__["symJobReplys"] = _lsf.symJobStatusUpdateReplyArray_symJobReplys_set
    __swig_getmethods__["symJobReplys"] = _lsf.symJobStatusUpdateReplyArray_symJobReplys_get
    if _newclass:symJobReplys = property(_lsf.symJobStatusUpdateReplyArray_symJobReplys_get, _lsf.symJobStatusUpdateReplyArray_symJobReplys_set)
    def __init__(self, *args): 
        this = _lsf.new_symJobStatusUpdateReplyArray(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _lsf.delete_symJobStatusUpdateReplyArray
    __del__ = lambda self : None;
symJobStatusUpdateReplyArray_swigregister = _lsf.symJobStatusUpdateReplyArray_swigregister
symJobStatusUpdateReplyArray_swigregister(symJobStatusUpdateReplyArray)

REQUEUE_DONE = _lsf.REQUEUE_DONE
REQUEUE_EXIT = _lsf.REQUEUE_EXIT
REQUEUE_RUN = _lsf.REQUEUE_RUN
class jobrequeue(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, jobrequeue, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, jobrequeue, name)
    __repr__ = _swig_repr
    __swig_setmethods__["jobId"] = _lsf.jobrequeue_jobId_set
    __swig_getmethods__["jobId"] = _lsf.jobrequeue_jobId_get
    if _newclass:jobId = property(_lsf.jobrequeue_jobId_get, _lsf.jobrequeue_jobId_set)
    __swig_setmethods__["status"] = _lsf.jobrequeue_status_set
    __swig_getmethods__["status"] = _lsf.jobrequeue_status_get
    if _newclass:status = property(_lsf.jobrequeue_status_get, _lsf.jobrequeue_status_set)
    __swig_setmethods__["options"] = _lsf.jobrequeue_options_set
    __swig_getmethods__["options"] = _lsf.jobrequeue_options_get
    if _newclass:options = property(_lsf.jobrequeue_options_get, _lsf.jobrequeue_options_set)
    def __init__(self, *args): 
        this = _lsf.new_jobrequeue(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _lsf.delete_jobrequeue
    __del__ = lambda self : None;
jobrequeue_swigregister = _lsf.jobrequeue_swigregister
jobrequeue_swigregister(jobrequeue)

class requeueEStruct(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, requeueEStruct, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, requeueEStruct, name)
    __repr__ = _swig_repr
    __swig_setmethods__["type"] = _lsf.requeueEStruct_type_set
    __swig_getmethods__["type"] = _lsf.requeueEStruct_type_get
    if _newclass:type = property(_lsf.requeueEStruct_type_get, _lsf.requeueEStruct_type_set)
    __swig_setmethods__["value"] = _lsf.requeueEStruct_value_set
    __swig_getmethods__["value"] = _lsf.requeueEStruct_value_get
    if _newclass:value = property(_lsf.requeueEStruct_value_get, _lsf.requeueEStruct_value_set)
    __swig_setmethods__["interval"] = _lsf.requeueEStruct_interval_set
    __swig_getmethods__["interval"] = _lsf.requeueEStruct_interval_get
    if _newclass:interval = property(_lsf.requeueEStruct_interval_get, _lsf.requeueEStruct_interval_set)
    def __init__(self, *args): 
        this = _lsf.new_requeueEStruct(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _lsf.delete_requeueEStruct
    __del__ = lambda self : None;
requeueEStruct_swigregister = _lsf.requeueEStruct_swigregister
requeueEStruct_swigregister(requeueEStruct)
RQE_NORMAL = _lsf.RQE_NORMAL
RQE_EXCLUDE = _lsf.RQE_EXCLUDE
RQE_END = _lsf.RQE_END

class requeue_t(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, requeue_t, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, requeue_t, name)
    __repr__ = _swig_repr
    __swig_setmethods__["numReqValues"] = _lsf.requeue_t_numReqValues_set
    __swig_getmethods__["numReqValues"] = _lsf.requeue_t_numReqValues_get
    if _newclass:numReqValues = property(_lsf.requeue_t_numReqValues_get, _lsf.requeue_t_numReqValues_set)
    __swig_setmethods__["reqValues"] = _lsf.requeue_t_reqValues_set
    __swig_getmethods__["reqValues"] = _lsf.requeue_t_reqValues_get
    if _newclass:reqValues = property(_lsf.requeue_t_reqValues_get, _lsf.requeue_t_reqValues_set)
    def __init__(self, *args): 
        this = _lsf.new_requeue_t(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _lsf.delete_requeue_t
    __del__ = lambda self : None;
requeue_t_swigregister = _lsf.requeue_t_swigregister
requeue_t_swigregister(requeue_t)

class guarPoolInfo(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, guarPoolInfo, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, guarPoolInfo, name)
    __repr__ = _swig_repr
    __swig_setmethods__["name"] = _lsf.guarPoolInfo_name_set
    __swig_getmethods__["name"] = _lsf.guarPoolInfo_name_get
    if _newclass:name = property(_lsf.guarPoolInfo_name_get, _lsf.guarPoolInfo_name_set)
    __swig_setmethods__["type"] = _lsf.guarPoolInfo_type_set
    __swig_getmethods__["type"] = _lsf.guarPoolInfo_type_get
    if _newclass:type = property(_lsf.guarPoolInfo_type_get, _lsf.guarPoolInfo_type_set)
    __swig_setmethods__["rsrcName"] = _lsf.guarPoolInfo_rsrcName_set
    __swig_getmethods__["rsrcName"] = _lsf.guarPoolInfo_rsrcName_get
    if _newclass:rsrcName = property(_lsf.guarPoolInfo_rsrcName_get, _lsf.guarPoolInfo_rsrcName_set)
    __swig_setmethods__["nGuaranteed"] = _lsf.guarPoolInfo_nGuaranteed_set
    __swig_getmethods__["nGuaranteed"] = _lsf.guarPoolInfo_nGuaranteed_get
    if _newclass:nGuaranteed = property(_lsf.guarPoolInfo_nGuaranteed_get, _lsf.guarPoolInfo_nGuaranteed_set)
    __swig_setmethods__["nUsed"] = _lsf.guarPoolInfo_nUsed_set
    __swig_getmethods__["nUsed"] = _lsf.guarPoolInfo_nUsed_get
    if _newclass:nUsed = property(_lsf.guarPoolInfo_nUsed_get, _lsf.guarPoolInfo_nUsed_set)
    __swig_setmethods__["nGuaranteedUsed"] = _lsf.guarPoolInfo_nGuaranteedUsed_set
    __swig_getmethods__["nGuaranteedUsed"] = _lsf.guarPoolInfo_nGuaranteedUsed_get
    if _newclass:nGuaranteedUsed = property(_lsf.guarPoolInfo_nGuaranteedUsed_get, _lsf.guarPoolInfo_nGuaranteedUsed_set)
    def __init__(self, *args): 
        this = _lsf.new_guarPoolInfo(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _lsf.delete_guarPoolInfo
    __del__ = lambda self : None;
guarPoolInfo_swigregister = _lsf.guarPoolInfo_swigregister
guarPoolInfo_swigregister(guarPoolInfo)

class serviceClass(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, serviceClass, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, serviceClass, name)
    __repr__ = _swig_repr
    __swig_setmethods__["name"] = _lsf.serviceClass_name_set
    __swig_getmethods__["name"] = _lsf.serviceClass_name_get
    if _newclass:name = property(_lsf.serviceClass_name_get, _lsf.serviceClass_name_set)
    __swig_setmethods__["priority"] = _lsf.serviceClass_priority_set
    __swig_getmethods__["priority"] = _lsf.serviceClass_priority_get
    if _newclass:priority = property(_lsf.serviceClass_priority_get, _lsf.serviceClass_priority_set)
    __swig_setmethods__["ngoals"] = _lsf.serviceClass_ngoals_set
    __swig_getmethods__["ngoals"] = _lsf.serviceClass_ngoals_get
    if _newclass:ngoals = property(_lsf.serviceClass_ngoals_get, _lsf.serviceClass_ngoals_set)
    __swig_setmethods__["goals"] = _lsf.serviceClass_goals_set
    __swig_getmethods__["goals"] = _lsf.serviceClass_goals_get
    if _newclass:goals = property(_lsf.serviceClass_goals_get, _lsf.serviceClass_goals_set)
    __swig_setmethods__["userGroups"] = _lsf.serviceClass_userGroups_set
    __swig_getmethods__["userGroups"] = _lsf.serviceClass_userGroups_get
    if _newclass:userGroups = property(_lsf.serviceClass_userGroups_get, _lsf.serviceClass_userGroups_set)
    __swig_setmethods__["description"] = _lsf.serviceClass_description_set
    __swig_getmethods__["description"] = _lsf.serviceClass_description_get
    if _newclass:description = property(_lsf.serviceClass_description_get, _lsf.serviceClass_description_set)
    __swig_setmethods__["controlAction"] = _lsf.serviceClass_controlAction_set
    __swig_getmethods__["controlAction"] = _lsf.serviceClass_controlAction_get
    if _newclass:controlAction = property(_lsf.serviceClass_controlAction_get, _lsf.serviceClass_controlAction_set)
    __swig_setmethods__["throughput"] = _lsf.serviceClass_throughput_set
    __swig_getmethods__["throughput"] = _lsf.serviceClass_throughput_get
    if _newclass:throughput = property(_lsf.serviceClass_throughput_get, _lsf.serviceClass_throughput_set)
    __swig_setmethods__["counters"] = _lsf.serviceClass_counters_set
    __swig_getmethods__["counters"] = _lsf.serviceClass_counters_get
    if _newclass:counters = property(_lsf.serviceClass_counters_get, _lsf.serviceClass_counters_set)
    __swig_setmethods__["consumer"] = _lsf.serviceClass_consumer_set
    __swig_getmethods__["consumer"] = _lsf.serviceClass_consumer_get
    if _newclass:consumer = property(_lsf.serviceClass_consumer_get, _lsf.serviceClass_consumer_set)
    __swig_setmethods__["ctrl"] = _lsf.serviceClass_ctrl_set
    __swig_getmethods__["ctrl"] = _lsf.serviceClass_ctrl_get
    if _newclass:ctrl = property(_lsf.serviceClass_ctrl_get, _lsf.serviceClass_ctrl_set)
    __swig_setmethods__["ctrlExt"] = _lsf.serviceClass_ctrlExt_set
    __swig_getmethods__["ctrlExt"] = _lsf.serviceClass_ctrlExt_get
    if _newclass:ctrlExt = property(_lsf.serviceClass_ctrlExt_get, _lsf.serviceClass_ctrlExt_set)
    __swig_setmethods__["accessControl"] = _lsf.serviceClass_accessControl_set
    __swig_getmethods__["accessControl"] = _lsf.serviceClass_accessControl_get
    if _newclass:accessControl = property(_lsf.serviceClass_accessControl_get, _lsf.serviceClass_accessControl_set)
    __swig_setmethods__["autoAttach"] = _lsf.serviceClass_autoAttach_set
    __swig_getmethods__["autoAttach"] = _lsf.serviceClass_autoAttach_get
    if _newclass:autoAttach = property(_lsf.serviceClass_autoAttach_get, _lsf.serviceClass_autoAttach_set)
    __swig_setmethods__["nGuarPools"] = _lsf.serviceClass_nGuarPools_set
    __swig_getmethods__["nGuarPools"] = _lsf.serviceClass_nGuarPools_get
    if _newclass:nGuarPools = property(_lsf.serviceClass_nGuarPools_get, _lsf.serviceClass_nGuarPools_set)
    __swig_setmethods__["guarPools"] = _lsf.serviceClass_guarPools_set
    __swig_getmethods__["guarPools"] = _lsf.serviceClass_guarPools_get
    if _newclass:guarPools = property(_lsf.serviceClass_guarPools_get, _lsf.serviceClass_guarPools_set)
    def __init__(self, *args): 
        this = _lsf.new_serviceClass(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _lsf.delete_serviceClass
    __del__ = lambda self : None;
serviceClass_swigregister = _lsf.serviceClass_swigregister
serviceClass_swigregister(serviceClass)

GOAL_WINDOW_OPEN = _lsf.GOAL_WINDOW_OPEN
GOAL_WINDOW_CLOSED = _lsf.GOAL_WINDOW_CLOSED
GOAL_ONTIME = _lsf.GOAL_ONTIME
GOAL_DELAYED = _lsf.GOAL_DELAYED
GOAL_DISABLED = _lsf.GOAL_DISABLED
GOAL_DEADLINE = _lsf.GOAL_DEADLINE
GOAL_VELOCITY = _lsf.GOAL_VELOCITY
GOAL_THROUGHPUT = _lsf.GOAL_THROUGHPUT
GOAL_GUARANTEE = _lsf.GOAL_GUARANTEE
class objective(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, objective, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, objective, name)
    __repr__ = _swig_repr
    __swig_setmethods__["spec"] = _lsf.objective_spec_set
    __swig_getmethods__["spec"] = _lsf.objective_spec_get
    if _newclass:spec = property(_lsf.objective_spec_get, _lsf.objective_spec_set)
    __swig_setmethods__["type"] = _lsf.objective_type_set
    __swig_getmethods__["type"] = _lsf.objective_type_get
    if _newclass:type = property(_lsf.objective_type_get, _lsf.objective_type_set)
    __swig_setmethods__["state"] = _lsf.objective_state_set
    __swig_getmethods__["state"] = _lsf.objective_state_get
    if _newclass:state = property(_lsf.objective_state_get, _lsf.objective_state_set)
    __swig_setmethods__["goal"] = _lsf.objective_goal_set
    __swig_getmethods__["goal"] = _lsf.objective_goal_get
    if _newclass:goal = property(_lsf.objective_goal_get, _lsf.objective_goal_set)
    __swig_setmethods__["actual"] = _lsf.objective_actual_set
    __swig_getmethods__["actual"] = _lsf.objective_actual_get
    if _newclass:actual = property(_lsf.objective_actual_get, _lsf.objective_actual_set)
    __swig_setmethods__["optimum"] = _lsf.objective_optimum_set
    __swig_getmethods__["optimum"] = _lsf.objective_optimum_get
    if _newclass:optimum = property(_lsf.objective_optimum_get, _lsf.objective_optimum_set)
    __swig_setmethods__["minimum"] = _lsf.objective_minimum_set
    __swig_getmethods__["minimum"] = _lsf.objective_minimum_get
    if _newclass:minimum = property(_lsf.objective_minimum_get, _lsf.objective_minimum_set)
    def __init__(self, *args): 
        this = _lsf.new_objective(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _lsf.delete_objective
    __del__ = lambda self : None;
objective_swigregister = _lsf.objective_swigregister
objective_swigregister(objective)

class slaControl(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, slaControl, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, slaControl, name)
    __repr__ = _swig_repr
    __swig_setmethods__["sla"] = _lsf.slaControl_sla_set
    __swig_getmethods__["sla"] = _lsf.slaControl_sla_get
    if _newclass:sla = property(_lsf.slaControl_sla_get, _lsf.slaControl_sla_set)
    __swig_setmethods__["consumer"] = _lsf.slaControl_consumer_set
    __swig_getmethods__["consumer"] = _lsf.slaControl_consumer_get
    if _newclass:consumer = property(_lsf.slaControl_consumer_get, _lsf.slaControl_consumer_set)
    __swig_setmethods__["maxHostIdleTime"] = _lsf.slaControl_maxHostIdleTime_set
    __swig_getmethods__["maxHostIdleTime"] = _lsf.slaControl_maxHostIdleTime_get
    if _newclass:maxHostIdleTime = property(_lsf.slaControl_maxHostIdleTime_get, _lsf.slaControl_maxHostIdleTime_set)
    __swig_setmethods__["recallTimeout"] = _lsf.slaControl_recallTimeout_set
    __swig_getmethods__["recallTimeout"] = _lsf.slaControl_recallTimeout_get
    if _newclass:recallTimeout = property(_lsf.slaControl_recallTimeout_get, _lsf.slaControl_recallTimeout_set)
    __swig_setmethods__["numHostRecalled"] = _lsf.slaControl_numHostRecalled_set
    __swig_getmethods__["numHostRecalled"] = _lsf.slaControl_numHostRecalled_get
    if _newclass:numHostRecalled = property(_lsf.slaControl_numHostRecalled_get, _lsf.slaControl_numHostRecalled_set)
    __swig_setmethods__["egoResReq"] = _lsf.slaControl_egoResReq_set
    __swig_getmethods__["egoResReq"] = _lsf.slaControl_egoResReq_get
    if _newclass:egoResReq = property(_lsf.slaControl_egoResReq_get, _lsf.slaControl_egoResReq_set)
    def __init__(self, *args): 
        this = _lsf.new_slaControl(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _lsf.delete_slaControl
    __del__ = lambda self : None;
slaControl_swigregister = _lsf.slaControl_swigregister
slaControl_swigregister(slaControl)

class slaControlExt(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, slaControlExt, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, slaControlExt, name)
    __repr__ = _swig_repr
    __swig_setmethods__["allocflags"] = _lsf.slaControlExt_allocflags_set
    __swig_getmethods__["allocflags"] = _lsf.slaControlExt_allocflags_get
    if _newclass:allocflags = property(_lsf.slaControlExt_allocflags_get, _lsf.slaControlExt_allocflags_set)
    __swig_setmethods__["tile"] = _lsf.slaControlExt_tile_set
    __swig_getmethods__["tile"] = _lsf.slaControlExt_tile_get
    if _newclass:tile = property(_lsf.slaControlExt_tile_get, _lsf.slaControlExt_tile_set)
    def __init__(self, *args): 
        this = _lsf.new_slaControlExt(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _lsf.delete_slaControlExt
    __del__ = lambda self : None;
slaControlExt_swigregister = _lsf.slaControlExt_swigregister
slaControlExt_swigregister(slaControlExt)

class appInfoEnt(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, appInfoEnt, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, appInfoEnt, name)
    __repr__ = _swig_repr
    __swig_setmethods__["name"] = _lsf.appInfoEnt_name_set
    __swig_getmethods__["name"] = _lsf.appInfoEnt_name_get
    if _newclass:name = property(_lsf.appInfoEnt_name_get, _lsf.appInfoEnt_name_set)
    __swig_setmethods__["description"] = _lsf.appInfoEnt_description_set
    __swig_getmethods__["description"] = _lsf.appInfoEnt_description_get
    if _newclass:description = property(_lsf.appInfoEnt_description_get, _lsf.appInfoEnt_description_set)
    __swig_setmethods__["numJobs"] = _lsf.appInfoEnt_numJobs_set
    __swig_getmethods__["numJobs"] = _lsf.appInfoEnt_numJobs_get
    if _newclass:numJobs = property(_lsf.appInfoEnt_numJobs_get, _lsf.appInfoEnt_numJobs_set)
    __swig_setmethods__["numPEND"] = _lsf.appInfoEnt_numPEND_set
    __swig_getmethods__["numPEND"] = _lsf.appInfoEnt_numPEND_get
    if _newclass:numPEND = property(_lsf.appInfoEnt_numPEND_get, _lsf.appInfoEnt_numPEND_set)
    __swig_setmethods__["numRUN"] = _lsf.appInfoEnt_numRUN_set
    __swig_getmethods__["numRUN"] = _lsf.appInfoEnt_numRUN_get
    if _newclass:numRUN = property(_lsf.appInfoEnt_numRUN_get, _lsf.appInfoEnt_numRUN_set)
    __swig_setmethods__["numSSUSP"] = _lsf.appInfoEnt_numSSUSP_set
    __swig_getmethods__["numSSUSP"] = _lsf.appInfoEnt_numSSUSP_get
    if _newclass:numSSUSP = property(_lsf.appInfoEnt_numSSUSP_get, _lsf.appInfoEnt_numSSUSP_set)
    __swig_setmethods__["numUSUSP"] = _lsf.appInfoEnt_numUSUSP_set
    __swig_getmethods__["numUSUSP"] = _lsf.appInfoEnt_numUSUSP_get
    if _newclass:numUSUSP = property(_lsf.appInfoEnt_numUSUSP_get, _lsf.appInfoEnt_numUSUSP_set)
    __swig_setmethods__["numRESERVE"] = _lsf.appInfoEnt_numRESERVE_set
    __swig_getmethods__["numRESERVE"] = _lsf.appInfoEnt_numRESERVE_get
    if _newclass:numRESERVE = property(_lsf.appInfoEnt_numRESERVE_get, _lsf.appInfoEnt_numRESERVE_set)
    __swig_setmethods__["aAttrib"] = _lsf.appInfoEnt_aAttrib_set
    __swig_getmethods__["aAttrib"] = _lsf.appInfoEnt_aAttrib_get
    if _newclass:aAttrib = property(_lsf.appInfoEnt_aAttrib_get, _lsf.appInfoEnt_aAttrib_set)
    __swig_setmethods__["chunkJobSize"] = _lsf.appInfoEnt_chunkJobSize_set
    __swig_getmethods__["chunkJobSize"] = _lsf.appInfoEnt_chunkJobSize_get
    if _newclass:chunkJobSize = property(_lsf.appInfoEnt_chunkJobSize_get, _lsf.appInfoEnt_chunkJobSize_set)
    __swig_setmethods__["requeueEValues"] = _lsf.appInfoEnt_requeueEValues_set
    __swig_getmethods__["requeueEValues"] = _lsf.appInfoEnt_requeueEValues_get
    if _newclass:requeueEValues = property(_lsf.appInfoEnt_requeueEValues_get, _lsf.appInfoEnt_requeueEValues_set)
    __swig_setmethods__["successEValues"] = _lsf.appInfoEnt_successEValues_set
    __swig_getmethods__["successEValues"] = _lsf.appInfoEnt_successEValues_get
    if _newclass:successEValues = property(_lsf.appInfoEnt_successEValues_get, _lsf.appInfoEnt_successEValues_set)
    __swig_setmethods__["preCmd"] = _lsf.appInfoEnt_preCmd_set
    __swig_getmethods__["preCmd"] = _lsf.appInfoEnt_preCmd_get
    if _newclass:preCmd = property(_lsf.appInfoEnt_preCmd_get, _lsf.appInfoEnt_preCmd_set)
    __swig_setmethods__["postCmd"] = _lsf.appInfoEnt_postCmd_set
    __swig_getmethods__["postCmd"] = _lsf.appInfoEnt_postCmd_get
    if _newclass:postCmd = property(_lsf.appInfoEnt_postCmd_get, _lsf.appInfoEnt_postCmd_set)
    __swig_setmethods__["jobStarter"] = _lsf.appInfoEnt_jobStarter_set
    __swig_getmethods__["jobStarter"] = _lsf.appInfoEnt_jobStarter_get
    if _newclass:jobStarter = property(_lsf.appInfoEnt_jobStarter_get, _lsf.appInfoEnt_jobStarter_set)
    __swig_setmethods__["suspendActCmd"] = _lsf.appInfoEnt_suspendActCmd_set
    __swig_getmethods__["suspendActCmd"] = _lsf.appInfoEnt_suspendActCmd_get
    if _newclass:suspendActCmd = property(_lsf.appInfoEnt_suspendActCmd_get, _lsf.appInfoEnt_suspendActCmd_set)
    __swig_setmethods__["resumeActCmd"] = _lsf.appInfoEnt_resumeActCmd_set
    __swig_getmethods__["resumeActCmd"] = _lsf.appInfoEnt_resumeActCmd_get
    if _newclass:resumeActCmd = property(_lsf.appInfoEnt_resumeActCmd_get, _lsf.appInfoEnt_resumeActCmd_set)
    __swig_setmethods__["terminateActCmd"] = _lsf.appInfoEnt_terminateActCmd_set
    __swig_getmethods__["terminateActCmd"] = _lsf.appInfoEnt_terminateActCmd_get
    if _newclass:terminateActCmd = property(_lsf.appInfoEnt_terminateActCmd_get, _lsf.appInfoEnt_terminateActCmd_set)
    __swig_setmethods__["memLimitType"] = _lsf.appInfoEnt_memLimitType_set
    __swig_getmethods__["memLimitType"] = _lsf.appInfoEnt_memLimitType_get
    if _newclass:memLimitType = property(_lsf.appInfoEnt_memLimitType_get, _lsf.appInfoEnt_memLimitType_set)
    __swig_setmethods__["defLimits"] = _lsf.appInfoEnt_defLimits_set
    __swig_getmethods__["defLimits"] = _lsf.appInfoEnt_defLimits_get
    if _newclass:defLimits = property(_lsf.appInfoEnt_defLimits_get, _lsf.appInfoEnt_defLimits_set)
    __swig_setmethods__["hostSpec"] = _lsf.appInfoEnt_hostSpec_set
    __swig_getmethods__["hostSpec"] = _lsf.appInfoEnt_hostSpec_get
    if _newclass:hostSpec = property(_lsf.appInfoEnt_hostSpec_get, _lsf.appInfoEnt_hostSpec_set)
    __swig_setmethods__["resReq"] = _lsf.appInfoEnt_resReq_set
    __swig_getmethods__["resReq"] = _lsf.appInfoEnt_resReq_get
    if _newclass:resReq = property(_lsf.appInfoEnt_resReq_get, _lsf.appInfoEnt_resReq_set)
    __swig_setmethods__["maxProcLimit"] = _lsf.appInfoEnt_maxProcLimit_set
    __swig_getmethods__["maxProcLimit"] = _lsf.appInfoEnt_maxProcLimit_get
    if _newclass:maxProcLimit = property(_lsf.appInfoEnt_maxProcLimit_get, _lsf.appInfoEnt_maxProcLimit_set)
    __swig_setmethods__["defProcLimit"] = _lsf.appInfoEnt_defProcLimit_set
    __swig_getmethods__["defProcLimit"] = _lsf.appInfoEnt_defProcLimit_get
    if _newclass:defProcLimit = property(_lsf.appInfoEnt_defProcLimit_get, _lsf.appInfoEnt_defProcLimit_set)
    __swig_setmethods__["minProcLimit"] = _lsf.appInfoEnt_minProcLimit_set
    __swig_getmethods__["minProcLimit"] = _lsf.appInfoEnt_minProcLimit_get
    if _newclass:minProcLimit = property(_lsf.appInfoEnt_minProcLimit_get, _lsf.appInfoEnt_minProcLimit_set)
    __swig_setmethods__["runTime"] = _lsf.appInfoEnt_runTime_set
    __swig_getmethods__["runTime"] = _lsf.appInfoEnt_runTime_get
    if _newclass:runTime = property(_lsf.appInfoEnt_runTime_get, _lsf.appInfoEnt_runTime_set)
    __swig_setmethods__["jobIncludePostProc"] = _lsf.appInfoEnt_jobIncludePostProc_set
    __swig_getmethods__["jobIncludePostProc"] = _lsf.appInfoEnt_jobIncludePostProc_get
    if _newclass:jobIncludePostProc = property(_lsf.appInfoEnt_jobIncludePostProc_get, _lsf.appInfoEnt_jobIncludePostProc_set)
    __swig_setmethods__["jobPostProcTimeOut"] = _lsf.appInfoEnt_jobPostProcTimeOut_set
    __swig_getmethods__["jobPostProcTimeOut"] = _lsf.appInfoEnt_jobPostProcTimeOut_get
    if _newclass:jobPostProcTimeOut = property(_lsf.appInfoEnt_jobPostProcTimeOut_get, _lsf.appInfoEnt_jobPostProcTimeOut_set)
    __swig_setmethods__["rTaskGoneAction"] = _lsf.appInfoEnt_rTaskGoneAction_set
    __swig_getmethods__["rTaskGoneAction"] = _lsf.appInfoEnt_rTaskGoneAction_get
    if _newclass:rTaskGoneAction = property(_lsf.appInfoEnt_rTaskGoneAction_get, _lsf.appInfoEnt_rTaskGoneAction_set)
    __swig_setmethods__["djobEnvScript"] = _lsf.appInfoEnt_djobEnvScript_set
    __swig_getmethods__["djobEnvScript"] = _lsf.appInfoEnt_djobEnvScript_get
    if _newclass:djobEnvScript = property(_lsf.appInfoEnt_djobEnvScript_get, _lsf.appInfoEnt_djobEnvScript_set)
    __swig_setmethods__["djobRuInterval"] = _lsf.appInfoEnt_djobRuInterval_set
    __swig_getmethods__["djobRuInterval"] = _lsf.appInfoEnt_djobRuInterval_get
    if _newclass:djobRuInterval = property(_lsf.appInfoEnt_djobRuInterval_get, _lsf.appInfoEnt_djobRuInterval_set)
    __swig_setmethods__["djobHbInterval"] = _lsf.appInfoEnt_djobHbInterval_set
    __swig_getmethods__["djobHbInterval"] = _lsf.appInfoEnt_djobHbInterval_get
    if _newclass:djobHbInterval = property(_lsf.appInfoEnt_djobHbInterval_get, _lsf.appInfoEnt_djobHbInterval_set)
    __swig_setmethods__["djobCommfailAction"] = _lsf.appInfoEnt_djobCommfailAction_set
    __swig_getmethods__["djobCommfailAction"] = _lsf.appInfoEnt_djobCommfailAction_get
    if _newclass:djobCommfailAction = property(_lsf.appInfoEnt_djobCommfailAction_get, _lsf.appInfoEnt_djobCommfailAction_set)
    __swig_setmethods__["djobDisabled"] = _lsf.appInfoEnt_djobDisabled_set
    __swig_getmethods__["djobDisabled"] = _lsf.appInfoEnt_djobDisabled_get
    if _newclass:djobDisabled = property(_lsf.appInfoEnt_djobDisabled_get, _lsf.appInfoEnt_djobDisabled_set)
    __swig_setmethods__["djobResizeGracePeriod"] = _lsf.appInfoEnt_djobResizeGracePeriod_set
    __swig_getmethods__["djobResizeGracePeriod"] = _lsf.appInfoEnt_djobResizeGracePeriod_get
    if _newclass:djobResizeGracePeriod = property(_lsf.appInfoEnt_djobResizeGracePeriod_get, _lsf.appInfoEnt_djobResizeGracePeriod_set)
    __swig_setmethods__["chkpntDir"] = _lsf.appInfoEnt_chkpntDir_set
    __swig_getmethods__["chkpntDir"] = _lsf.appInfoEnt_chkpntDir_get
    if _newclass:chkpntDir = property(_lsf.appInfoEnt_chkpntDir_get, _lsf.appInfoEnt_chkpntDir_set)
    __swig_setmethods__["chkpntMethod"] = _lsf.appInfoEnt_chkpntMethod_set
    __swig_getmethods__["chkpntMethod"] = _lsf.appInfoEnt_chkpntMethod_get
    if _newclass:chkpntMethod = property(_lsf.appInfoEnt_chkpntMethod_get, _lsf.appInfoEnt_chkpntMethod_set)
    __swig_setmethods__["chkpntPeriod"] = _lsf.appInfoEnt_chkpntPeriod_set
    __swig_getmethods__["chkpntPeriod"] = _lsf.appInfoEnt_chkpntPeriod_get
    if _newclass:chkpntPeriod = property(_lsf.appInfoEnt_chkpntPeriod_get, _lsf.appInfoEnt_chkpntPeriod_set)
    __swig_setmethods__["initChkpntPeriod"] = _lsf.appInfoEnt_initChkpntPeriod_set
    __swig_getmethods__["initChkpntPeriod"] = _lsf.appInfoEnt_initChkpntPeriod_get
    if _newclass:initChkpntPeriod = property(_lsf.appInfoEnt_initChkpntPeriod_get, _lsf.appInfoEnt_initChkpntPeriod_set)
    __swig_setmethods__["migThreshold"] = _lsf.appInfoEnt_migThreshold_set
    __swig_getmethods__["migThreshold"] = _lsf.appInfoEnt_migThreshold_get
    if _newclass:migThreshold = property(_lsf.appInfoEnt_migThreshold_get, _lsf.appInfoEnt_migThreshold_set)
    __swig_setmethods__["maxJobPreempt"] = _lsf.appInfoEnt_maxJobPreempt_set
    __swig_getmethods__["maxJobPreempt"] = _lsf.appInfoEnt_maxJobPreempt_get
    if _newclass:maxJobPreempt = property(_lsf.appInfoEnt_maxJobPreempt_get, _lsf.appInfoEnt_maxJobPreempt_set)
    __swig_setmethods__["maxPreExecRetry"] = _lsf.appInfoEnt_maxPreExecRetry_set
    __swig_getmethods__["maxPreExecRetry"] = _lsf.appInfoEnt_maxPreExecRetry_get
    if _newclass:maxPreExecRetry = property(_lsf.appInfoEnt_maxPreExecRetry_get, _lsf.appInfoEnt_maxPreExecRetry_set)
    __swig_setmethods__["localMaxPreExecRetry"] = _lsf.appInfoEnt_localMaxPreExecRetry_set
    __swig_getmethods__["localMaxPreExecRetry"] = _lsf.appInfoEnt_localMaxPreExecRetry_get
    if _newclass:localMaxPreExecRetry = property(_lsf.appInfoEnt_localMaxPreExecRetry_get, _lsf.appInfoEnt_localMaxPreExecRetry_set)
    __swig_setmethods__["maxJobRequeue"] = _lsf.appInfoEnt_maxJobRequeue_set
    __swig_getmethods__["maxJobRequeue"] = _lsf.appInfoEnt_maxJobRequeue_get
    if _newclass:maxJobRequeue = property(_lsf.appInfoEnt_maxJobRequeue_get, _lsf.appInfoEnt_maxJobRequeue_set)
    __swig_setmethods__["noPreemptRunTime"] = _lsf.appInfoEnt_noPreemptRunTime_set
    __swig_getmethods__["noPreemptRunTime"] = _lsf.appInfoEnt_noPreemptRunTime_get
    if _newclass:noPreemptRunTime = property(_lsf.appInfoEnt_noPreemptRunTime_get, _lsf.appInfoEnt_noPreemptRunTime_set)
    __swig_setmethods__["noPreemptFinishTime"] = _lsf.appInfoEnt_noPreemptFinishTime_set
    __swig_getmethods__["noPreemptFinishTime"] = _lsf.appInfoEnt_noPreemptFinishTime_get
    if _newclass:noPreemptFinishTime = property(_lsf.appInfoEnt_noPreemptFinishTime_get, _lsf.appInfoEnt_noPreemptFinishTime_set)
    __swig_setmethods__["noPreemptRunTimePercent"] = _lsf.appInfoEnt_noPreemptRunTimePercent_set
    __swig_getmethods__["noPreemptRunTimePercent"] = _lsf.appInfoEnt_noPreemptRunTimePercent_get
    if _newclass:noPreemptRunTimePercent = property(_lsf.appInfoEnt_noPreemptRunTimePercent_get, _lsf.appInfoEnt_noPreemptRunTimePercent_set)
    __swig_setmethods__["noPreemptFinishTimePercent"] = _lsf.appInfoEnt_noPreemptFinishTimePercent_set
    __swig_getmethods__["noPreemptFinishTimePercent"] = _lsf.appInfoEnt_noPreemptFinishTimePercent_get
    if _newclass:noPreemptFinishTimePercent = property(_lsf.appInfoEnt_noPreemptFinishTimePercent_get, _lsf.appInfoEnt_noPreemptFinishTimePercent_set)
    __swig_setmethods__["usePam"] = _lsf.appInfoEnt_usePam_set
    __swig_getmethods__["usePam"] = _lsf.appInfoEnt_usePam_get
    if _newclass:usePam = property(_lsf.appInfoEnt_usePam_get, _lsf.appInfoEnt_usePam_set)
    __swig_setmethods__["bindingOption"] = _lsf.appInfoEnt_bindingOption_set
    __swig_getmethods__["bindingOption"] = _lsf.appInfoEnt_bindingOption_get
    if _newclass:bindingOption = property(_lsf.appInfoEnt_bindingOption_get, _lsf.appInfoEnt_bindingOption_set)
    __swig_setmethods__["persistHostOrder"] = _lsf.appInfoEnt_persistHostOrder_set
    __swig_getmethods__["persistHostOrder"] = _lsf.appInfoEnt_persistHostOrder_get
    if _newclass:persistHostOrder = property(_lsf.appInfoEnt_persistHostOrder_get, _lsf.appInfoEnt_persistHostOrder_set)
    __swig_setmethods__["resizeNotifyCmd"] = _lsf.appInfoEnt_resizeNotifyCmd_set
    __swig_getmethods__["resizeNotifyCmd"] = _lsf.appInfoEnt_resizeNotifyCmd_get
    if _newclass:resizeNotifyCmd = property(_lsf.appInfoEnt_resizeNotifyCmd_get, _lsf.appInfoEnt_resizeNotifyCmd_set)
    __swig_setmethods__["noPreemptInterval"] = _lsf.appInfoEnt_noPreemptInterval_set
    __swig_getmethods__["noPreemptInterval"] = _lsf.appInfoEnt_noPreemptInterval_get
    if _newclass:noPreemptInterval = property(_lsf.appInfoEnt_noPreemptInterval_get, _lsf.appInfoEnt_noPreemptInterval_set)
    __swig_setmethods__["maxTotalTimePreempt"] = _lsf.appInfoEnt_maxTotalTimePreempt_set
    __swig_getmethods__["maxTotalTimePreempt"] = _lsf.appInfoEnt_maxTotalTimePreempt_get
    if _newclass:maxTotalTimePreempt = property(_lsf.appInfoEnt_maxTotalTimePreempt_get, _lsf.appInfoEnt_maxTotalTimePreempt_set)
    __swig_setmethods__["nice"] = _lsf.appInfoEnt_nice_set
    __swig_getmethods__["nice"] = _lsf.appInfoEnt_nice_get
    if _newclass:nice = property(_lsf.appInfoEnt_nice_get, _lsf.appInfoEnt_nice_set)
    __swig_setmethods__["preemptDelayTime"] = _lsf.appInfoEnt_preemptDelayTime_set
    __swig_getmethods__["preemptDelayTime"] = _lsf.appInfoEnt_preemptDelayTime_get
    if _newclass:preemptDelayTime = property(_lsf.appInfoEnt_preemptDelayTime_get, _lsf.appInfoEnt_preemptDelayTime_set)
    __swig_setmethods__["jobPreProcTimeOut"] = _lsf.appInfoEnt_jobPreProcTimeOut_set
    __swig_getmethods__["jobPreProcTimeOut"] = _lsf.appInfoEnt_jobPreProcTimeOut_get
    if _newclass:jobPreProcTimeOut = property(_lsf.appInfoEnt_jobPreProcTimeOut_get, _lsf.appInfoEnt_jobPreProcTimeOut_set)
    def __init__(self, *args): 
        this = _lsf.new_appInfoEnt(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _lsf.delete_appInfoEnt
    __del__ = lambda self : None;
appInfoEnt_swigregister = _lsf.appInfoEnt_swigregister
appInfoEnt_swigregister(appInfoEnt)

A_ATTRIB_RERUNNABLE = _lsf.A_ATTRIB_RERUNNABLE
A_ATTRIB_NONRERUNNABLE = _lsf.A_ATTRIB_NONRERUNNABLE
A_ATTRIB_DEFAULT = _lsf.A_ATTRIB_DEFAULT
A_ATTRIB_ABS_RUNLIMIT = _lsf.A_ATTRIB_ABS_RUNLIMIT
A_ATTRIB_JOBBINDING = _lsf.A_ATTRIB_JOBBINDING
A_ATTRIB_NONJOBBINDING = _lsf.A_ATTRIB_NONJOBBINDING
A_ATTRIB_CHKPNT = _lsf.A_ATTRIB_CHKPNT
A_ATTRIB_RESIZABLE = _lsf.A_ATTRIB_RESIZABLE
A_ATTRIB_AUTO_RESIZABLE = _lsf.A_ATTRIB_AUTO_RESIZABLE
BINDING_OPTION_BALANCE = _lsf.BINDING_OPTION_BALANCE
BINDING_OPTION_PACK = _lsf.BINDING_OPTION_PACK
BINDING_OPTION_ANY = _lsf.BINDING_OPTION_ANY
BINDING_OPTION_USER = _lsf.BINDING_OPTION_USER
BINDING_OPTION_USER_CPU_LIST = _lsf.BINDING_OPTION_USER_CPU_LIST
BINDING_OPTION_NONE = _lsf.BINDING_OPTION_NONE
TO_TOP = _lsf.TO_TOP
TO_BOTTOM = _lsf.TO_BOTTOM
QUEUE_OPEN = _lsf.QUEUE_OPEN
QUEUE_CLOSED = _lsf.QUEUE_CLOSED
QUEUE_ACTIVATE = _lsf.QUEUE_ACTIVATE
QUEUE_INACTIVATE = _lsf.QUEUE_INACTIVATE
QUEUE_CLEAN = _lsf.QUEUE_CLEAN
class queueCtrlReq(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, queueCtrlReq, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, queueCtrlReq, name)
    __repr__ = _swig_repr
    __swig_setmethods__["queue"] = _lsf.queueCtrlReq_queue_set
    __swig_getmethods__["queue"] = _lsf.queueCtrlReq_queue_get
    if _newclass:queue = property(_lsf.queueCtrlReq_queue_get, _lsf.queueCtrlReq_queue_set)
    __swig_setmethods__["opCode"] = _lsf.queueCtrlReq_opCode_set
    __swig_getmethods__["opCode"] = _lsf.queueCtrlReq_opCode_get
    if _newclass:opCode = property(_lsf.queueCtrlReq_opCode_get, _lsf.queueCtrlReq_opCode_set)
    __swig_setmethods__["message"] = _lsf.queueCtrlReq_message_set
    __swig_getmethods__["message"] = _lsf.queueCtrlReq_message_get
    if _newclass:message = property(_lsf.queueCtrlReq_message_get, _lsf.queueCtrlReq_message_set)
    def __init__(self, *args): 
        this = _lsf.new_queueCtrlReq(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _lsf.delete_queueCtrlReq
    __del__ = lambda self : None;
queueCtrlReq_swigregister = _lsf.queueCtrlReq_swigregister
queueCtrlReq_swigregister(queueCtrlReq)

HOST_OPEN = _lsf.HOST_OPEN
HOST_CLOSE = _lsf.HOST_CLOSE
HOST_REBOOT = _lsf.HOST_REBOOT
HOST_SHUTDOWN = _lsf.HOST_SHUTDOWN
HOST_CLOSE_REMOTE = _lsf.HOST_CLOSE_REMOTE
class hostCtrlReq(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, hostCtrlReq, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, hostCtrlReq, name)
    __repr__ = _swig_repr
    __swig_setmethods__["host"] = _lsf.hostCtrlReq_host_set
    __swig_getmethods__["host"] = _lsf.hostCtrlReq_host_get
    if _newclass:host = property(_lsf.hostCtrlReq_host_get, _lsf.hostCtrlReq_host_set)
    __swig_setmethods__["opCode"] = _lsf.hostCtrlReq_opCode_set
    __swig_getmethods__["opCode"] = _lsf.hostCtrlReq_opCode_get
    if _newclass:opCode = property(_lsf.hostCtrlReq_opCode_get, _lsf.hostCtrlReq_opCode_set)
    __swig_setmethods__["message"] = _lsf.hostCtrlReq_message_set
    __swig_getmethods__["message"] = _lsf.hostCtrlReq_message_get
    if _newclass:message = property(_lsf.hostCtrlReq_message_get, _lsf.hostCtrlReq_message_set)
    def __init__(self, *args): 
        this = _lsf.new_hostCtrlReq(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _lsf.delete_hostCtrlReq
    __del__ = lambda self : None;
hostCtrlReq_swigregister = _lsf.hostCtrlReq_swigregister
hostCtrlReq_swigregister(hostCtrlReq)

HGHOST_ADD = _lsf.HGHOST_ADD
HGHOST_DEL = _lsf.HGHOST_DEL
class hgCtrlReq(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, hgCtrlReq, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, hgCtrlReq, name)
    __repr__ = _swig_repr
    __swig_setmethods__["opCode"] = _lsf.hgCtrlReq_opCode_set
    __swig_getmethods__["opCode"] = _lsf.hgCtrlReq_opCode_get
    if _newclass:opCode = property(_lsf.hgCtrlReq_opCode_get, _lsf.hgCtrlReq_opCode_set)
    __swig_setmethods__["grpname"] = _lsf.hgCtrlReq_grpname_set
    __swig_getmethods__["grpname"] = _lsf.hgCtrlReq_grpname_get
    if _newclass:grpname = property(_lsf.hgCtrlReq_grpname_get, _lsf.hgCtrlReq_grpname_set)
    __swig_setmethods__["numhosts"] = _lsf.hgCtrlReq_numhosts_set
    __swig_getmethods__["numhosts"] = _lsf.hgCtrlReq_numhosts_get
    if _newclass:numhosts = property(_lsf.hgCtrlReq_numhosts_get, _lsf.hgCtrlReq_numhosts_set)
    __swig_setmethods__["hosts"] = _lsf.hgCtrlReq_hosts_set
    __swig_getmethods__["hosts"] = _lsf.hgCtrlReq_hosts_get
    if _newclass:hosts = property(_lsf.hgCtrlReq_hosts_get, _lsf.hgCtrlReq_hosts_set)
    __swig_setmethods__["message"] = _lsf.hgCtrlReq_message_set
    __swig_getmethods__["message"] = _lsf.hgCtrlReq_message_get
    if _newclass:message = property(_lsf.hgCtrlReq_message_get, _lsf.hgCtrlReq_message_set)
    def __init__(self, *args): 
        this = _lsf.new_hgCtrlReq(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _lsf.delete_hgCtrlReq
    __del__ = lambda self : None;
hgCtrlReq_swigregister = _lsf.hgCtrlReq_swigregister
hgCtrlReq_swigregister(hgCtrlReq)

class hgCtrlReply(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, hgCtrlReply, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, hgCtrlReply, name)
    __repr__ = _swig_repr
    __swig_setmethods__["numsucc"] = _lsf.hgCtrlReply_numsucc_set
    __swig_getmethods__["numsucc"] = _lsf.hgCtrlReply_numsucc_get
    if _newclass:numsucc = property(_lsf.hgCtrlReply_numsucc_get, _lsf.hgCtrlReply_numsucc_set)
    __swig_setmethods__["numfail"] = _lsf.hgCtrlReply_numfail_set
    __swig_getmethods__["numfail"] = _lsf.hgCtrlReply_numfail_get
    if _newclass:numfail = property(_lsf.hgCtrlReply_numfail_get, _lsf.hgCtrlReply_numfail_set)
    __swig_setmethods__["succHosts"] = _lsf.hgCtrlReply_succHosts_set
    __swig_getmethods__["succHosts"] = _lsf.hgCtrlReply_succHosts_get
    if _newclass:succHosts = property(_lsf.hgCtrlReply_succHosts_get, _lsf.hgCtrlReply_succHosts_set)
    __swig_setmethods__["failHosts"] = _lsf.hgCtrlReply_failHosts_set
    __swig_getmethods__["failHosts"] = _lsf.hgCtrlReply_failHosts_get
    if _newclass:failHosts = property(_lsf.hgCtrlReply_failHosts_get, _lsf.hgCtrlReply_failHosts_set)
    __swig_setmethods__["failReasons"] = _lsf.hgCtrlReply_failReasons_set
    __swig_getmethods__["failReasons"] = _lsf.hgCtrlReply_failReasons_get
    if _newclass:failReasons = property(_lsf.hgCtrlReply_failReasons_get, _lsf.hgCtrlReply_failReasons_set)
    def __init__(self, *args): 
        this = _lsf.new_hgCtrlReply(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _lsf.delete_hgCtrlReply
    __del__ = lambda self : None;
hgCtrlReply_swigregister = _lsf.hgCtrlReply_swigregister
hgCtrlReply_swigregister(hgCtrlReply)

MBD_RESTART = _lsf.MBD_RESTART
MBD_RECONFIG = _lsf.MBD_RECONFIG
MBD_CKCONFIG = _lsf.MBD_CKCONFIG
class mbdCtrlReq(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, mbdCtrlReq, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, mbdCtrlReq, name)
    __repr__ = _swig_repr
    __swig_setmethods__["opCode"] = _lsf.mbdCtrlReq_opCode_set
    __swig_getmethods__["opCode"] = _lsf.mbdCtrlReq_opCode_get
    if _newclass:opCode = property(_lsf.mbdCtrlReq_opCode_get, _lsf.mbdCtrlReq_opCode_set)
    __swig_setmethods__["name"] = _lsf.mbdCtrlReq_name_set
    __swig_getmethods__["name"] = _lsf.mbdCtrlReq_name_get
    if _newclass:name = property(_lsf.mbdCtrlReq_name_get, _lsf.mbdCtrlReq_name_set)
    __swig_setmethods__["message"] = _lsf.mbdCtrlReq_message_set
    __swig_getmethods__["message"] = _lsf.mbdCtrlReq_message_get
    if _newclass:message = property(_lsf.mbdCtrlReq_message_get, _lsf.mbdCtrlReq_message_set)
    def __init__(self, *args): 
        this = _lsf.new_mbdCtrlReq(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _lsf.delete_mbdCtrlReq
    __del__ = lambda self : None;
mbdCtrlReq_swigregister = _lsf.mbdCtrlReq_swigregister
mbdCtrlReq_swigregister(mbdCtrlReq)

PERFMON_START = _lsf.PERFMON_START
PERFMON_STOP = _lsf.PERFMON_STOP
PERFMON_SET_PERIOD = _lsf.PERFMON_SET_PERIOD
DEF_PERFMON_PERIOD = _lsf.DEF_PERFMON_PERIOD
class perfmonMetricsEnt(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, perfmonMetricsEnt, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, perfmonMetricsEnt, name)
    __repr__ = _swig_repr
    __swig_setmethods__["name"] = _lsf.perfmonMetricsEnt_name_set
    __swig_getmethods__["name"] = _lsf.perfmonMetricsEnt_name_get
    if _newclass:name = property(_lsf.perfmonMetricsEnt_name_get, _lsf.perfmonMetricsEnt_name_set)
    __swig_setmethods__["current"] = _lsf.perfmonMetricsEnt_current_set
    __swig_getmethods__["current"] = _lsf.perfmonMetricsEnt_current_get
    if _newclass:current = property(_lsf.perfmonMetricsEnt_current_get, _lsf.perfmonMetricsEnt_current_set)
    __swig_setmethods__["max"] = _lsf.perfmonMetricsEnt_max_set
    __swig_getmethods__["max"] = _lsf.perfmonMetricsEnt_max_get
    if _newclass:max = property(_lsf.perfmonMetricsEnt_max_get, _lsf.perfmonMetricsEnt_max_set)
    __swig_setmethods__["min"] = _lsf.perfmonMetricsEnt_min_set
    __swig_getmethods__["min"] = _lsf.perfmonMetricsEnt_min_get
    if _newclass:min = property(_lsf.perfmonMetricsEnt_min_get, _lsf.perfmonMetricsEnt_min_set)
    __swig_setmethods__["avg"] = _lsf.perfmonMetricsEnt_avg_set
    __swig_getmethods__["avg"] = _lsf.perfmonMetricsEnt_avg_get
    if _newclass:avg = property(_lsf.perfmonMetricsEnt_avg_get, _lsf.perfmonMetricsEnt_avg_set)
    __swig_setmethods__["total"] = _lsf.perfmonMetricsEnt_total_set
    __swig_getmethods__["total"] = _lsf.perfmonMetricsEnt_total_get
    if _newclass:total = property(_lsf.perfmonMetricsEnt_total_get, _lsf.perfmonMetricsEnt_total_set)
    def __init__(self, *args): 
        this = _lsf.new_perfmonMetricsEnt(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _lsf.delete_perfmonMetricsEnt
    __del__ = lambda self : None;
perfmonMetricsEnt_swigregister = _lsf.perfmonMetricsEnt_swigregister
perfmonMetricsEnt_swigregister(perfmonMetricsEnt)

class perfmonInfo(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, perfmonInfo, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, perfmonInfo, name)
    __repr__ = _swig_repr
    __swig_setmethods__["num"] = _lsf.perfmonInfo_num_set
    __swig_getmethods__["num"] = _lsf.perfmonInfo_num_get
    if _newclass:num = property(_lsf.perfmonInfo_num_get, _lsf.perfmonInfo_num_set)
    __swig_setmethods__["record"] = _lsf.perfmonInfo_record_set
    __swig_getmethods__["record"] = _lsf.perfmonInfo_record_get
    if _newclass:record = property(_lsf.perfmonInfo_record_get, _lsf.perfmonInfo_record_set)
    __swig_setmethods__["period"] = _lsf.perfmonInfo_period_set
    __swig_getmethods__["period"] = _lsf.perfmonInfo_period_get
    if _newclass:period = property(_lsf.perfmonInfo_period_get, _lsf.perfmonInfo_period_set)
    __swig_setmethods__["start"] = _lsf.perfmonInfo_start_set
    __swig_getmethods__["start"] = _lsf.perfmonInfo_start_get
    if _newclass:start = property(_lsf.perfmonInfo_start_get, _lsf.perfmonInfo_start_set)
    __swig_setmethods__["end"] = _lsf.perfmonInfo_end_set
    __swig_getmethods__["end"] = _lsf.perfmonInfo_end_get
    if _newclass:end = property(_lsf.perfmonInfo_end_get, _lsf.perfmonInfo_end_set)
    def __init__(self, *args): 
        this = _lsf.new_perfmonInfo(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _lsf.delete_perfmonInfo
    __del__ = lambda self : None;
perfmonInfo_swigregister = _lsf.perfmonInfo_swigregister
perfmonInfo_swigregister(perfmonInfo)

JGRP_RELEASE_PARENTONLY = _lsf.JGRP_RELEASE_PARENTONLY
class logSwitchLog(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, logSwitchLog, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, logSwitchLog, name)
    __repr__ = _swig_repr
    __swig_setmethods__["lastJobId"] = _lsf.logSwitchLog_lastJobId_set
    __swig_getmethods__["lastJobId"] = _lsf.logSwitchLog_lastJobId_get
    if _newclass:lastJobId = property(_lsf.logSwitchLog_lastJobId_get, _lsf.logSwitchLog_lastJobId_set)
    def __init__(self, *args): 
        this = _lsf.new_logSwitchLog(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _lsf.delete_logSwitchLog
    __del__ = lambda self : None;
logSwitchLog_swigregister = _lsf.logSwitchLog_swigregister
logSwitchLog_swigregister(logSwitchLog)

class dataLoggingLog(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, dataLoggingLog, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, dataLoggingLog, name)
    __repr__ = _swig_repr
    __swig_setmethods__["loggingTime"] = _lsf.dataLoggingLog_loggingTime_set
    __swig_getmethods__["loggingTime"] = _lsf.dataLoggingLog_loggingTime_get
    if _newclass:loggingTime = property(_lsf.dataLoggingLog_loggingTime_get, _lsf.dataLoggingLog_loggingTime_set)
    def __init__(self, *args): 
        this = _lsf.new_dataLoggingLog(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _lsf.delete_dataLoggingLog
    __del__ = lambda self : None;
dataLoggingLog_swigregister = _lsf.dataLoggingLog_swigregister
dataLoggingLog_swigregister(dataLoggingLog)

class jgrpNewLog(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, jgrpNewLog, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, jgrpNewLog, name)
    __repr__ = _swig_repr
    __swig_setmethods__["userId"] = _lsf.jgrpNewLog_userId_set
    __swig_getmethods__["userId"] = _lsf.jgrpNewLog_userId_get
    if _newclass:userId = property(_lsf.jgrpNewLog_userId_get, _lsf.jgrpNewLog_userId_set)
    __swig_setmethods__["submitTime"] = _lsf.jgrpNewLog_submitTime_set
    __swig_getmethods__["submitTime"] = _lsf.jgrpNewLog_submitTime_get
    if _newclass:submitTime = property(_lsf.jgrpNewLog_submitTime_get, _lsf.jgrpNewLog_submitTime_set)
    __swig_setmethods__["userName"] = _lsf.jgrpNewLog_userName_set
    __swig_getmethods__["userName"] = _lsf.jgrpNewLog_userName_get
    if _newclass:userName = property(_lsf.jgrpNewLog_userName_get, _lsf.jgrpNewLog_userName_set)
    __swig_setmethods__["depCond"] = _lsf.jgrpNewLog_depCond_set
    __swig_getmethods__["depCond"] = _lsf.jgrpNewLog_depCond_get
    if _newclass:depCond = property(_lsf.jgrpNewLog_depCond_get, _lsf.jgrpNewLog_depCond_set)
    __swig_setmethods__["timeEvent"] = _lsf.jgrpNewLog_timeEvent_set
    __swig_getmethods__["timeEvent"] = _lsf.jgrpNewLog_timeEvent_get
    if _newclass:timeEvent = property(_lsf.jgrpNewLog_timeEvent_get, _lsf.jgrpNewLog_timeEvent_set)
    __swig_setmethods__["groupSpec"] = _lsf.jgrpNewLog_groupSpec_set
    __swig_getmethods__["groupSpec"] = _lsf.jgrpNewLog_groupSpec_get
    if _newclass:groupSpec = property(_lsf.jgrpNewLog_groupSpec_get, _lsf.jgrpNewLog_groupSpec_set)
    __swig_setmethods__["destSpec"] = _lsf.jgrpNewLog_destSpec_set
    __swig_getmethods__["destSpec"] = _lsf.jgrpNewLog_destSpec_get
    if _newclass:destSpec = property(_lsf.jgrpNewLog_destSpec_get, _lsf.jgrpNewLog_destSpec_set)
    __swig_setmethods__["delOptions"] = _lsf.jgrpNewLog_delOptions_set
    __swig_getmethods__["delOptions"] = _lsf.jgrpNewLog_delOptions_get
    if _newclass:delOptions = property(_lsf.jgrpNewLog_delOptions_get, _lsf.jgrpNewLog_delOptions_set)
    __swig_setmethods__["delOptions2"] = _lsf.jgrpNewLog_delOptions2_set
    __swig_getmethods__["delOptions2"] = _lsf.jgrpNewLog_delOptions2_get
    if _newclass:delOptions2 = property(_lsf.jgrpNewLog_delOptions2_get, _lsf.jgrpNewLog_delOptions2_set)
    __swig_setmethods__["fromPlatform"] = _lsf.jgrpNewLog_fromPlatform_set
    __swig_getmethods__["fromPlatform"] = _lsf.jgrpNewLog_fromPlatform_get
    if _newclass:fromPlatform = property(_lsf.jgrpNewLog_fromPlatform_get, _lsf.jgrpNewLog_fromPlatform_set)
    __swig_setmethods__["sla"] = _lsf.jgrpNewLog_sla_set
    __swig_getmethods__["sla"] = _lsf.jgrpNewLog_sla_get
    if _newclass:sla = property(_lsf.jgrpNewLog_sla_get, _lsf.jgrpNewLog_sla_set)
    __swig_setmethods__["maxJLimit"] = _lsf.jgrpNewLog_maxJLimit_set
    __swig_getmethods__["maxJLimit"] = _lsf.jgrpNewLog_maxJLimit_get
    if _newclass:maxJLimit = property(_lsf.jgrpNewLog_maxJLimit_get, _lsf.jgrpNewLog_maxJLimit_set)
    __swig_setmethods__["options"] = _lsf.jgrpNewLog_options_set
    __swig_getmethods__["options"] = _lsf.jgrpNewLog_options_get
    if _newclass:options = property(_lsf.jgrpNewLog_options_get, _lsf.jgrpNewLog_options_set)
    def __init__(self, *args): 
        this = _lsf.new_jgrpNewLog(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _lsf.delete_jgrpNewLog
    __del__ = lambda self : None;
jgrpNewLog_swigregister = _lsf.jgrpNewLog_swigregister
jgrpNewLog_swigregister(jgrpNewLog)

class jgrpCtrlLog(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, jgrpCtrlLog, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, jgrpCtrlLog, name)
    __repr__ = _swig_repr
    __swig_setmethods__["userId"] = _lsf.jgrpCtrlLog_userId_set
    __swig_getmethods__["userId"] = _lsf.jgrpCtrlLog_userId_get
    if _newclass:userId = property(_lsf.jgrpCtrlLog_userId_get, _lsf.jgrpCtrlLog_userId_set)
    __swig_setmethods__["userName"] = _lsf.jgrpCtrlLog_userName_set
    __swig_getmethods__["userName"] = _lsf.jgrpCtrlLog_userName_get
    if _newclass:userName = property(_lsf.jgrpCtrlLog_userName_get, _lsf.jgrpCtrlLog_userName_set)
    __swig_setmethods__["groupSpec"] = _lsf.jgrpCtrlLog_groupSpec_set
    __swig_getmethods__["groupSpec"] = _lsf.jgrpCtrlLog_groupSpec_get
    if _newclass:groupSpec = property(_lsf.jgrpCtrlLog_groupSpec_get, _lsf.jgrpCtrlLog_groupSpec_set)
    __swig_setmethods__["options"] = _lsf.jgrpCtrlLog_options_set
    __swig_getmethods__["options"] = _lsf.jgrpCtrlLog_options_get
    if _newclass:options = property(_lsf.jgrpCtrlLog_options_get, _lsf.jgrpCtrlLog_options_set)
    __swig_setmethods__["ctrlOp"] = _lsf.jgrpCtrlLog_ctrlOp_set
    __swig_getmethods__["ctrlOp"] = _lsf.jgrpCtrlLog_ctrlOp_get
    if _newclass:ctrlOp = property(_lsf.jgrpCtrlLog_ctrlOp_get, _lsf.jgrpCtrlLog_ctrlOp_set)
    def __init__(self, *args): 
        this = _lsf.new_jgrpCtrlLog(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _lsf.delete_jgrpCtrlLog
    __del__ = lambda self : None;
jgrpCtrlLog_swigregister = _lsf.jgrpCtrlLog_swigregister
jgrpCtrlLog_swigregister(jgrpCtrlLog)

class jgrpStatusLog(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, jgrpStatusLog, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, jgrpStatusLog, name)
    __repr__ = _swig_repr
    __swig_setmethods__["groupSpec"] = _lsf.jgrpStatusLog_groupSpec_set
    __swig_getmethods__["groupSpec"] = _lsf.jgrpStatusLog_groupSpec_get
    if _newclass:groupSpec = property(_lsf.jgrpStatusLog_groupSpec_get, _lsf.jgrpStatusLog_groupSpec_set)
    __swig_setmethods__["status"] = _lsf.jgrpStatusLog_status_set
    __swig_getmethods__["status"] = _lsf.jgrpStatusLog_status_get
    if _newclass:status = property(_lsf.jgrpStatusLog_status_get, _lsf.jgrpStatusLog_status_set)
    __swig_setmethods__["oldStatus"] = _lsf.jgrpStatusLog_oldStatus_set
    __swig_getmethods__["oldStatus"] = _lsf.jgrpStatusLog_oldStatus_get
    if _newclass:oldStatus = property(_lsf.jgrpStatusLog_oldStatus_get, _lsf.jgrpStatusLog_oldStatus_set)
    def __init__(self, *args): 
        this = _lsf.new_jgrpStatusLog(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _lsf.delete_jgrpStatusLog
    __del__ = lambda self : None;
jgrpStatusLog_swigregister = _lsf.jgrpStatusLog_swigregister
jgrpStatusLog_swigregister(jgrpStatusLog)

class jobNewLog(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, jobNewLog, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, jobNewLog, name)
    __repr__ = _swig_repr
    __swig_setmethods__["jobId"] = _lsf.jobNewLog_jobId_set
    __swig_getmethods__["jobId"] = _lsf.jobNewLog_jobId_get
    if _newclass:jobId = property(_lsf.jobNewLog_jobId_get, _lsf.jobNewLog_jobId_set)
    __swig_setmethods__["userId"] = _lsf.jobNewLog_userId_set
    __swig_getmethods__["userId"] = _lsf.jobNewLog_userId_get
    if _newclass:userId = property(_lsf.jobNewLog_userId_get, _lsf.jobNewLog_userId_set)
    __swig_setmethods__["userName"] = _lsf.jobNewLog_userName_set
    __swig_getmethods__["userName"] = _lsf.jobNewLog_userName_get
    if _newclass:userName = property(_lsf.jobNewLog_userName_get, _lsf.jobNewLog_userName_set)
    __swig_setmethods__["options"] = _lsf.jobNewLog_options_set
    __swig_getmethods__["options"] = _lsf.jobNewLog_options_get
    if _newclass:options = property(_lsf.jobNewLog_options_get, _lsf.jobNewLog_options_set)
    __swig_setmethods__["options2"] = _lsf.jobNewLog_options2_set
    __swig_getmethods__["options2"] = _lsf.jobNewLog_options2_get
    if _newclass:options2 = property(_lsf.jobNewLog_options2_get, _lsf.jobNewLog_options2_set)
    __swig_setmethods__["numProcessors"] = _lsf.jobNewLog_numProcessors_set
    __swig_getmethods__["numProcessors"] = _lsf.jobNewLog_numProcessors_get
    if _newclass:numProcessors = property(_lsf.jobNewLog_numProcessors_get, _lsf.jobNewLog_numProcessors_set)
    __swig_setmethods__["submitTime"] = _lsf.jobNewLog_submitTime_set
    __swig_getmethods__["submitTime"] = _lsf.jobNewLog_submitTime_get
    if _newclass:submitTime = property(_lsf.jobNewLog_submitTime_get, _lsf.jobNewLog_submitTime_set)
    __swig_setmethods__["beginTime"] = _lsf.jobNewLog_beginTime_set
    __swig_getmethods__["beginTime"] = _lsf.jobNewLog_beginTime_get
    if _newclass:beginTime = property(_lsf.jobNewLog_beginTime_get, _lsf.jobNewLog_beginTime_set)
    __swig_setmethods__["termTime"] = _lsf.jobNewLog_termTime_set
    __swig_getmethods__["termTime"] = _lsf.jobNewLog_termTime_get
    if _newclass:termTime = property(_lsf.jobNewLog_termTime_get, _lsf.jobNewLog_termTime_set)
    __swig_setmethods__["sigValue"] = _lsf.jobNewLog_sigValue_set
    __swig_getmethods__["sigValue"] = _lsf.jobNewLog_sigValue_get
    if _newclass:sigValue = property(_lsf.jobNewLog_sigValue_get, _lsf.jobNewLog_sigValue_set)
    __swig_setmethods__["chkpntPeriod"] = _lsf.jobNewLog_chkpntPeriod_set
    __swig_getmethods__["chkpntPeriod"] = _lsf.jobNewLog_chkpntPeriod_get
    if _newclass:chkpntPeriod = property(_lsf.jobNewLog_chkpntPeriod_get, _lsf.jobNewLog_chkpntPeriod_set)
    __swig_setmethods__["restartPid"] = _lsf.jobNewLog_restartPid_set
    __swig_getmethods__["restartPid"] = _lsf.jobNewLog_restartPid_get
    if _newclass:restartPid = property(_lsf.jobNewLog_restartPid_get, _lsf.jobNewLog_restartPid_set)
    __swig_setmethods__["rLimits"] = _lsf.jobNewLog_rLimits_set
    __swig_getmethods__["rLimits"] = _lsf.jobNewLog_rLimits_get
    if _newclass:rLimits = property(_lsf.jobNewLog_rLimits_get, _lsf.jobNewLog_rLimits_set)
    __swig_setmethods__["hostSpec"] = _lsf.jobNewLog_hostSpec_set
    __swig_getmethods__["hostSpec"] = _lsf.jobNewLog_hostSpec_get
    if _newclass:hostSpec = property(_lsf.jobNewLog_hostSpec_get, _lsf.jobNewLog_hostSpec_set)
    __swig_setmethods__["hostFactor"] = _lsf.jobNewLog_hostFactor_set
    __swig_getmethods__["hostFactor"] = _lsf.jobNewLog_hostFactor_get
    if _newclass:hostFactor = property(_lsf.jobNewLog_hostFactor_get, _lsf.jobNewLog_hostFactor_set)
    __swig_setmethods__["umask"] = _lsf.jobNewLog_umask_set
    __swig_getmethods__["umask"] = _lsf.jobNewLog_umask_get
    if _newclass:umask = property(_lsf.jobNewLog_umask_get, _lsf.jobNewLog_umask_set)
    __swig_setmethods__["queue"] = _lsf.jobNewLog_queue_set
    __swig_getmethods__["queue"] = _lsf.jobNewLog_queue_get
    if _newclass:queue = property(_lsf.jobNewLog_queue_get, _lsf.jobNewLog_queue_set)
    __swig_setmethods__["resReq"] = _lsf.jobNewLog_resReq_set
    __swig_getmethods__["resReq"] = _lsf.jobNewLog_resReq_get
    if _newclass:resReq = property(_lsf.jobNewLog_resReq_get, _lsf.jobNewLog_resReq_set)
    __swig_setmethods__["fromHost"] = _lsf.jobNewLog_fromHost_set
    __swig_getmethods__["fromHost"] = _lsf.jobNewLog_fromHost_get
    if _newclass:fromHost = property(_lsf.jobNewLog_fromHost_get, _lsf.jobNewLog_fromHost_set)
    __swig_setmethods__["cwd"] = _lsf.jobNewLog_cwd_set
    __swig_getmethods__["cwd"] = _lsf.jobNewLog_cwd_get
    if _newclass:cwd = property(_lsf.jobNewLog_cwd_get, _lsf.jobNewLog_cwd_set)
    __swig_setmethods__["chkpntDir"] = _lsf.jobNewLog_chkpntDir_set
    __swig_getmethods__["chkpntDir"] = _lsf.jobNewLog_chkpntDir_get
    if _newclass:chkpntDir = property(_lsf.jobNewLog_chkpntDir_get, _lsf.jobNewLog_chkpntDir_set)
    __swig_setmethods__["inFile"] = _lsf.jobNewLog_inFile_set
    __swig_getmethods__["inFile"] = _lsf.jobNewLog_inFile_get
    if _newclass:inFile = property(_lsf.jobNewLog_inFile_get, _lsf.jobNewLog_inFile_set)
    __swig_setmethods__["outFile"] = _lsf.jobNewLog_outFile_set
    __swig_getmethods__["outFile"] = _lsf.jobNewLog_outFile_get
    if _newclass:outFile = property(_lsf.jobNewLog_outFile_get, _lsf.jobNewLog_outFile_set)
    __swig_setmethods__["errFile"] = _lsf.jobNewLog_errFile_set
    __swig_getmethods__["errFile"] = _lsf.jobNewLog_errFile_get
    if _newclass:errFile = property(_lsf.jobNewLog_errFile_get, _lsf.jobNewLog_errFile_set)
    __swig_setmethods__["inFileSpool"] = _lsf.jobNewLog_inFileSpool_set
    __swig_getmethods__["inFileSpool"] = _lsf.jobNewLog_inFileSpool_get
    if _newclass:inFileSpool = property(_lsf.jobNewLog_inFileSpool_get, _lsf.jobNewLog_inFileSpool_set)
    __swig_setmethods__["commandSpool"] = _lsf.jobNewLog_commandSpool_set
    __swig_getmethods__["commandSpool"] = _lsf.jobNewLog_commandSpool_get
    if _newclass:commandSpool = property(_lsf.jobNewLog_commandSpool_get, _lsf.jobNewLog_commandSpool_set)
    __swig_setmethods__["jobSpoolDir"] = _lsf.jobNewLog_jobSpoolDir_set
    __swig_getmethods__["jobSpoolDir"] = _lsf.jobNewLog_jobSpoolDir_get
    if _newclass:jobSpoolDir = property(_lsf.jobNewLog_jobSpoolDir_get, _lsf.jobNewLog_jobSpoolDir_set)
    __swig_setmethods__["subHomeDir"] = _lsf.jobNewLog_subHomeDir_set
    __swig_getmethods__["subHomeDir"] = _lsf.jobNewLog_subHomeDir_get
    if _newclass:subHomeDir = property(_lsf.jobNewLog_subHomeDir_get, _lsf.jobNewLog_subHomeDir_set)
    __swig_setmethods__["jobFile"] = _lsf.jobNewLog_jobFile_set
    __swig_getmethods__["jobFile"] = _lsf.jobNewLog_jobFile_get
    if _newclass:jobFile = property(_lsf.jobNewLog_jobFile_get, _lsf.jobNewLog_jobFile_set)
    __swig_setmethods__["numAskedHosts"] = _lsf.jobNewLog_numAskedHosts_set
    __swig_getmethods__["numAskedHosts"] = _lsf.jobNewLog_numAskedHosts_get
    if _newclass:numAskedHosts = property(_lsf.jobNewLog_numAskedHosts_get, _lsf.jobNewLog_numAskedHosts_set)
    __swig_setmethods__["askedHosts"] = _lsf.jobNewLog_askedHosts_set
    __swig_getmethods__["askedHosts"] = _lsf.jobNewLog_askedHosts_get
    if _newclass:askedHosts = property(_lsf.jobNewLog_askedHosts_get, _lsf.jobNewLog_askedHosts_set)
    __swig_setmethods__["dependCond"] = _lsf.jobNewLog_dependCond_set
    __swig_getmethods__["dependCond"] = _lsf.jobNewLog_dependCond_get
    if _newclass:dependCond = property(_lsf.jobNewLog_dependCond_get, _lsf.jobNewLog_dependCond_set)
    __swig_setmethods__["timeEvent"] = _lsf.jobNewLog_timeEvent_set
    __swig_getmethods__["timeEvent"] = _lsf.jobNewLog_timeEvent_get
    if _newclass:timeEvent = property(_lsf.jobNewLog_timeEvent_get, _lsf.jobNewLog_timeEvent_set)
    __swig_setmethods__["jobName"] = _lsf.jobNewLog_jobName_set
    __swig_getmethods__["jobName"] = _lsf.jobNewLog_jobName_get
    if _newclass:jobName = property(_lsf.jobNewLog_jobName_get, _lsf.jobNewLog_jobName_set)
    __swig_setmethods__["command"] = _lsf.jobNewLog_command_set
    __swig_getmethods__["command"] = _lsf.jobNewLog_command_get
    if _newclass:command = property(_lsf.jobNewLog_command_get, _lsf.jobNewLog_command_set)
    __swig_setmethods__["nxf"] = _lsf.jobNewLog_nxf_set
    __swig_getmethods__["nxf"] = _lsf.jobNewLog_nxf_get
    if _newclass:nxf = property(_lsf.jobNewLog_nxf_get, _lsf.jobNewLog_nxf_set)
    __swig_setmethods__["xf"] = _lsf.jobNewLog_xf_set
    __swig_getmethods__["xf"] = _lsf.jobNewLog_xf_get
    if _newclass:xf = property(_lsf.jobNewLog_xf_get, _lsf.jobNewLog_xf_set)
    __swig_setmethods__["preExecCmd"] = _lsf.jobNewLog_preExecCmd_set
    __swig_getmethods__["preExecCmd"] = _lsf.jobNewLog_preExecCmd_get
    if _newclass:preExecCmd = property(_lsf.jobNewLog_preExecCmd_get, _lsf.jobNewLog_preExecCmd_set)
    __swig_setmethods__["mailUser"] = _lsf.jobNewLog_mailUser_set
    __swig_getmethods__["mailUser"] = _lsf.jobNewLog_mailUser_get
    if _newclass:mailUser = property(_lsf.jobNewLog_mailUser_get, _lsf.jobNewLog_mailUser_set)
    __swig_setmethods__["projectName"] = _lsf.jobNewLog_projectName_set
    __swig_getmethods__["projectName"] = _lsf.jobNewLog_projectName_get
    if _newclass:projectName = property(_lsf.jobNewLog_projectName_get, _lsf.jobNewLog_projectName_set)
    __swig_setmethods__["niosPort"] = _lsf.jobNewLog_niosPort_set
    __swig_getmethods__["niosPort"] = _lsf.jobNewLog_niosPort_get
    if _newclass:niosPort = property(_lsf.jobNewLog_niosPort_get, _lsf.jobNewLog_niosPort_set)
    __swig_setmethods__["maxNumProcessors"] = _lsf.jobNewLog_maxNumProcessors_set
    __swig_getmethods__["maxNumProcessors"] = _lsf.jobNewLog_maxNumProcessors_get
    if _newclass:maxNumProcessors = property(_lsf.jobNewLog_maxNumProcessors_get, _lsf.jobNewLog_maxNumProcessors_set)
    __swig_setmethods__["schedHostType"] = _lsf.jobNewLog_schedHostType_set
    __swig_getmethods__["schedHostType"] = _lsf.jobNewLog_schedHostType_get
    if _newclass:schedHostType = property(_lsf.jobNewLog_schedHostType_get, _lsf.jobNewLog_schedHostType_set)
    __swig_setmethods__["loginShell"] = _lsf.jobNewLog_loginShell_set
    __swig_getmethods__["loginShell"] = _lsf.jobNewLog_loginShell_get
    if _newclass:loginShell = property(_lsf.jobNewLog_loginShell_get, _lsf.jobNewLog_loginShell_set)
    __swig_setmethods__["userGroup"] = _lsf.jobNewLog_userGroup_set
    __swig_getmethods__["userGroup"] = _lsf.jobNewLog_userGroup_get
    if _newclass:userGroup = property(_lsf.jobNewLog_userGroup_get, _lsf.jobNewLog_userGroup_set)
    __swig_setmethods__["exceptList"] = _lsf.jobNewLog_exceptList_set
    __swig_getmethods__["exceptList"] = _lsf.jobNewLog_exceptList_get
    if _newclass:exceptList = property(_lsf.jobNewLog_exceptList_get, _lsf.jobNewLog_exceptList_set)
    __swig_setmethods__["idx"] = _lsf.jobNewLog_idx_set
    __swig_getmethods__["idx"] = _lsf.jobNewLog_idx_get
    if _newclass:idx = property(_lsf.jobNewLog_idx_get, _lsf.jobNewLog_idx_set)
    __swig_setmethods__["userPriority"] = _lsf.jobNewLog_userPriority_set
    __swig_getmethods__["userPriority"] = _lsf.jobNewLog_userPriority_get
    if _newclass:userPriority = property(_lsf.jobNewLog_userPriority_get, _lsf.jobNewLog_userPriority_set)
    __swig_setmethods__["rsvId"] = _lsf.jobNewLog_rsvId_set
    __swig_getmethods__["rsvId"] = _lsf.jobNewLog_rsvId_get
    if _newclass:rsvId = property(_lsf.jobNewLog_rsvId_get, _lsf.jobNewLog_rsvId_set)
    __swig_setmethods__["jobGroup"] = _lsf.jobNewLog_jobGroup_set
    __swig_getmethods__["jobGroup"] = _lsf.jobNewLog_jobGroup_get
    if _newclass:jobGroup = property(_lsf.jobNewLog_jobGroup_get, _lsf.jobNewLog_jobGroup_set)
    __swig_setmethods__["extsched"] = _lsf.jobNewLog_extsched_set
    __swig_getmethods__["extsched"] = _lsf.jobNewLog_extsched_get
    if _newclass:extsched = property(_lsf.jobNewLog_extsched_get, _lsf.jobNewLog_extsched_set)
    __swig_setmethods__["warningTimePeriod"] = _lsf.jobNewLog_warningTimePeriod_set
    __swig_getmethods__["warningTimePeriod"] = _lsf.jobNewLog_warningTimePeriod_get
    if _newclass:warningTimePeriod = property(_lsf.jobNewLog_warningTimePeriod_get, _lsf.jobNewLog_warningTimePeriod_set)
    __swig_setmethods__["warningAction"] = _lsf.jobNewLog_warningAction_set
    __swig_getmethods__["warningAction"] = _lsf.jobNewLog_warningAction_get
    if _newclass:warningAction = property(_lsf.jobNewLog_warningAction_get, _lsf.jobNewLog_warningAction_set)
    __swig_setmethods__["sla"] = _lsf.jobNewLog_sla_set
    __swig_getmethods__["sla"] = _lsf.jobNewLog_sla_get
    if _newclass:sla = property(_lsf.jobNewLog_sla_get, _lsf.jobNewLog_sla_set)
    __swig_setmethods__["SLArunLimit"] = _lsf.jobNewLog_SLArunLimit_set
    __swig_getmethods__["SLArunLimit"] = _lsf.jobNewLog_SLArunLimit_get
    if _newclass:SLArunLimit = property(_lsf.jobNewLog_SLArunLimit_get, _lsf.jobNewLog_SLArunLimit_set)
    __swig_setmethods__["licenseProject"] = _lsf.jobNewLog_licenseProject_set
    __swig_getmethods__["licenseProject"] = _lsf.jobNewLog_licenseProject_get
    if _newclass:licenseProject = property(_lsf.jobNewLog_licenseProject_get, _lsf.jobNewLog_licenseProject_set)
    __swig_setmethods__["options3"] = _lsf.jobNewLog_options3_set
    __swig_getmethods__["options3"] = _lsf.jobNewLog_options3_get
    if _newclass:options3 = property(_lsf.jobNewLog_options3_get, _lsf.jobNewLog_options3_set)
    __swig_setmethods__["app"] = _lsf.jobNewLog_app_set
    __swig_getmethods__["app"] = _lsf.jobNewLog_app_get
    if _newclass:app = property(_lsf.jobNewLog_app_get, _lsf.jobNewLog_app_set)
    __swig_setmethods__["postExecCmd"] = _lsf.jobNewLog_postExecCmd_set
    __swig_getmethods__["postExecCmd"] = _lsf.jobNewLog_postExecCmd_get
    if _newclass:postExecCmd = property(_lsf.jobNewLog_postExecCmd_get, _lsf.jobNewLog_postExecCmd_set)
    __swig_setmethods__["runtimeEstimation"] = _lsf.jobNewLog_runtimeEstimation_set
    __swig_getmethods__["runtimeEstimation"] = _lsf.jobNewLog_runtimeEstimation_get
    if _newclass:runtimeEstimation = property(_lsf.jobNewLog_runtimeEstimation_get, _lsf.jobNewLog_runtimeEstimation_set)
    __swig_setmethods__["requeueEValues"] = _lsf.jobNewLog_requeueEValues_set
    __swig_getmethods__["requeueEValues"] = _lsf.jobNewLog_requeueEValues_get
    if _newclass:requeueEValues = property(_lsf.jobNewLog_requeueEValues_get, _lsf.jobNewLog_requeueEValues_set)
    __swig_setmethods__["initChkpntPeriod"] = _lsf.jobNewLog_initChkpntPeriod_set
    __swig_getmethods__["initChkpntPeriod"] = _lsf.jobNewLog_initChkpntPeriod_get
    if _newclass:initChkpntPeriod = property(_lsf.jobNewLog_initChkpntPeriod_get, _lsf.jobNewLog_initChkpntPeriod_set)
    __swig_setmethods__["migThreshold"] = _lsf.jobNewLog_migThreshold_set
    __swig_getmethods__["migThreshold"] = _lsf.jobNewLog_migThreshold_get
    if _newclass:migThreshold = property(_lsf.jobNewLog_migThreshold_get, _lsf.jobNewLog_migThreshold_set)
    __swig_setmethods__["notifyCmd"] = _lsf.jobNewLog_notifyCmd_set
    __swig_getmethods__["notifyCmd"] = _lsf.jobNewLog_notifyCmd_get
    if _newclass:notifyCmd = property(_lsf.jobNewLog_notifyCmd_get, _lsf.jobNewLog_notifyCmd_set)
    __swig_setmethods__["jobDescription"] = _lsf.jobNewLog_jobDescription_set
    __swig_getmethods__["jobDescription"] = _lsf.jobNewLog_jobDescription_get
    if _newclass:jobDescription = property(_lsf.jobNewLog_jobDescription_get, _lsf.jobNewLog_jobDescription_set)
    __swig_setmethods__["submitExt"] = _lsf.jobNewLog_submitExt_set
    __swig_getmethods__["submitExt"] = _lsf.jobNewLog_submitExt_get
    if _newclass:submitExt = property(_lsf.jobNewLog_submitExt_get, _lsf.jobNewLog_submitExt_set)
    def __init__(self, *args): 
        this = _lsf.new_jobNewLog(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _lsf.delete_jobNewLog
    __del__ = lambda self : None;
jobNewLog_swigregister = _lsf.jobNewLog_swigregister
jobNewLog_swigregister(jobNewLog)

class jobModLog(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, jobModLog, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, jobModLog, name)
    __repr__ = _swig_repr
    __swig_setmethods__["jobIdStr"] = _lsf.jobModLog_jobIdStr_set
    __swig_getmethods__["jobIdStr"] = _lsf.jobModLog_jobIdStr_get
    if _newclass:jobIdStr = property(_lsf.jobModLog_jobIdStr_get, _lsf.jobModLog_jobIdStr_set)
    __swig_setmethods__["options"] = _lsf.jobModLog_options_set
    __swig_getmethods__["options"] = _lsf.jobModLog_options_get
    if _newclass:options = property(_lsf.jobModLog_options_get, _lsf.jobModLog_options_set)
    __swig_setmethods__["options2"] = _lsf.jobModLog_options2_set
    __swig_getmethods__["options2"] = _lsf.jobModLog_options2_get
    if _newclass:options2 = property(_lsf.jobModLog_options2_get, _lsf.jobModLog_options2_set)
    __swig_setmethods__["delOptions"] = _lsf.jobModLog_delOptions_set
    __swig_getmethods__["delOptions"] = _lsf.jobModLog_delOptions_get
    if _newclass:delOptions = property(_lsf.jobModLog_delOptions_get, _lsf.jobModLog_delOptions_set)
    __swig_setmethods__["delOptions2"] = _lsf.jobModLog_delOptions2_set
    __swig_getmethods__["delOptions2"] = _lsf.jobModLog_delOptions2_get
    if _newclass:delOptions2 = property(_lsf.jobModLog_delOptions2_get, _lsf.jobModLog_delOptions2_set)
    __swig_setmethods__["userId"] = _lsf.jobModLog_userId_set
    __swig_getmethods__["userId"] = _lsf.jobModLog_userId_get
    if _newclass:userId = property(_lsf.jobModLog_userId_get, _lsf.jobModLog_userId_set)
    __swig_setmethods__["userName"] = _lsf.jobModLog_userName_set
    __swig_getmethods__["userName"] = _lsf.jobModLog_userName_get
    if _newclass:userName = property(_lsf.jobModLog_userName_get, _lsf.jobModLog_userName_set)
    __swig_setmethods__["submitTime"] = _lsf.jobModLog_submitTime_set
    __swig_getmethods__["submitTime"] = _lsf.jobModLog_submitTime_get
    if _newclass:submitTime = property(_lsf.jobModLog_submitTime_get, _lsf.jobModLog_submitTime_set)
    __swig_setmethods__["umask"] = _lsf.jobModLog_umask_set
    __swig_getmethods__["umask"] = _lsf.jobModLog_umask_get
    if _newclass:umask = property(_lsf.jobModLog_umask_get, _lsf.jobModLog_umask_set)
    __swig_setmethods__["numProcessors"] = _lsf.jobModLog_numProcessors_set
    __swig_getmethods__["numProcessors"] = _lsf.jobModLog_numProcessors_get
    if _newclass:numProcessors = property(_lsf.jobModLog_numProcessors_get, _lsf.jobModLog_numProcessors_set)
    __swig_setmethods__["beginTime"] = _lsf.jobModLog_beginTime_set
    __swig_getmethods__["beginTime"] = _lsf.jobModLog_beginTime_get
    if _newclass:beginTime = property(_lsf.jobModLog_beginTime_get, _lsf.jobModLog_beginTime_set)
    __swig_setmethods__["termTime"] = _lsf.jobModLog_termTime_set
    __swig_getmethods__["termTime"] = _lsf.jobModLog_termTime_get
    if _newclass:termTime = property(_lsf.jobModLog_termTime_get, _lsf.jobModLog_termTime_set)
    __swig_setmethods__["sigValue"] = _lsf.jobModLog_sigValue_set
    __swig_getmethods__["sigValue"] = _lsf.jobModLog_sigValue_get
    if _newclass:sigValue = property(_lsf.jobModLog_sigValue_get, _lsf.jobModLog_sigValue_set)
    __swig_setmethods__["restartPid"] = _lsf.jobModLog_restartPid_set
    __swig_getmethods__["restartPid"] = _lsf.jobModLog_restartPid_get
    if _newclass:restartPid = property(_lsf.jobModLog_restartPid_get, _lsf.jobModLog_restartPid_set)
    __swig_setmethods__["jobName"] = _lsf.jobModLog_jobName_set
    __swig_getmethods__["jobName"] = _lsf.jobModLog_jobName_get
    if _newclass:jobName = property(_lsf.jobModLog_jobName_get, _lsf.jobModLog_jobName_set)
    __swig_setmethods__["queue"] = _lsf.jobModLog_queue_set
    __swig_getmethods__["queue"] = _lsf.jobModLog_queue_get
    if _newclass:queue = property(_lsf.jobModLog_queue_get, _lsf.jobModLog_queue_set)
    __swig_setmethods__["numAskedHosts"] = _lsf.jobModLog_numAskedHosts_set
    __swig_getmethods__["numAskedHosts"] = _lsf.jobModLog_numAskedHosts_get
    if _newclass:numAskedHosts = property(_lsf.jobModLog_numAskedHosts_get, _lsf.jobModLog_numAskedHosts_set)
    __swig_setmethods__["askedHosts"] = _lsf.jobModLog_askedHosts_set
    __swig_getmethods__["askedHosts"] = _lsf.jobModLog_askedHosts_get
    if _newclass:askedHosts = property(_lsf.jobModLog_askedHosts_get, _lsf.jobModLog_askedHosts_set)
    __swig_setmethods__["resReq"] = _lsf.jobModLog_resReq_set
    __swig_getmethods__["resReq"] = _lsf.jobModLog_resReq_get
    if _newclass:resReq = property(_lsf.jobModLog_resReq_get, _lsf.jobModLog_resReq_set)
    __swig_setmethods__["rLimits"] = _lsf.jobModLog_rLimits_set
    __swig_getmethods__["rLimits"] = _lsf.jobModLog_rLimits_get
    if _newclass:rLimits = property(_lsf.jobModLog_rLimits_get, _lsf.jobModLog_rLimits_set)
    __swig_setmethods__["hostSpec"] = _lsf.jobModLog_hostSpec_set
    __swig_getmethods__["hostSpec"] = _lsf.jobModLog_hostSpec_get
    if _newclass:hostSpec = property(_lsf.jobModLog_hostSpec_get, _lsf.jobModLog_hostSpec_set)
    __swig_setmethods__["dependCond"] = _lsf.jobModLog_dependCond_set
    __swig_getmethods__["dependCond"] = _lsf.jobModLog_dependCond_get
    if _newclass:dependCond = property(_lsf.jobModLog_dependCond_get, _lsf.jobModLog_dependCond_set)
    __swig_setmethods__["timeEvent"] = _lsf.jobModLog_timeEvent_set
    __swig_getmethods__["timeEvent"] = _lsf.jobModLog_timeEvent_get
    if _newclass:timeEvent = property(_lsf.jobModLog_timeEvent_get, _lsf.jobModLog_timeEvent_set)
    __swig_setmethods__["subHomeDir"] = _lsf.jobModLog_subHomeDir_set
    __swig_getmethods__["subHomeDir"] = _lsf.jobModLog_subHomeDir_get
    if _newclass:subHomeDir = property(_lsf.jobModLog_subHomeDir_get, _lsf.jobModLog_subHomeDir_set)
    __swig_setmethods__["inFile"] = _lsf.jobModLog_inFile_set
    __swig_getmethods__["inFile"] = _lsf.jobModLog_inFile_get
    if _newclass:inFile = property(_lsf.jobModLog_inFile_get, _lsf.jobModLog_inFile_set)
    __swig_setmethods__["outFile"] = _lsf.jobModLog_outFile_set
    __swig_getmethods__["outFile"] = _lsf.jobModLog_outFile_get
    if _newclass:outFile = property(_lsf.jobModLog_outFile_get, _lsf.jobModLog_outFile_set)
    __swig_setmethods__["errFile"] = _lsf.jobModLog_errFile_set
    __swig_getmethods__["errFile"] = _lsf.jobModLog_errFile_get
    if _newclass:errFile = property(_lsf.jobModLog_errFile_get, _lsf.jobModLog_errFile_set)
    __swig_setmethods__["command"] = _lsf.jobModLog_command_set
    __swig_getmethods__["command"] = _lsf.jobModLog_command_get
    if _newclass:command = property(_lsf.jobModLog_command_get, _lsf.jobModLog_command_set)
    __swig_setmethods__["inFileSpool"] = _lsf.jobModLog_inFileSpool_set
    __swig_getmethods__["inFileSpool"] = _lsf.jobModLog_inFileSpool_get
    if _newclass:inFileSpool = property(_lsf.jobModLog_inFileSpool_get, _lsf.jobModLog_inFileSpool_set)
    __swig_setmethods__["commandSpool"] = _lsf.jobModLog_commandSpool_set
    __swig_getmethods__["commandSpool"] = _lsf.jobModLog_commandSpool_get
    if _newclass:commandSpool = property(_lsf.jobModLog_commandSpool_get, _lsf.jobModLog_commandSpool_set)
    __swig_setmethods__["chkpntPeriod"] = _lsf.jobModLog_chkpntPeriod_set
    __swig_getmethods__["chkpntPeriod"] = _lsf.jobModLog_chkpntPeriod_get
    if _newclass:chkpntPeriod = property(_lsf.jobModLog_chkpntPeriod_get, _lsf.jobModLog_chkpntPeriod_set)
    __swig_setmethods__["chkpntDir"] = _lsf.jobModLog_chkpntDir_set
    __swig_getmethods__["chkpntDir"] = _lsf.jobModLog_chkpntDir_get
    if _newclass:chkpntDir = property(_lsf.jobModLog_chkpntDir_get, _lsf.jobModLog_chkpntDir_set)
    __swig_setmethods__["nxf"] = _lsf.jobModLog_nxf_set
    __swig_getmethods__["nxf"] = _lsf.jobModLog_nxf_get
    if _newclass:nxf = property(_lsf.jobModLog_nxf_get, _lsf.jobModLog_nxf_set)
    __swig_setmethods__["xf"] = _lsf.jobModLog_xf_set
    __swig_getmethods__["xf"] = _lsf.jobModLog_xf_get
    if _newclass:xf = property(_lsf.jobModLog_xf_get, _lsf.jobModLog_xf_set)
    __swig_setmethods__["jobFile"] = _lsf.jobModLog_jobFile_set
    __swig_getmethods__["jobFile"] = _lsf.jobModLog_jobFile_get
    if _newclass:jobFile = property(_lsf.jobModLog_jobFile_get, _lsf.jobModLog_jobFile_set)
    __swig_setmethods__["fromHost"] = _lsf.jobModLog_fromHost_set
    __swig_getmethods__["fromHost"] = _lsf.jobModLog_fromHost_get
    if _newclass:fromHost = property(_lsf.jobModLog_fromHost_get, _lsf.jobModLog_fromHost_set)
    __swig_setmethods__["cwd"] = _lsf.jobModLog_cwd_set
    __swig_getmethods__["cwd"] = _lsf.jobModLog_cwd_get
    if _newclass:cwd = property(_lsf.jobModLog_cwd_get, _lsf.jobModLog_cwd_set)
    __swig_setmethods__["preExecCmd"] = _lsf.jobModLog_preExecCmd_set
    __swig_getmethods__["preExecCmd"] = _lsf.jobModLog_preExecCmd_get
    if _newclass:preExecCmd = property(_lsf.jobModLog_preExecCmd_get, _lsf.jobModLog_preExecCmd_set)
    __swig_setmethods__["mailUser"] = _lsf.jobModLog_mailUser_set
    __swig_getmethods__["mailUser"] = _lsf.jobModLog_mailUser_get
    if _newclass:mailUser = property(_lsf.jobModLog_mailUser_get, _lsf.jobModLog_mailUser_set)
    __swig_setmethods__["projectName"] = _lsf.jobModLog_projectName_set
    __swig_getmethods__["projectName"] = _lsf.jobModLog_projectName_get
    if _newclass:projectName = property(_lsf.jobModLog_projectName_get, _lsf.jobModLog_projectName_set)
    __swig_setmethods__["niosPort"] = _lsf.jobModLog_niosPort_set
    __swig_getmethods__["niosPort"] = _lsf.jobModLog_niosPort_get
    if _newclass:niosPort = property(_lsf.jobModLog_niosPort_get, _lsf.jobModLog_niosPort_set)
    __swig_setmethods__["maxNumProcessors"] = _lsf.jobModLog_maxNumProcessors_set
    __swig_getmethods__["maxNumProcessors"] = _lsf.jobModLog_maxNumProcessors_get
    if _newclass:maxNumProcessors = property(_lsf.jobModLog_maxNumProcessors_get, _lsf.jobModLog_maxNumProcessors_set)
    __swig_setmethods__["loginShell"] = _lsf.jobModLog_loginShell_set
    __swig_getmethods__["loginShell"] = _lsf.jobModLog_loginShell_get
    if _newclass:loginShell = property(_lsf.jobModLog_loginShell_get, _lsf.jobModLog_loginShell_set)
    __swig_setmethods__["schedHostType"] = _lsf.jobModLog_schedHostType_set
    __swig_getmethods__["schedHostType"] = _lsf.jobModLog_schedHostType_get
    if _newclass:schedHostType = property(_lsf.jobModLog_schedHostType_get, _lsf.jobModLog_schedHostType_set)
    __swig_setmethods__["userGroup"] = _lsf.jobModLog_userGroup_set
    __swig_getmethods__["userGroup"] = _lsf.jobModLog_userGroup_get
    if _newclass:userGroup = property(_lsf.jobModLog_userGroup_get, _lsf.jobModLog_userGroup_set)
    __swig_setmethods__["exceptList"] = _lsf.jobModLog_exceptList_set
    __swig_getmethods__["exceptList"] = _lsf.jobModLog_exceptList_get
    if _newclass:exceptList = property(_lsf.jobModLog_exceptList_get, _lsf.jobModLog_exceptList_set)
    __swig_setmethods__["userPriority"] = _lsf.jobModLog_userPriority_set
    __swig_getmethods__["userPriority"] = _lsf.jobModLog_userPriority_get
    if _newclass:userPriority = property(_lsf.jobModLog_userPriority_get, _lsf.jobModLog_userPriority_set)
    __swig_setmethods__["rsvId"] = _lsf.jobModLog_rsvId_set
    __swig_getmethods__["rsvId"] = _lsf.jobModLog_rsvId_get
    if _newclass:rsvId = property(_lsf.jobModLog_rsvId_get, _lsf.jobModLog_rsvId_set)
    __swig_setmethods__["extsched"] = _lsf.jobModLog_extsched_set
    __swig_getmethods__["extsched"] = _lsf.jobModLog_extsched_get
    if _newclass:extsched = property(_lsf.jobModLog_extsched_get, _lsf.jobModLog_extsched_set)
    __swig_setmethods__["warningTimePeriod"] = _lsf.jobModLog_warningTimePeriod_set
    __swig_getmethods__["warningTimePeriod"] = _lsf.jobModLog_warningTimePeriod_get
    if _newclass:warningTimePeriod = property(_lsf.jobModLog_warningTimePeriod_get, _lsf.jobModLog_warningTimePeriod_set)
    __swig_setmethods__["warningAction"] = _lsf.jobModLog_warningAction_set
    __swig_getmethods__["warningAction"] = _lsf.jobModLog_warningAction_get
    if _newclass:warningAction = property(_lsf.jobModLog_warningAction_get, _lsf.jobModLog_warningAction_set)
    __swig_setmethods__["jobGroup"] = _lsf.jobModLog_jobGroup_set
    __swig_getmethods__["jobGroup"] = _lsf.jobModLog_jobGroup_get
    if _newclass:jobGroup = property(_lsf.jobModLog_jobGroup_get, _lsf.jobModLog_jobGroup_set)
    __swig_setmethods__["sla"] = _lsf.jobModLog_sla_set
    __swig_getmethods__["sla"] = _lsf.jobModLog_sla_get
    if _newclass:sla = property(_lsf.jobModLog_sla_get, _lsf.jobModLog_sla_set)
    __swig_setmethods__["licenseProject"] = _lsf.jobModLog_licenseProject_set
    __swig_getmethods__["licenseProject"] = _lsf.jobModLog_licenseProject_get
    if _newclass:licenseProject = property(_lsf.jobModLog_licenseProject_get, _lsf.jobModLog_licenseProject_set)
    __swig_setmethods__["options3"] = _lsf.jobModLog_options3_set
    __swig_getmethods__["options3"] = _lsf.jobModLog_options3_get
    if _newclass:options3 = property(_lsf.jobModLog_options3_get, _lsf.jobModLog_options3_set)
    __swig_setmethods__["delOptions3"] = _lsf.jobModLog_delOptions3_set
    __swig_getmethods__["delOptions3"] = _lsf.jobModLog_delOptions3_get
    if _newclass:delOptions3 = property(_lsf.jobModLog_delOptions3_get, _lsf.jobModLog_delOptions3_set)
    __swig_setmethods__["app"] = _lsf.jobModLog_app_set
    __swig_getmethods__["app"] = _lsf.jobModLog_app_get
    if _newclass:app = property(_lsf.jobModLog_app_get, _lsf.jobModLog_app_set)
    __swig_setmethods__["apsString"] = _lsf.jobModLog_apsString_set
    __swig_getmethods__["apsString"] = _lsf.jobModLog_apsString_get
    if _newclass:apsString = property(_lsf.jobModLog_apsString_get, _lsf.jobModLog_apsString_set)
    __swig_setmethods__["postExecCmd"] = _lsf.jobModLog_postExecCmd_set
    __swig_getmethods__["postExecCmd"] = _lsf.jobModLog_postExecCmd_get
    if _newclass:postExecCmd = property(_lsf.jobModLog_postExecCmd_get, _lsf.jobModLog_postExecCmd_set)
    __swig_setmethods__["runtimeEstimation"] = _lsf.jobModLog_runtimeEstimation_set
    __swig_getmethods__["runtimeEstimation"] = _lsf.jobModLog_runtimeEstimation_get
    if _newclass:runtimeEstimation = property(_lsf.jobModLog_runtimeEstimation_get, _lsf.jobModLog_runtimeEstimation_set)
    __swig_setmethods__["requeueEValues"] = _lsf.jobModLog_requeueEValues_set
    __swig_getmethods__["requeueEValues"] = _lsf.jobModLog_requeueEValues_get
    if _newclass:requeueEValues = property(_lsf.jobModLog_requeueEValues_get, _lsf.jobModLog_requeueEValues_set)
    __swig_setmethods__["initChkpntPeriod"] = _lsf.jobModLog_initChkpntPeriod_set
    __swig_getmethods__["initChkpntPeriod"] = _lsf.jobModLog_initChkpntPeriod_get
    if _newclass:initChkpntPeriod = property(_lsf.jobModLog_initChkpntPeriod_get, _lsf.jobModLog_initChkpntPeriod_set)
    __swig_setmethods__["migThreshold"] = _lsf.jobModLog_migThreshold_set
    __swig_getmethods__["migThreshold"] = _lsf.jobModLog_migThreshold_get
    if _newclass:migThreshold = property(_lsf.jobModLog_migThreshold_get, _lsf.jobModLog_migThreshold_set)
    __swig_setmethods__["notifyCmd"] = _lsf.jobModLog_notifyCmd_set
    __swig_getmethods__["notifyCmd"] = _lsf.jobModLog_notifyCmd_get
    if _newclass:notifyCmd = property(_lsf.jobModLog_notifyCmd_get, _lsf.jobModLog_notifyCmd_set)
    __swig_setmethods__["jobDescription"] = _lsf.jobModLog_jobDescription_set
    __swig_getmethods__["jobDescription"] = _lsf.jobModLog_jobDescription_get
    if _newclass:jobDescription = property(_lsf.jobModLog_jobDescription_get, _lsf.jobModLog_jobDescription_set)
    __swig_setmethods__["submitExt"] = _lsf.jobModLog_submitExt_set
    __swig_getmethods__["submitExt"] = _lsf.jobModLog_submitExt_get
    if _newclass:submitExt = property(_lsf.jobModLog_submitExt_get, _lsf.jobModLog_submitExt_set)
    def __init__(self, *args): 
        this = _lsf.new_jobModLog(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _lsf.delete_jobModLog
    __del__ = lambda self : None;
jobModLog_swigregister = _lsf.jobModLog_swigregister
jobModLog_swigregister(jobModLog)

class jobStartLog(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, jobStartLog, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, jobStartLog, name)
    __repr__ = _swig_repr
    __swig_setmethods__["jobId"] = _lsf.jobStartLog_jobId_set
    __swig_getmethods__["jobId"] = _lsf.jobStartLog_jobId_get
    if _newclass:jobId = property(_lsf.jobStartLog_jobId_get, _lsf.jobStartLog_jobId_set)
    __swig_setmethods__["jStatus"] = _lsf.jobStartLog_jStatus_set
    __swig_getmethods__["jStatus"] = _lsf.jobStartLog_jStatus_get
    if _newclass:jStatus = property(_lsf.jobStartLog_jStatus_get, _lsf.jobStartLog_jStatus_set)
    __swig_setmethods__["jobPid"] = _lsf.jobStartLog_jobPid_set
    __swig_getmethods__["jobPid"] = _lsf.jobStartLog_jobPid_get
    if _newclass:jobPid = property(_lsf.jobStartLog_jobPid_get, _lsf.jobStartLog_jobPid_set)
    __swig_setmethods__["jobPGid"] = _lsf.jobStartLog_jobPGid_set
    __swig_getmethods__["jobPGid"] = _lsf.jobStartLog_jobPGid_get
    if _newclass:jobPGid = property(_lsf.jobStartLog_jobPGid_get, _lsf.jobStartLog_jobPGid_set)
    __swig_setmethods__["hostFactor"] = _lsf.jobStartLog_hostFactor_set
    __swig_getmethods__["hostFactor"] = _lsf.jobStartLog_hostFactor_get
    if _newclass:hostFactor = property(_lsf.jobStartLog_hostFactor_get, _lsf.jobStartLog_hostFactor_set)
    __swig_setmethods__["numExHosts"] = _lsf.jobStartLog_numExHosts_set
    __swig_getmethods__["numExHosts"] = _lsf.jobStartLog_numExHosts_get
    if _newclass:numExHosts = property(_lsf.jobStartLog_numExHosts_get, _lsf.jobStartLog_numExHosts_set)
    __swig_setmethods__["execHosts"] = _lsf.jobStartLog_execHosts_set
    __swig_getmethods__["execHosts"] = _lsf.jobStartLog_execHosts_get
    if _newclass:execHosts = property(_lsf.jobStartLog_execHosts_get, _lsf.jobStartLog_execHosts_set)
    __swig_setmethods__["queuePreCmd"] = _lsf.jobStartLog_queuePreCmd_set
    __swig_getmethods__["queuePreCmd"] = _lsf.jobStartLog_queuePreCmd_get
    if _newclass:queuePreCmd = property(_lsf.jobStartLog_queuePreCmd_get, _lsf.jobStartLog_queuePreCmd_set)
    __swig_setmethods__["queuePostCmd"] = _lsf.jobStartLog_queuePostCmd_set
    __swig_getmethods__["queuePostCmd"] = _lsf.jobStartLog_queuePostCmd_get
    if _newclass:queuePostCmd = property(_lsf.jobStartLog_queuePostCmd_get, _lsf.jobStartLog_queuePostCmd_set)
    __swig_setmethods__["jFlags"] = _lsf.jobStartLog_jFlags_set
    __swig_getmethods__["jFlags"] = _lsf.jobStartLog_jFlags_get
    if _newclass:jFlags = property(_lsf.jobStartLog_jFlags_get, _lsf.jobStartLog_jFlags_set)
    __swig_setmethods__["userGroup"] = _lsf.jobStartLog_userGroup_set
    __swig_getmethods__["userGroup"] = _lsf.jobStartLog_userGroup_get
    if _newclass:userGroup = property(_lsf.jobStartLog_userGroup_get, _lsf.jobStartLog_userGroup_set)
    __swig_setmethods__["idx"] = _lsf.jobStartLog_idx_set
    __swig_getmethods__["idx"] = _lsf.jobStartLog_idx_get
    if _newclass:idx = property(_lsf.jobStartLog_idx_get, _lsf.jobStartLog_idx_set)
    __swig_setmethods__["additionalInfo"] = _lsf.jobStartLog_additionalInfo_set
    __swig_getmethods__["additionalInfo"] = _lsf.jobStartLog_additionalInfo_get
    if _newclass:additionalInfo = property(_lsf.jobStartLog_additionalInfo_get, _lsf.jobStartLog_additionalInfo_set)
    __swig_setmethods__["duration4PreemptBackfill"] = _lsf.jobStartLog_duration4PreemptBackfill_set
    __swig_getmethods__["duration4PreemptBackfill"] = _lsf.jobStartLog_duration4PreemptBackfill_get
    if _newclass:duration4PreemptBackfill = property(_lsf.jobStartLog_duration4PreemptBackfill_get, _lsf.jobStartLog_duration4PreemptBackfill_set)
    __swig_setmethods__["jFlags2"] = _lsf.jobStartLog_jFlags2_set
    __swig_getmethods__["jFlags2"] = _lsf.jobStartLog_jFlags2_get
    if _newclass:jFlags2 = property(_lsf.jobStartLog_jFlags2_get, _lsf.jobStartLog_jFlags2_set)
    def __init__(self, *args): 
        this = _lsf.new_jobStartLog(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _lsf.delete_jobStartLog
    __del__ = lambda self : None;
jobStartLog_swigregister = _lsf.jobStartLog_swigregister
jobStartLog_swigregister(jobStartLog)

class jobStartAcceptLog(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, jobStartAcceptLog, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, jobStartAcceptLog, name)
    __repr__ = _swig_repr
    __swig_setmethods__["jobId"] = _lsf.jobStartAcceptLog_jobId_set
    __swig_getmethods__["jobId"] = _lsf.jobStartAcceptLog_jobId_get
    if _newclass:jobId = property(_lsf.jobStartAcceptLog_jobId_get, _lsf.jobStartAcceptLog_jobId_set)
    __swig_setmethods__["jobPid"] = _lsf.jobStartAcceptLog_jobPid_set
    __swig_getmethods__["jobPid"] = _lsf.jobStartAcceptLog_jobPid_get
    if _newclass:jobPid = property(_lsf.jobStartAcceptLog_jobPid_get, _lsf.jobStartAcceptLog_jobPid_set)
    __swig_setmethods__["jobPGid"] = _lsf.jobStartAcceptLog_jobPGid_set
    __swig_getmethods__["jobPGid"] = _lsf.jobStartAcceptLog_jobPGid_get
    if _newclass:jobPGid = property(_lsf.jobStartAcceptLog_jobPGid_get, _lsf.jobStartAcceptLog_jobPGid_set)
    __swig_setmethods__["idx"] = _lsf.jobStartAcceptLog_idx_set
    __swig_getmethods__["idx"] = _lsf.jobStartAcceptLog_idx_get
    if _newclass:idx = property(_lsf.jobStartAcceptLog_idx_get, _lsf.jobStartAcceptLog_idx_set)
    def __init__(self, *args): 
        this = _lsf.new_jobStartAcceptLog(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _lsf.delete_jobStartAcceptLog
    __del__ = lambda self : None;
jobStartAcceptLog_swigregister = _lsf.jobStartAcceptLog_swigregister
jobStartAcceptLog_swigregister(jobStartAcceptLog)

class jobExecuteLog(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, jobExecuteLog, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, jobExecuteLog, name)
    __repr__ = _swig_repr
    __swig_setmethods__["jobId"] = _lsf.jobExecuteLog_jobId_set
    __swig_getmethods__["jobId"] = _lsf.jobExecuteLog_jobId_get
    if _newclass:jobId = property(_lsf.jobExecuteLog_jobId_get, _lsf.jobExecuteLog_jobId_set)
    __swig_setmethods__["execUid"] = _lsf.jobExecuteLog_execUid_set
    __swig_getmethods__["execUid"] = _lsf.jobExecuteLog_execUid_get
    if _newclass:execUid = property(_lsf.jobExecuteLog_execUid_get, _lsf.jobExecuteLog_execUid_set)
    __swig_setmethods__["execHome"] = _lsf.jobExecuteLog_execHome_set
    __swig_getmethods__["execHome"] = _lsf.jobExecuteLog_execHome_get
    if _newclass:execHome = property(_lsf.jobExecuteLog_execHome_get, _lsf.jobExecuteLog_execHome_set)
    __swig_setmethods__["execCwd"] = _lsf.jobExecuteLog_execCwd_set
    __swig_getmethods__["execCwd"] = _lsf.jobExecuteLog_execCwd_get
    if _newclass:execCwd = property(_lsf.jobExecuteLog_execCwd_get, _lsf.jobExecuteLog_execCwd_set)
    __swig_setmethods__["jobPGid"] = _lsf.jobExecuteLog_jobPGid_set
    __swig_getmethods__["jobPGid"] = _lsf.jobExecuteLog_jobPGid_get
    if _newclass:jobPGid = property(_lsf.jobExecuteLog_jobPGid_get, _lsf.jobExecuteLog_jobPGid_set)
    __swig_setmethods__["execUsername"] = _lsf.jobExecuteLog_execUsername_set
    __swig_getmethods__["execUsername"] = _lsf.jobExecuteLog_execUsername_get
    if _newclass:execUsername = property(_lsf.jobExecuteLog_execUsername_get, _lsf.jobExecuteLog_execUsername_set)
    __swig_setmethods__["jobPid"] = _lsf.jobExecuteLog_jobPid_set
    __swig_getmethods__["jobPid"] = _lsf.jobExecuteLog_jobPid_get
    if _newclass:jobPid = property(_lsf.jobExecuteLog_jobPid_get, _lsf.jobExecuteLog_jobPid_set)
    __swig_setmethods__["idx"] = _lsf.jobExecuteLog_idx_set
    __swig_getmethods__["idx"] = _lsf.jobExecuteLog_idx_get
    if _newclass:idx = property(_lsf.jobExecuteLog_idx_get, _lsf.jobExecuteLog_idx_set)
    __swig_setmethods__["additionalInfo"] = _lsf.jobExecuteLog_additionalInfo_set
    __swig_getmethods__["additionalInfo"] = _lsf.jobExecuteLog_additionalInfo_get
    if _newclass:additionalInfo = property(_lsf.jobExecuteLog_additionalInfo_get, _lsf.jobExecuteLog_additionalInfo_set)
    __swig_setmethods__["SLAscaledRunLimit"] = _lsf.jobExecuteLog_SLAscaledRunLimit_set
    __swig_getmethods__["SLAscaledRunLimit"] = _lsf.jobExecuteLog_SLAscaledRunLimit_get
    if _newclass:SLAscaledRunLimit = property(_lsf.jobExecuteLog_SLAscaledRunLimit_get, _lsf.jobExecuteLog_SLAscaledRunLimit_set)
    __swig_setmethods__["position"] = _lsf.jobExecuteLog_position_set
    __swig_getmethods__["position"] = _lsf.jobExecuteLog_position_get
    if _newclass:position = property(_lsf.jobExecuteLog_position_get, _lsf.jobExecuteLog_position_set)
    __swig_setmethods__["execRusage"] = _lsf.jobExecuteLog_execRusage_set
    __swig_getmethods__["execRusage"] = _lsf.jobExecuteLog_execRusage_get
    if _newclass:execRusage = property(_lsf.jobExecuteLog_execRusage_get, _lsf.jobExecuteLog_execRusage_set)
    __swig_setmethods__["duration4PreemptBackfill"] = _lsf.jobExecuteLog_duration4PreemptBackfill_set
    __swig_getmethods__["duration4PreemptBackfill"] = _lsf.jobExecuteLog_duration4PreemptBackfill_get
    if _newclass:duration4PreemptBackfill = property(_lsf.jobExecuteLog_duration4PreemptBackfill_get, _lsf.jobExecuteLog_duration4PreemptBackfill_set)
    def __init__(self, *args): 
        this = _lsf.new_jobExecuteLog(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _lsf.delete_jobExecuteLog
    __del__ = lambda self : None;
jobExecuteLog_swigregister = _lsf.jobExecuteLog_swigregister
jobExecuteLog_swigregister(jobExecuteLog)

class jobStatusLog(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, jobStatusLog, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, jobStatusLog, name)
    __repr__ = _swig_repr
    __swig_setmethods__["jobId"] = _lsf.jobStatusLog_jobId_set
    __swig_getmethods__["jobId"] = _lsf.jobStatusLog_jobId_get
    if _newclass:jobId = property(_lsf.jobStatusLog_jobId_get, _lsf.jobStatusLog_jobId_set)
    __swig_setmethods__["jStatus"] = _lsf.jobStatusLog_jStatus_set
    __swig_getmethods__["jStatus"] = _lsf.jobStatusLog_jStatus_get
    if _newclass:jStatus = property(_lsf.jobStatusLog_jStatus_get, _lsf.jobStatusLog_jStatus_set)
    __swig_setmethods__["reason"] = _lsf.jobStatusLog_reason_set
    __swig_getmethods__["reason"] = _lsf.jobStatusLog_reason_get
    if _newclass:reason = property(_lsf.jobStatusLog_reason_get, _lsf.jobStatusLog_reason_set)
    __swig_setmethods__["subreasons"] = _lsf.jobStatusLog_subreasons_set
    __swig_getmethods__["subreasons"] = _lsf.jobStatusLog_subreasons_get
    if _newclass:subreasons = property(_lsf.jobStatusLog_subreasons_get, _lsf.jobStatusLog_subreasons_set)
    __swig_setmethods__["cpuTime"] = _lsf.jobStatusLog_cpuTime_set
    __swig_getmethods__["cpuTime"] = _lsf.jobStatusLog_cpuTime_get
    if _newclass:cpuTime = property(_lsf.jobStatusLog_cpuTime_get, _lsf.jobStatusLog_cpuTime_set)
    __swig_setmethods__["endTime"] = _lsf.jobStatusLog_endTime_set
    __swig_getmethods__["endTime"] = _lsf.jobStatusLog_endTime_get
    if _newclass:endTime = property(_lsf.jobStatusLog_endTime_get, _lsf.jobStatusLog_endTime_set)
    __swig_setmethods__["ru"] = _lsf.jobStatusLog_ru_set
    __swig_getmethods__["ru"] = _lsf.jobStatusLog_ru_get
    if _newclass:ru = property(_lsf.jobStatusLog_ru_get, _lsf.jobStatusLog_ru_set)
    __swig_setmethods__["lsfRusage"] = _lsf.jobStatusLog_lsfRusage_set
    __swig_getmethods__["lsfRusage"] = _lsf.jobStatusLog_lsfRusage_get
    if _newclass:lsfRusage = property(_lsf.jobStatusLog_lsfRusage_get, _lsf.jobStatusLog_lsfRusage_set)
    __swig_setmethods__["jFlags"] = _lsf.jobStatusLog_jFlags_set
    __swig_getmethods__["jFlags"] = _lsf.jobStatusLog_jFlags_get
    if _newclass:jFlags = property(_lsf.jobStatusLog_jFlags_get, _lsf.jobStatusLog_jFlags_set)
    __swig_setmethods__["exitStatus"] = _lsf.jobStatusLog_exitStatus_set
    __swig_getmethods__["exitStatus"] = _lsf.jobStatusLog_exitStatus_get
    if _newclass:exitStatus = property(_lsf.jobStatusLog_exitStatus_get, _lsf.jobStatusLog_exitStatus_set)
    __swig_setmethods__["idx"] = _lsf.jobStatusLog_idx_set
    __swig_getmethods__["idx"] = _lsf.jobStatusLog_idx_get
    if _newclass:idx = property(_lsf.jobStatusLog_idx_get, _lsf.jobStatusLog_idx_set)
    __swig_setmethods__["exitInfo"] = _lsf.jobStatusLog_exitInfo_set
    __swig_getmethods__["exitInfo"] = _lsf.jobStatusLog_exitInfo_get
    if _newclass:exitInfo = property(_lsf.jobStatusLog_exitInfo_get, _lsf.jobStatusLog_exitInfo_set)
    __swig_setmethods__["numhRusages"] = _lsf.jobStatusLog_numhRusages_set
    __swig_getmethods__["numhRusages"] = _lsf.jobStatusLog_numhRusages_get
    if _newclass:numhRusages = property(_lsf.jobStatusLog_numhRusages_get, _lsf.jobStatusLog_numhRusages_set)
    __swig_setmethods__["hostRusage"] = _lsf.jobStatusLog_hostRusage_set
    __swig_getmethods__["hostRusage"] = _lsf.jobStatusLog_hostRusage_get
    if _newclass:hostRusage = property(_lsf.jobStatusLog_hostRusage_get, _lsf.jobStatusLog_hostRusage_set)
    def __init__(self, *args): 
        this = _lsf.new_jobStatusLog(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _lsf.delete_jobStatusLog
    __del__ = lambda self : None;
jobStatusLog_swigregister = _lsf.jobStatusLog_swigregister
jobStatusLog_swigregister(jobStatusLog)

class sbdJobStatusLog(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, sbdJobStatusLog, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, sbdJobStatusLog, name)
    __repr__ = _swig_repr
    __swig_setmethods__["jobId"] = _lsf.sbdJobStatusLog_jobId_set
    __swig_getmethods__["jobId"] = _lsf.sbdJobStatusLog_jobId_get
    if _newclass:jobId = property(_lsf.sbdJobStatusLog_jobId_get, _lsf.sbdJobStatusLog_jobId_set)
    __swig_setmethods__["jStatus"] = _lsf.sbdJobStatusLog_jStatus_set
    __swig_getmethods__["jStatus"] = _lsf.sbdJobStatusLog_jStatus_get
    if _newclass:jStatus = property(_lsf.sbdJobStatusLog_jStatus_get, _lsf.sbdJobStatusLog_jStatus_set)
    __swig_setmethods__["reasons"] = _lsf.sbdJobStatusLog_reasons_set
    __swig_getmethods__["reasons"] = _lsf.sbdJobStatusLog_reasons_get
    if _newclass:reasons = property(_lsf.sbdJobStatusLog_reasons_get, _lsf.sbdJobStatusLog_reasons_set)
    __swig_setmethods__["subreasons"] = _lsf.sbdJobStatusLog_subreasons_set
    __swig_getmethods__["subreasons"] = _lsf.sbdJobStatusLog_subreasons_get
    if _newclass:subreasons = property(_lsf.sbdJobStatusLog_subreasons_get, _lsf.sbdJobStatusLog_subreasons_set)
    __swig_setmethods__["actPid"] = _lsf.sbdJobStatusLog_actPid_set
    __swig_getmethods__["actPid"] = _lsf.sbdJobStatusLog_actPid_get
    if _newclass:actPid = property(_lsf.sbdJobStatusLog_actPid_get, _lsf.sbdJobStatusLog_actPid_set)
    __swig_setmethods__["actValue"] = _lsf.sbdJobStatusLog_actValue_set
    __swig_getmethods__["actValue"] = _lsf.sbdJobStatusLog_actValue_get
    if _newclass:actValue = property(_lsf.sbdJobStatusLog_actValue_get, _lsf.sbdJobStatusLog_actValue_set)
    __swig_setmethods__["actPeriod"] = _lsf.sbdJobStatusLog_actPeriod_set
    __swig_getmethods__["actPeriod"] = _lsf.sbdJobStatusLog_actPeriod_get
    if _newclass:actPeriod = property(_lsf.sbdJobStatusLog_actPeriod_get, _lsf.sbdJobStatusLog_actPeriod_set)
    __swig_setmethods__["actFlags"] = _lsf.sbdJobStatusLog_actFlags_set
    __swig_getmethods__["actFlags"] = _lsf.sbdJobStatusLog_actFlags_get
    if _newclass:actFlags = property(_lsf.sbdJobStatusLog_actFlags_get, _lsf.sbdJobStatusLog_actFlags_set)
    __swig_setmethods__["actStatus"] = _lsf.sbdJobStatusLog_actStatus_set
    __swig_getmethods__["actStatus"] = _lsf.sbdJobStatusLog_actStatus_get
    if _newclass:actStatus = property(_lsf.sbdJobStatusLog_actStatus_get, _lsf.sbdJobStatusLog_actStatus_set)
    __swig_setmethods__["actReasons"] = _lsf.sbdJobStatusLog_actReasons_set
    __swig_getmethods__["actReasons"] = _lsf.sbdJobStatusLog_actReasons_get
    if _newclass:actReasons = property(_lsf.sbdJobStatusLog_actReasons_get, _lsf.sbdJobStatusLog_actReasons_set)
    __swig_setmethods__["actSubReasons"] = _lsf.sbdJobStatusLog_actSubReasons_set
    __swig_getmethods__["actSubReasons"] = _lsf.sbdJobStatusLog_actSubReasons_get
    if _newclass:actSubReasons = property(_lsf.sbdJobStatusLog_actSubReasons_get, _lsf.sbdJobStatusLog_actSubReasons_set)
    __swig_setmethods__["idx"] = _lsf.sbdJobStatusLog_idx_set
    __swig_getmethods__["idx"] = _lsf.sbdJobStatusLog_idx_get
    if _newclass:idx = property(_lsf.sbdJobStatusLog_idx_get, _lsf.sbdJobStatusLog_idx_set)
    __swig_setmethods__["sigValue"] = _lsf.sbdJobStatusLog_sigValue_set
    __swig_getmethods__["sigValue"] = _lsf.sbdJobStatusLog_sigValue_get
    if _newclass:sigValue = property(_lsf.sbdJobStatusLog_sigValue_get, _lsf.sbdJobStatusLog_sigValue_set)
    __swig_setmethods__["exitInfo"] = _lsf.sbdJobStatusLog_exitInfo_set
    __swig_getmethods__["exitInfo"] = _lsf.sbdJobStatusLog_exitInfo_get
    if _newclass:exitInfo = property(_lsf.sbdJobStatusLog_exitInfo_get, _lsf.sbdJobStatusLog_exitInfo_set)
    __swig_setmethods__["numhRusages"] = _lsf.sbdJobStatusLog_numhRusages_set
    __swig_getmethods__["numhRusages"] = _lsf.sbdJobStatusLog_numhRusages_get
    if _newclass:numhRusages = property(_lsf.sbdJobStatusLog_numhRusages_get, _lsf.sbdJobStatusLog_numhRusages_set)
    __swig_setmethods__["hostRusage"] = _lsf.sbdJobStatusLog_hostRusage_set
    __swig_getmethods__["hostRusage"] = _lsf.sbdJobStatusLog_hostRusage_get
    if _newclass:hostRusage = property(_lsf.sbdJobStatusLog_hostRusage_get, _lsf.sbdJobStatusLog_hostRusage_set)
    def __init__(self, *args): 
        this = _lsf.new_sbdJobStatusLog(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _lsf.delete_sbdJobStatusLog
    __del__ = lambda self : None;
sbdJobStatusLog_swigregister = _lsf.sbdJobStatusLog_swigregister
sbdJobStatusLog_swigregister(sbdJobStatusLog)

class sbdUnreportedStatusLog(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, sbdUnreportedStatusLog, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, sbdUnreportedStatusLog, name)
    __repr__ = _swig_repr
    __swig_setmethods__["jobId"] = _lsf.sbdUnreportedStatusLog_jobId_set
    __swig_getmethods__["jobId"] = _lsf.sbdUnreportedStatusLog_jobId_get
    if _newclass:jobId = property(_lsf.sbdUnreportedStatusLog_jobId_get, _lsf.sbdUnreportedStatusLog_jobId_set)
    __swig_setmethods__["actPid"] = _lsf.sbdUnreportedStatusLog_actPid_set
    __swig_getmethods__["actPid"] = _lsf.sbdUnreportedStatusLog_actPid_get
    if _newclass:actPid = property(_lsf.sbdUnreportedStatusLog_actPid_get, _lsf.sbdUnreportedStatusLog_actPid_set)
    __swig_setmethods__["jobPid"] = _lsf.sbdUnreportedStatusLog_jobPid_set
    __swig_getmethods__["jobPid"] = _lsf.sbdUnreportedStatusLog_jobPid_get
    if _newclass:jobPid = property(_lsf.sbdUnreportedStatusLog_jobPid_get, _lsf.sbdUnreportedStatusLog_jobPid_set)
    __swig_setmethods__["jobPGid"] = _lsf.sbdUnreportedStatusLog_jobPGid_set
    __swig_getmethods__["jobPGid"] = _lsf.sbdUnreportedStatusLog_jobPGid_get
    if _newclass:jobPGid = property(_lsf.sbdUnreportedStatusLog_jobPGid_get, _lsf.sbdUnreportedStatusLog_jobPGid_set)
    __swig_setmethods__["newStatus"] = _lsf.sbdUnreportedStatusLog_newStatus_set
    __swig_getmethods__["newStatus"] = _lsf.sbdUnreportedStatusLog_newStatus_get
    if _newclass:newStatus = property(_lsf.sbdUnreportedStatusLog_newStatus_get, _lsf.sbdUnreportedStatusLog_newStatus_set)
    __swig_setmethods__["reason"] = _lsf.sbdUnreportedStatusLog_reason_set
    __swig_getmethods__["reason"] = _lsf.sbdUnreportedStatusLog_reason_get
    if _newclass:reason = property(_lsf.sbdUnreportedStatusLog_reason_get, _lsf.sbdUnreportedStatusLog_reason_set)
    __swig_setmethods__["subreasons"] = _lsf.sbdUnreportedStatusLog_subreasons_set
    __swig_getmethods__["subreasons"] = _lsf.sbdUnreportedStatusLog_subreasons_get
    if _newclass:subreasons = property(_lsf.sbdUnreportedStatusLog_subreasons_get, _lsf.sbdUnreportedStatusLog_subreasons_set)
    __swig_setmethods__["lsfRusage"] = _lsf.sbdUnreportedStatusLog_lsfRusage_set
    __swig_getmethods__["lsfRusage"] = _lsf.sbdUnreportedStatusLog_lsfRusage_get
    if _newclass:lsfRusage = property(_lsf.sbdUnreportedStatusLog_lsfRusage_get, _lsf.sbdUnreportedStatusLog_lsfRusage_set)
    __swig_setmethods__["execUid"] = _lsf.sbdUnreportedStatusLog_execUid_set
    __swig_getmethods__["execUid"] = _lsf.sbdUnreportedStatusLog_execUid_get
    if _newclass:execUid = property(_lsf.sbdUnreportedStatusLog_execUid_get, _lsf.sbdUnreportedStatusLog_execUid_set)
    __swig_setmethods__["exitStatus"] = _lsf.sbdUnreportedStatusLog_exitStatus_set
    __swig_getmethods__["exitStatus"] = _lsf.sbdUnreportedStatusLog_exitStatus_get
    if _newclass:exitStatus = property(_lsf.sbdUnreportedStatusLog_exitStatus_get, _lsf.sbdUnreportedStatusLog_exitStatus_set)
    __swig_setmethods__["execCwd"] = _lsf.sbdUnreportedStatusLog_execCwd_set
    __swig_getmethods__["execCwd"] = _lsf.sbdUnreportedStatusLog_execCwd_get
    if _newclass:execCwd = property(_lsf.sbdUnreportedStatusLog_execCwd_get, _lsf.sbdUnreportedStatusLog_execCwd_set)
    __swig_setmethods__["execHome"] = _lsf.sbdUnreportedStatusLog_execHome_set
    __swig_getmethods__["execHome"] = _lsf.sbdUnreportedStatusLog_execHome_get
    if _newclass:execHome = property(_lsf.sbdUnreportedStatusLog_execHome_get, _lsf.sbdUnreportedStatusLog_execHome_set)
    __swig_setmethods__["execUsername"] = _lsf.sbdUnreportedStatusLog_execUsername_set
    __swig_getmethods__["execUsername"] = _lsf.sbdUnreportedStatusLog_execUsername_get
    if _newclass:execUsername = property(_lsf.sbdUnreportedStatusLog_execUsername_get, _lsf.sbdUnreportedStatusLog_execUsername_set)
    __swig_setmethods__["msgId"] = _lsf.sbdUnreportedStatusLog_msgId_set
    __swig_getmethods__["msgId"] = _lsf.sbdUnreportedStatusLog_msgId_get
    if _newclass:msgId = property(_lsf.sbdUnreportedStatusLog_msgId_get, _lsf.sbdUnreportedStatusLog_msgId_set)
    __swig_setmethods__["runRusage"] = _lsf.sbdUnreportedStatusLog_runRusage_set
    __swig_getmethods__["runRusage"] = _lsf.sbdUnreportedStatusLog_runRusage_get
    if _newclass:runRusage = property(_lsf.sbdUnreportedStatusLog_runRusage_get, _lsf.sbdUnreportedStatusLog_runRusage_set)
    __swig_setmethods__["sigValue"] = _lsf.sbdUnreportedStatusLog_sigValue_set
    __swig_getmethods__["sigValue"] = _lsf.sbdUnreportedStatusLog_sigValue_get
    if _newclass:sigValue = property(_lsf.sbdUnreportedStatusLog_sigValue_get, _lsf.sbdUnreportedStatusLog_sigValue_set)
    __swig_setmethods__["actStatus"] = _lsf.sbdUnreportedStatusLog_actStatus_set
    __swig_getmethods__["actStatus"] = _lsf.sbdUnreportedStatusLog_actStatus_get
    if _newclass:actStatus = property(_lsf.sbdUnreportedStatusLog_actStatus_get, _lsf.sbdUnreportedStatusLog_actStatus_set)
    __swig_setmethods__["seq"] = _lsf.sbdUnreportedStatusLog_seq_set
    __swig_getmethods__["seq"] = _lsf.sbdUnreportedStatusLog_seq_get
    if _newclass:seq = property(_lsf.sbdUnreportedStatusLog_seq_get, _lsf.sbdUnreportedStatusLog_seq_set)
    __swig_setmethods__["idx"] = _lsf.sbdUnreportedStatusLog_idx_set
    __swig_getmethods__["idx"] = _lsf.sbdUnreportedStatusLog_idx_get
    if _newclass:idx = property(_lsf.sbdUnreportedStatusLog_idx_get, _lsf.sbdUnreportedStatusLog_idx_set)
    __swig_setmethods__["exitInfo"] = _lsf.sbdUnreportedStatusLog_exitInfo_set
    __swig_getmethods__["exitInfo"] = _lsf.sbdUnreportedStatusLog_exitInfo_get
    if _newclass:exitInfo = property(_lsf.sbdUnreportedStatusLog_exitInfo_get, _lsf.sbdUnreportedStatusLog_exitInfo_set)
    __swig_setmethods__["numhRusages"] = _lsf.sbdUnreportedStatusLog_numhRusages_set
    __swig_getmethods__["numhRusages"] = _lsf.sbdUnreportedStatusLog_numhRusages_get
    if _newclass:numhRusages = property(_lsf.sbdUnreportedStatusLog_numhRusages_get, _lsf.sbdUnreportedStatusLog_numhRusages_set)
    __swig_setmethods__["hostRusage"] = _lsf.sbdUnreportedStatusLog_hostRusage_set
    __swig_getmethods__["hostRusage"] = _lsf.sbdUnreportedStatusLog_hostRusage_get
    if _newclass:hostRusage = property(_lsf.sbdUnreportedStatusLog_hostRusage_get, _lsf.sbdUnreportedStatusLog_hostRusage_set)
    def __init__(self, *args): 
        this = _lsf.new_sbdUnreportedStatusLog(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _lsf.delete_sbdUnreportedStatusLog
    __del__ = lambda self : None;
sbdUnreportedStatusLog_swigregister = _lsf.sbdUnreportedStatusLog_swigregister
sbdUnreportedStatusLog_swigregister(sbdUnreportedStatusLog)

class jobSwitchLog(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, jobSwitchLog, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, jobSwitchLog, name)
    __repr__ = _swig_repr
    __swig_setmethods__["userId"] = _lsf.jobSwitchLog_userId_set
    __swig_getmethods__["userId"] = _lsf.jobSwitchLog_userId_get
    if _newclass:userId = property(_lsf.jobSwitchLog_userId_get, _lsf.jobSwitchLog_userId_set)
    __swig_setmethods__["jobId"] = _lsf.jobSwitchLog_jobId_set
    __swig_getmethods__["jobId"] = _lsf.jobSwitchLog_jobId_get
    if _newclass:jobId = property(_lsf.jobSwitchLog_jobId_get, _lsf.jobSwitchLog_jobId_set)
    __swig_setmethods__["queue"] = _lsf.jobSwitchLog_queue_set
    __swig_getmethods__["queue"] = _lsf.jobSwitchLog_queue_get
    if _newclass:queue = property(_lsf.jobSwitchLog_queue_get, _lsf.jobSwitchLog_queue_set)
    __swig_setmethods__["idx"] = _lsf.jobSwitchLog_idx_set
    __swig_getmethods__["idx"] = _lsf.jobSwitchLog_idx_get
    if _newclass:idx = property(_lsf.jobSwitchLog_idx_get, _lsf.jobSwitchLog_idx_set)
    __swig_setmethods__["userName"] = _lsf.jobSwitchLog_userName_set
    __swig_getmethods__["userName"] = _lsf.jobSwitchLog_userName_get
    if _newclass:userName = property(_lsf.jobSwitchLog_userName_get, _lsf.jobSwitchLog_userName_set)
    def __init__(self, *args): 
        this = _lsf.new_jobSwitchLog(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _lsf.delete_jobSwitchLog
    __del__ = lambda self : None;
jobSwitchLog_swigregister = _lsf.jobSwitchLog_swigregister
jobSwitchLog_swigregister(jobSwitchLog)

class jobMoveLog(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, jobMoveLog, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, jobMoveLog, name)
    __repr__ = _swig_repr
    __swig_setmethods__["userId"] = _lsf.jobMoveLog_userId_set
    __swig_getmethods__["userId"] = _lsf.jobMoveLog_userId_get
    if _newclass:userId = property(_lsf.jobMoveLog_userId_get, _lsf.jobMoveLog_userId_set)
    __swig_setmethods__["jobId"] = _lsf.jobMoveLog_jobId_set
    __swig_getmethods__["jobId"] = _lsf.jobMoveLog_jobId_get
    if _newclass:jobId = property(_lsf.jobMoveLog_jobId_get, _lsf.jobMoveLog_jobId_set)
    __swig_setmethods__["position"] = _lsf.jobMoveLog_position_set
    __swig_getmethods__["position"] = _lsf.jobMoveLog_position_get
    if _newclass:position = property(_lsf.jobMoveLog_position_get, _lsf.jobMoveLog_position_set)
    __swig_setmethods__["base"] = _lsf.jobMoveLog_base_set
    __swig_getmethods__["base"] = _lsf.jobMoveLog_base_get
    if _newclass:base = property(_lsf.jobMoveLog_base_get, _lsf.jobMoveLog_base_set)
    __swig_setmethods__["idx"] = _lsf.jobMoveLog_idx_set
    __swig_getmethods__["idx"] = _lsf.jobMoveLog_idx_get
    if _newclass:idx = property(_lsf.jobMoveLog_idx_get, _lsf.jobMoveLog_idx_set)
    __swig_setmethods__["userName"] = _lsf.jobMoveLog_userName_set
    __swig_getmethods__["userName"] = _lsf.jobMoveLog_userName_get
    if _newclass:userName = property(_lsf.jobMoveLog_userName_get, _lsf.jobMoveLog_userName_set)
    def __init__(self, *args): 
        this = _lsf.new_jobMoveLog(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _lsf.delete_jobMoveLog
    __del__ = lambda self : None;
jobMoveLog_swigregister = _lsf.jobMoveLog_swigregister
jobMoveLog_swigregister(jobMoveLog)

class chkpntLog(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, chkpntLog, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, chkpntLog, name)
    __repr__ = _swig_repr
    __swig_setmethods__["jobId"] = _lsf.chkpntLog_jobId_set
    __swig_getmethods__["jobId"] = _lsf.chkpntLog_jobId_get
    if _newclass:jobId = property(_lsf.chkpntLog_jobId_get, _lsf.chkpntLog_jobId_set)
    __swig_setmethods__["period"] = _lsf.chkpntLog_period_set
    __swig_getmethods__["period"] = _lsf.chkpntLog_period_get
    if _newclass:period = property(_lsf.chkpntLog_period_get, _lsf.chkpntLog_period_set)
    __swig_setmethods__["pid"] = _lsf.chkpntLog_pid_set
    __swig_getmethods__["pid"] = _lsf.chkpntLog_pid_get
    if _newclass:pid = property(_lsf.chkpntLog_pid_get, _lsf.chkpntLog_pid_set)
    __swig_setmethods__["ok"] = _lsf.chkpntLog_ok_set
    __swig_getmethods__["ok"] = _lsf.chkpntLog_ok_get
    if _newclass:ok = property(_lsf.chkpntLog_ok_get, _lsf.chkpntLog_ok_set)
    __swig_setmethods__["flags"] = _lsf.chkpntLog_flags_set
    __swig_getmethods__["flags"] = _lsf.chkpntLog_flags_get
    if _newclass:flags = property(_lsf.chkpntLog_flags_get, _lsf.chkpntLog_flags_set)
    __swig_setmethods__["idx"] = _lsf.chkpntLog_idx_set
    __swig_getmethods__["idx"] = _lsf.chkpntLog_idx_get
    if _newclass:idx = property(_lsf.chkpntLog_idx_get, _lsf.chkpntLog_idx_set)
    def __init__(self, *args): 
        this = _lsf.new_chkpntLog(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _lsf.delete_chkpntLog
    __del__ = lambda self : None;
chkpntLog_swigregister = _lsf.chkpntLog_swigregister
chkpntLog_swigregister(chkpntLog)

class jobRequeueLog(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, jobRequeueLog, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, jobRequeueLog, name)
    __repr__ = _swig_repr
    __swig_setmethods__["jobId"] = _lsf.jobRequeueLog_jobId_set
    __swig_getmethods__["jobId"] = _lsf.jobRequeueLog_jobId_get
    if _newclass:jobId = property(_lsf.jobRequeueLog_jobId_get, _lsf.jobRequeueLog_jobId_set)
    __swig_setmethods__["idx"] = _lsf.jobRequeueLog_idx_set
    __swig_getmethods__["idx"] = _lsf.jobRequeueLog_idx_get
    if _newclass:idx = property(_lsf.jobRequeueLog_idx_get, _lsf.jobRequeueLog_idx_set)
    def __init__(self, *args): 
        this = _lsf.new_jobRequeueLog(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _lsf.delete_jobRequeueLog
    __del__ = lambda self : None;
jobRequeueLog_swigregister = _lsf.jobRequeueLog_swigregister
jobRequeueLog_swigregister(jobRequeueLog)

class jobCleanLog(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, jobCleanLog, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, jobCleanLog, name)
    __repr__ = _swig_repr
    __swig_setmethods__["jobId"] = _lsf.jobCleanLog_jobId_set
    __swig_getmethods__["jobId"] = _lsf.jobCleanLog_jobId_get
    if _newclass:jobId = property(_lsf.jobCleanLog_jobId_get, _lsf.jobCleanLog_jobId_set)
    __swig_setmethods__["idx"] = _lsf.jobCleanLog_idx_set
    __swig_getmethods__["idx"] = _lsf.jobCleanLog_idx_get
    if _newclass:idx = property(_lsf.jobCleanLog_idx_get, _lsf.jobCleanLog_idx_set)
    def __init__(self, *args): 
        this = _lsf.new_jobCleanLog(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _lsf.delete_jobCleanLog
    __del__ = lambda self : None;
jobCleanLog_swigregister = _lsf.jobCleanLog_swigregister
jobCleanLog_swigregister(jobCleanLog)

class jobExceptionLog(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, jobExceptionLog, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, jobExceptionLog, name)
    __repr__ = _swig_repr
    __swig_setmethods__["jobId"] = _lsf.jobExceptionLog_jobId_set
    __swig_getmethods__["jobId"] = _lsf.jobExceptionLog_jobId_get
    if _newclass:jobId = property(_lsf.jobExceptionLog_jobId_get, _lsf.jobExceptionLog_jobId_set)
    __swig_setmethods__["exceptMask"] = _lsf.jobExceptionLog_exceptMask_set
    __swig_getmethods__["exceptMask"] = _lsf.jobExceptionLog_exceptMask_get
    if _newclass:exceptMask = property(_lsf.jobExceptionLog_exceptMask_get, _lsf.jobExceptionLog_exceptMask_set)
    __swig_setmethods__["actMask"] = _lsf.jobExceptionLog_actMask_set
    __swig_getmethods__["actMask"] = _lsf.jobExceptionLog_actMask_get
    if _newclass:actMask = property(_lsf.jobExceptionLog_actMask_get, _lsf.jobExceptionLog_actMask_set)
    __swig_setmethods__["timeEvent"] = _lsf.jobExceptionLog_timeEvent_set
    __swig_getmethods__["timeEvent"] = _lsf.jobExceptionLog_timeEvent_get
    if _newclass:timeEvent = property(_lsf.jobExceptionLog_timeEvent_get, _lsf.jobExceptionLog_timeEvent_set)
    __swig_setmethods__["exceptInfo"] = _lsf.jobExceptionLog_exceptInfo_set
    __swig_getmethods__["exceptInfo"] = _lsf.jobExceptionLog_exceptInfo_get
    if _newclass:exceptInfo = property(_lsf.jobExceptionLog_exceptInfo_get, _lsf.jobExceptionLog_exceptInfo_set)
    __swig_setmethods__["idx"] = _lsf.jobExceptionLog_idx_set
    __swig_getmethods__["idx"] = _lsf.jobExceptionLog_idx_get
    if _newclass:idx = property(_lsf.jobExceptionLog_idx_get, _lsf.jobExceptionLog_idx_set)
    def __init__(self, *args): 
        this = _lsf.new_jobExceptionLog(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _lsf.delete_jobExceptionLog
    __del__ = lambda self : None;
jobExceptionLog_swigregister = _lsf.jobExceptionLog_swigregister
jobExceptionLog_swigregister(jobExceptionLog)

class sigactLog(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, sigactLog, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, sigactLog, name)
    __repr__ = _swig_repr
    __swig_setmethods__["jobId"] = _lsf.sigactLog_jobId_set
    __swig_getmethods__["jobId"] = _lsf.sigactLog_jobId_get
    if _newclass:jobId = property(_lsf.sigactLog_jobId_get, _lsf.sigactLog_jobId_set)
    __swig_setmethods__["period"] = _lsf.sigactLog_period_set
    __swig_getmethods__["period"] = _lsf.sigactLog_period_get
    if _newclass:period = property(_lsf.sigactLog_period_get, _lsf.sigactLog_period_set)
    __swig_setmethods__["pid"] = _lsf.sigactLog_pid_set
    __swig_getmethods__["pid"] = _lsf.sigactLog_pid_get
    if _newclass:pid = property(_lsf.sigactLog_pid_get, _lsf.sigactLog_pid_set)
    __swig_setmethods__["jStatus"] = _lsf.sigactLog_jStatus_set
    __swig_getmethods__["jStatus"] = _lsf.sigactLog_jStatus_get
    if _newclass:jStatus = property(_lsf.sigactLog_jStatus_get, _lsf.sigactLog_jStatus_set)
    __swig_setmethods__["reasons"] = _lsf.sigactLog_reasons_set
    __swig_getmethods__["reasons"] = _lsf.sigactLog_reasons_get
    if _newclass:reasons = property(_lsf.sigactLog_reasons_get, _lsf.sigactLog_reasons_set)
    __swig_setmethods__["flags"] = _lsf.sigactLog_flags_set
    __swig_getmethods__["flags"] = _lsf.sigactLog_flags_get
    if _newclass:flags = property(_lsf.sigactLog_flags_get, _lsf.sigactLog_flags_set)
    __swig_setmethods__["signalSymbol"] = _lsf.sigactLog_signalSymbol_set
    __swig_getmethods__["signalSymbol"] = _lsf.sigactLog_signalSymbol_get
    if _newclass:signalSymbol = property(_lsf.sigactLog_signalSymbol_get, _lsf.sigactLog_signalSymbol_set)
    __swig_setmethods__["actStatus"] = _lsf.sigactLog_actStatus_set
    __swig_getmethods__["actStatus"] = _lsf.sigactLog_actStatus_get
    if _newclass:actStatus = property(_lsf.sigactLog_actStatus_get, _lsf.sigactLog_actStatus_set)
    __swig_setmethods__["idx"] = _lsf.sigactLog_idx_set
    __swig_getmethods__["idx"] = _lsf.sigactLog_idx_get
    if _newclass:idx = property(_lsf.sigactLog_idx_get, _lsf.sigactLog_idx_set)
    def __init__(self, *args): 
        this = _lsf.new_sigactLog(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _lsf.delete_sigactLog
    __del__ = lambda self : None;
sigactLog_swigregister = _lsf.sigactLog_swigregister
sigactLog_swigregister(sigactLog)

class migLog(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, migLog, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, migLog, name)
    __repr__ = _swig_repr
    __swig_setmethods__["jobId"] = _lsf.migLog_jobId_set
    __swig_getmethods__["jobId"] = _lsf.migLog_jobId_get
    if _newclass:jobId = property(_lsf.migLog_jobId_get, _lsf.migLog_jobId_set)
    __swig_setmethods__["numAskedHosts"] = _lsf.migLog_numAskedHosts_set
    __swig_getmethods__["numAskedHosts"] = _lsf.migLog_numAskedHosts_get
    if _newclass:numAskedHosts = property(_lsf.migLog_numAskedHosts_get, _lsf.migLog_numAskedHosts_set)
    __swig_setmethods__["askedHosts"] = _lsf.migLog_askedHosts_set
    __swig_getmethods__["askedHosts"] = _lsf.migLog_askedHosts_get
    if _newclass:askedHosts = property(_lsf.migLog_askedHosts_get, _lsf.migLog_askedHosts_set)
    __swig_setmethods__["userId"] = _lsf.migLog_userId_set
    __swig_getmethods__["userId"] = _lsf.migLog_userId_get
    if _newclass:userId = property(_lsf.migLog_userId_get, _lsf.migLog_userId_set)
    __swig_setmethods__["idx"] = _lsf.migLog_idx_set
    __swig_getmethods__["idx"] = _lsf.migLog_idx_get
    if _newclass:idx = property(_lsf.migLog_idx_get, _lsf.migLog_idx_set)
    __swig_setmethods__["userName"] = _lsf.migLog_userName_set
    __swig_getmethods__["userName"] = _lsf.migLog_userName_get
    if _newclass:userName = property(_lsf.migLog_userName_get, _lsf.migLog_userName_set)
    def __init__(self, *args): 
        this = _lsf.new_migLog(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _lsf.delete_migLog
    __del__ = lambda self : None;
migLog_swigregister = _lsf.migLog_swigregister
migLog_swigregister(migLog)

class signalLog(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, signalLog, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, signalLog, name)
    __repr__ = _swig_repr
    __swig_setmethods__["userId"] = _lsf.signalLog_userId_set
    __swig_getmethods__["userId"] = _lsf.signalLog_userId_get
    if _newclass:userId = property(_lsf.signalLog_userId_get, _lsf.signalLog_userId_set)
    __swig_setmethods__["jobId"] = _lsf.signalLog_jobId_set
    __swig_getmethods__["jobId"] = _lsf.signalLog_jobId_get
    if _newclass:jobId = property(_lsf.signalLog_jobId_get, _lsf.signalLog_jobId_set)
    __swig_setmethods__["signalSymbol"] = _lsf.signalLog_signalSymbol_set
    __swig_getmethods__["signalSymbol"] = _lsf.signalLog_signalSymbol_get
    if _newclass:signalSymbol = property(_lsf.signalLog_signalSymbol_get, _lsf.signalLog_signalSymbol_set)
    __swig_setmethods__["runCount"] = _lsf.signalLog_runCount_set
    __swig_getmethods__["runCount"] = _lsf.signalLog_runCount_get
    if _newclass:runCount = property(_lsf.signalLog_runCount_get, _lsf.signalLog_runCount_set)
    __swig_setmethods__["idx"] = _lsf.signalLog_idx_set
    __swig_getmethods__["idx"] = _lsf.signalLog_idx_get
    if _newclass:idx = property(_lsf.signalLog_idx_get, _lsf.signalLog_idx_set)
    __swig_setmethods__["userName"] = _lsf.signalLog_userName_set
    __swig_getmethods__["userName"] = _lsf.signalLog_userName_get
    if _newclass:userName = property(_lsf.signalLog_userName_get, _lsf.signalLog_userName_set)
    def __init__(self, *args): 
        this = _lsf.new_signalLog(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _lsf.delete_signalLog
    __del__ = lambda self : None;
signalLog_swigregister = _lsf.signalLog_swigregister
signalLog_swigregister(signalLog)

class queueCtrlLog(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, queueCtrlLog, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, queueCtrlLog, name)
    __repr__ = _swig_repr
    __swig_setmethods__["opCode"] = _lsf.queueCtrlLog_opCode_set
    __swig_getmethods__["opCode"] = _lsf.queueCtrlLog_opCode_get
    if _newclass:opCode = property(_lsf.queueCtrlLog_opCode_get, _lsf.queueCtrlLog_opCode_set)
    __swig_setmethods__["queue"] = _lsf.queueCtrlLog_queue_set
    __swig_getmethods__["queue"] = _lsf.queueCtrlLog_queue_get
    if _newclass:queue = property(_lsf.queueCtrlLog_queue_get, _lsf.queueCtrlLog_queue_set)
    __swig_setmethods__["userId"] = _lsf.queueCtrlLog_userId_set
    __swig_getmethods__["userId"] = _lsf.queueCtrlLog_userId_get
    if _newclass:userId = property(_lsf.queueCtrlLog_userId_get, _lsf.queueCtrlLog_userId_set)
    __swig_setmethods__["userName"] = _lsf.queueCtrlLog_userName_set
    __swig_getmethods__["userName"] = _lsf.queueCtrlLog_userName_get
    if _newclass:userName = property(_lsf.queueCtrlLog_userName_get, _lsf.queueCtrlLog_userName_set)
    __swig_setmethods__["message"] = _lsf.queueCtrlLog_message_set
    __swig_getmethods__["message"] = _lsf.queueCtrlLog_message_get
    if _newclass:message = property(_lsf.queueCtrlLog_message_get, _lsf.queueCtrlLog_message_set)
    def __init__(self, *args): 
        this = _lsf.new_queueCtrlLog(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _lsf.delete_queueCtrlLog
    __del__ = lambda self : None;
queueCtrlLog_swigregister = _lsf.queueCtrlLog_swigregister
queueCtrlLog_swigregister(queueCtrlLog)

class newDebugLog(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, newDebugLog, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, newDebugLog, name)
    __repr__ = _swig_repr
    __swig_setmethods__["opCode"] = _lsf.newDebugLog_opCode_set
    __swig_getmethods__["opCode"] = _lsf.newDebugLog_opCode_get
    if _newclass:opCode = property(_lsf.newDebugLog_opCode_get, _lsf.newDebugLog_opCode_set)
    __swig_setmethods__["level"] = _lsf.newDebugLog_level_set
    __swig_getmethods__["level"] = _lsf.newDebugLog_level_get
    if _newclass:level = property(_lsf.newDebugLog_level_get, _lsf.newDebugLog_level_set)
    __swig_setmethods__["_logclass"] = _lsf.newDebugLog__logclass_set
    __swig_getmethods__["_logclass"] = _lsf.newDebugLog__logclass_get
    if _newclass:_logclass = property(_lsf.newDebugLog__logclass_get, _lsf.newDebugLog__logclass_set)
    __swig_setmethods__["turnOff"] = _lsf.newDebugLog_turnOff_set
    __swig_getmethods__["turnOff"] = _lsf.newDebugLog_turnOff_get
    if _newclass:turnOff = property(_lsf.newDebugLog_turnOff_get, _lsf.newDebugLog_turnOff_set)
    __swig_setmethods__["logFileName"] = _lsf.newDebugLog_logFileName_set
    __swig_getmethods__["logFileName"] = _lsf.newDebugLog_logFileName_get
    if _newclass:logFileName = property(_lsf.newDebugLog_logFileName_get, _lsf.newDebugLog_logFileName_set)
    __swig_setmethods__["userId"] = _lsf.newDebugLog_userId_set
    __swig_getmethods__["userId"] = _lsf.newDebugLog_userId_get
    if _newclass:userId = property(_lsf.newDebugLog_userId_get, _lsf.newDebugLog_userId_set)
    def __init__(self, *args): 
        this = _lsf.new_newDebugLog(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _lsf.delete_newDebugLog
    __del__ = lambda self : None;
newDebugLog_swigregister = _lsf.newDebugLog_swigregister
newDebugLog_swigregister(newDebugLog)

class hostCtrlLog(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, hostCtrlLog, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, hostCtrlLog, name)
    __repr__ = _swig_repr
    __swig_setmethods__["opCode"] = _lsf.hostCtrlLog_opCode_set
    __swig_getmethods__["opCode"] = _lsf.hostCtrlLog_opCode_get
    if _newclass:opCode = property(_lsf.hostCtrlLog_opCode_get, _lsf.hostCtrlLog_opCode_set)
    __swig_setmethods__["host"] = _lsf.hostCtrlLog_host_set
    __swig_getmethods__["host"] = _lsf.hostCtrlLog_host_get
    if _newclass:host = property(_lsf.hostCtrlLog_host_get, _lsf.hostCtrlLog_host_set)
    __swig_setmethods__["userId"] = _lsf.hostCtrlLog_userId_set
    __swig_getmethods__["userId"] = _lsf.hostCtrlLog_userId_get
    if _newclass:userId = property(_lsf.hostCtrlLog_userId_get, _lsf.hostCtrlLog_userId_set)
    __swig_setmethods__["userName"] = _lsf.hostCtrlLog_userName_set
    __swig_getmethods__["userName"] = _lsf.hostCtrlLog_userName_get
    if _newclass:userName = property(_lsf.hostCtrlLog_userName_get, _lsf.hostCtrlLog_userName_set)
    __swig_setmethods__["message"] = _lsf.hostCtrlLog_message_set
    __swig_getmethods__["message"] = _lsf.hostCtrlLog_message_get
    if _newclass:message = property(_lsf.hostCtrlLog_message_get, _lsf.hostCtrlLog_message_set)
    def __init__(self, *args): 
        this = _lsf.new_hostCtrlLog(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _lsf.delete_hostCtrlLog
    __del__ = lambda self : None;
hostCtrlLog_swigregister = _lsf.hostCtrlLog_swigregister
hostCtrlLog_swigregister(hostCtrlLog)

class hgCtrlLog(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, hgCtrlLog, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, hgCtrlLog, name)
    __repr__ = _swig_repr
    __swig_setmethods__["opCode"] = _lsf.hgCtrlLog_opCode_set
    __swig_getmethods__["opCode"] = _lsf.hgCtrlLog_opCode_get
    if _newclass:opCode = property(_lsf.hgCtrlLog_opCode_get, _lsf.hgCtrlLog_opCode_set)
    __swig_setmethods__["host"] = _lsf.hgCtrlLog_host_set
    __swig_getmethods__["host"] = _lsf.hgCtrlLog_host_get
    if _newclass:host = property(_lsf.hgCtrlLog_host_get, _lsf.hgCtrlLog_host_set)
    __swig_setmethods__["grpname"] = _lsf.hgCtrlLog_grpname_set
    __swig_getmethods__["grpname"] = _lsf.hgCtrlLog_grpname_get
    if _newclass:grpname = property(_lsf.hgCtrlLog_grpname_get, _lsf.hgCtrlLog_grpname_set)
    __swig_setmethods__["userId"] = _lsf.hgCtrlLog_userId_set
    __swig_getmethods__["userId"] = _lsf.hgCtrlLog_userId_get
    if _newclass:userId = property(_lsf.hgCtrlLog_userId_get, _lsf.hgCtrlLog_userId_set)
    __swig_setmethods__["userName"] = _lsf.hgCtrlLog_userName_set
    __swig_getmethods__["userName"] = _lsf.hgCtrlLog_userName_get
    if _newclass:userName = property(_lsf.hgCtrlLog_userName_get, _lsf.hgCtrlLog_userName_set)
    __swig_setmethods__["message"] = _lsf.hgCtrlLog_message_set
    __swig_getmethods__["message"] = _lsf.hgCtrlLog_message_get
    if _newclass:message = property(_lsf.hgCtrlLog_message_get, _lsf.hgCtrlLog_message_set)
    def __init__(self, *args): 
        this = _lsf.new_hgCtrlLog(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _lsf.delete_hgCtrlLog
    __del__ = lambda self : None;
hgCtrlLog_swigregister = _lsf.hgCtrlLog_swigregister
hgCtrlLog_swigregister(hgCtrlLog)

SIMU_STATUS_READYSCHEDULE = _lsf.SIMU_STATUS_READYSCHEDULE
class mbdStartLog(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, mbdStartLog, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, mbdStartLog, name)
    __repr__ = _swig_repr
    __swig_setmethods__["master"] = _lsf.mbdStartLog_master_set
    __swig_getmethods__["master"] = _lsf.mbdStartLog_master_get
    if _newclass:master = property(_lsf.mbdStartLog_master_get, _lsf.mbdStartLog_master_set)
    __swig_setmethods__["cluster"] = _lsf.mbdStartLog_cluster_set
    __swig_getmethods__["cluster"] = _lsf.mbdStartLog_cluster_get
    if _newclass:cluster = property(_lsf.mbdStartLog_cluster_get, _lsf.mbdStartLog_cluster_set)
    __swig_setmethods__["numHosts"] = _lsf.mbdStartLog_numHosts_set
    __swig_getmethods__["numHosts"] = _lsf.mbdStartLog_numHosts_get
    if _newclass:numHosts = property(_lsf.mbdStartLog_numHosts_get, _lsf.mbdStartLog_numHosts_set)
    __swig_setmethods__["numQueues"] = _lsf.mbdStartLog_numQueues_set
    __swig_getmethods__["numQueues"] = _lsf.mbdStartLog_numQueues_get
    if _newclass:numQueues = property(_lsf.mbdStartLog_numQueues_get, _lsf.mbdStartLog_numQueues_set)
    def __init__(self, *args): 
        this = _lsf.new_mbdStartLog(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _lsf.delete_mbdStartLog
    __del__ = lambda self : None;
mbdStartLog_swigregister = _lsf.mbdStartLog_swigregister
mbdStartLog_swigregister(mbdStartLog)

class mbdSimStatusLog(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, mbdSimStatusLog, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, mbdSimStatusLog, name)
    __repr__ = _swig_repr
    __swig_setmethods__["simStatus"] = _lsf.mbdSimStatusLog_simStatus_set
    __swig_getmethods__["simStatus"] = _lsf.mbdSimStatusLog_simStatus_get
    if _newclass:simStatus = property(_lsf.mbdSimStatusLog_simStatus_get, _lsf.mbdSimStatusLog_simStatus_set)
    def __init__(self, *args): 
        this = _lsf.new_mbdSimStatusLog(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _lsf.delete_mbdSimStatusLog
    __del__ = lambda self : None;
mbdSimStatusLog_swigregister = _lsf.mbdSimStatusLog_swigregister
mbdSimStatusLog_swigregister(mbdSimStatusLog)

class mbdDieLog(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, mbdDieLog, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, mbdDieLog, name)
    __repr__ = _swig_repr
    __swig_setmethods__["master"] = _lsf.mbdDieLog_master_set
    __swig_getmethods__["master"] = _lsf.mbdDieLog_master_get
    if _newclass:master = property(_lsf.mbdDieLog_master_get, _lsf.mbdDieLog_master_set)
    __swig_setmethods__["numRemoveJobs"] = _lsf.mbdDieLog_numRemoveJobs_set
    __swig_getmethods__["numRemoveJobs"] = _lsf.mbdDieLog_numRemoveJobs_get
    if _newclass:numRemoveJobs = property(_lsf.mbdDieLog_numRemoveJobs_get, _lsf.mbdDieLog_numRemoveJobs_set)
    __swig_setmethods__["exitCode"] = _lsf.mbdDieLog_exitCode_set
    __swig_getmethods__["exitCode"] = _lsf.mbdDieLog_exitCode_get
    if _newclass:exitCode = property(_lsf.mbdDieLog_exitCode_get, _lsf.mbdDieLog_exitCode_set)
    __swig_setmethods__["message"] = _lsf.mbdDieLog_message_set
    __swig_getmethods__["message"] = _lsf.mbdDieLog_message_get
    if _newclass:message = property(_lsf.mbdDieLog_message_get, _lsf.mbdDieLog_message_set)
    def __init__(self, *args): 
        this = _lsf.new_mbdDieLog(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _lsf.delete_mbdDieLog
    __del__ = lambda self : None;
mbdDieLog_swigregister = _lsf.mbdDieLog_swigregister
mbdDieLog_swigregister(mbdDieLog)

class unfulfillLog(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, unfulfillLog, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, unfulfillLog, name)
    __repr__ = _swig_repr
    __swig_setmethods__["jobId"] = _lsf.unfulfillLog_jobId_set
    __swig_getmethods__["jobId"] = _lsf.unfulfillLog_jobId_get
    if _newclass:jobId = property(_lsf.unfulfillLog_jobId_get, _lsf.unfulfillLog_jobId_set)
    __swig_setmethods__["notSwitched"] = _lsf.unfulfillLog_notSwitched_set
    __swig_getmethods__["notSwitched"] = _lsf.unfulfillLog_notSwitched_get
    if _newclass:notSwitched = property(_lsf.unfulfillLog_notSwitched_get, _lsf.unfulfillLog_notSwitched_set)
    __swig_setmethods__["sig"] = _lsf.unfulfillLog_sig_set
    __swig_getmethods__["sig"] = _lsf.unfulfillLog_sig_get
    if _newclass:sig = property(_lsf.unfulfillLog_sig_get, _lsf.unfulfillLog_sig_set)
    __swig_setmethods__["sig1"] = _lsf.unfulfillLog_sig1_set
    __swig_getmethods__["sig1"] = _lsf.unfulfillLog_sig1_get
    if _newclass:sig1 = property(_lsf.unfulfillLog_sig1_get, _lsf.unfulfillLog_sig1_set)
    __swig_setmethods__["sig1Flags"] = _lsf.unfulfillLog_sig1Flags_set
    __swig_getmethods__["sig1Flags"] = _lsf.unfulfillLog_sig1Flags_get
    if _newclass:sig1Flags = property(_lsf.unfulfillLog_sig1Flags_get, _lsf.unfulfillLog_sig1Flags_set)
    __swig_setmethods__["chkPeriod"] = _lsf.unfulfillLog_chkPeriod_set
    __swig_getmethods__["chkPeriod"] = _lsf.unfulfillLog_chkPeriod_get
    if _newclass:chkPeriod = property(_lsf.unfulfillLog_chkPeriod_get, _lsf.unfulfillLog_chkPeriod_set)
    __swig_setmethods__["notModified"] = _lsf.unfulfillLog_notModified_set
    __swig_getmethods__["notModified"] = _lsf.unfulfillLog_notModified_get
    if _newclass:notModified = property(_lsf.unfulfillLog_notModified_get, _lsf.unfulfillLog_notModified_set)
    __swig_setmethods__["idx"] = _lsf.unfulfillLog_idx_set
    __swig_getmethods__["idx"] = _lsf.unfulfillLog_idx_get
    if _newclass:idx = property(_lsf.unfulfillLog_idx_get, _lsf.unfulfillLog_idx_set)
    __swig_setmethods__["miscOpts4PendSig"] = _lsf.unfulfillLog_miscOpts4PendSig_set
    __swig_getmethods__["miscOpts4PendSig"] = _lsf.unfulfillLog_miscOpts4PendSig_get
    if _newclass:miscOpts4PendSig = property(_lsf.unfulfillLog_miscOpts4PendSig_get, _lsf.unfulfillLog_miscOpts4PendSig_set)
    def __init__(self, *args): 
        this = _lsf.new_unfulfillLog(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _lsf.delete_unfulfillLog
    __del__ = lambda self : None;
unfulfillLog_swigregister = _lsf.unfulfillLog_swigregister
unfulfillLog_swigregister(unfulfillLog)

TERM_UNKNOWN = _lsf.TERM_UNKNOWN
TERM_PREEMPT = _lsf.TERM_PREEMPT
TERM_WINDOW = _lsf.TERM_WINDOW
TERM_LOAD = _lsf.TERM_LOAD
TERM_OTHER = _lsf.TERM_OTHER
TERM_RUNLIMIT = _lsf.TERM_RUNLIMIT
TERM_DEADLINE = _lsf.TERM_DEADLINE
TERM_PROCESSLIMIT = _lsf.TERM_PROCESSLIMIT
TERM_FORCE_OWNER = _lsf.TERM_FORCE_OWNER
TERM_FORCE_ADMIN = _lsf.TERM_FORCE_ADMIN
TERM_REQUEUE_OWNER = _lsf.TERM_REQUEUE_OWNER
TERM_REQUEUE_ADMIN = _lsf.TERM_REQUEUE_ADMIN
TERM_CPULIMIT = _lsf.TERM_CPULIMIT
TERM_CHKPNT = _lsf.TERM_CHKPNT
TERM_OWNER = _lsf.TERM_OWNER
TERM_ADMIN = _lsf.TERM_ADMIN
TERM_MEMLIMIT = _lsf.TERM_MEMLIMIT
TERM_EXTERNAL_SIGNAL = _lsf.TERM_EXTERNAL_SIGNAL
TERM_RMS = _lsf.TERM_RMS
TERM_ZOMBIE = _lsf.TERM_ZOMBIE
TERM_SWAP = _lsf.TERM_SWAP
TERM_THREADLIMIT = _lsf.TERM_THREADLIMIT
TERM_SLURM = _lsf.TERM_SLURM
TERM_BUCKET_KILL = _lsf.TERM_BUCKET_KILL
TERM_CTRL_PID = _lsf.TERM_CTRL_PID
TERM_CWD_NOTEXIST = _lsf.TERM_CWD_NOTEXIST
class jobFinishLog(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, jobFinishLog, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, jobFinishLog, name)
    __repr__ = _swig_repr
    __swig_setmethods__["jobId"] = _lsf.jobFinishLog_jobId_set
    __swig_getmethods__["jobId"] = _lsf.jobFinishLog_jobId_get
    if _newclass:jobId = property(_lsf.jobFinishLog_jobId_get, _lsf.jobFinishLog_jobId_set)
    __swig_setmethods__["userId"] = _lsf.jobFinishLog_userId_set
    __swig_getmethods__["userId"] = _lsf.jobFinishLog_userId_get
    if _newclass:userId = property(_lsf.jobFinishLog_userId_get, _lsf.jobFinishLog_userId_set)
    __swig_setmethods__["userName"] = _lsf.jobFinishLog_userName_set
    __swig_getmethods__["userName"] = _lsf.jobFinishLog_userName_get
    if _newclass:userName = property(_lsf.jobFinishLog_userName_get, _lsf.jobFinishLog_userName_set)
    __swig_setmethods__["options"] = _lsf.jobFinishLog_options_set
    __swig_getmethods__["options"] = _lsf.jobFinishLog_options_get
    if _newclass:options = property(_lsf.jobFinishLog_options_get, _lsf.jobFinishLog_options_set)
    __swig_setmethods__["numProcessors"] = _lsf.jobFinishLog_numProcessors_set
    __swig_getmethods__["numProcessors"] = _lsf.jobFinishLog_numProcessors_get
    if _newclass:numProcessors = property(_lsf.jobFinishLog_numProcessors_get, _lsf.jobFinishLog_numProcessors_set)
    __swig_setmethods__["jStatus"] = _lsf.jobFinishLog_jStatus_set
    __swig_getmethods__["jStatus"] = _lsf.jobFinishLog_jStatus_get
    if _newclass:jStatus = property(_lsf.jobFinishLog_jStatus_get, _lsf.jobFinishLog_jStatus_set)
    __swig_setmethods__["submitTime"] = _lsf.jobFinishLog_submitTime_set
    __swig_getmethods__["submitTime"] = _lsf.jobFinishLog_submitTime_get
    if _newclass:submitTime = property(_lsf.jobFinishLog_submitTime_get, _lsf.jobFinishLog_submitTime_set)
    __swig_setmethods__["beginTime"] = _lsf.jobFinishLog_beginTime_set
    __swig_getmethods__["beginTime"] = _lsf.jobFinishLog_beginTime_get
    if _newclass:beginTime = property(_lsf.jobFinishLog_beginTime_get, _lsf.jobFinishLog_beginTime_set)
    __swig_setmethods__["termTime"] = _lsf.jobFinishLog_termTime_set
    __swig_getmethods__["termTime"] = _lsf.jobFinishLog_termTime_get
    if _newclass:termTime = property(_lsf.jobFinishLog_termTime_get, _lsf.jobFinishLog_termTime_set)
    __swig_setmethods__["startTime"] = _lsf.jobFinishLog_startTime_set
    __swig_getmethods__["startTime"] = _lsf.jobFinishLog_startTime_get
    if _newclass:startTime = property(_lsf.jobFinishLog_startTime_get, _lsf.jobFinishLog_startTime_set)
    __swig_setmethods__["endTime"] = _lsf.jobFinishLog_endTime_set
    __swig_getmethods__["endTime"] = _lsf.jobFinishLog_endTime_get
    if _newclass:endTime = property(_lsf.jobFinishLog_endTime_get, _lsf.jobFinishLog_endTime_set)
    __swig_setmethods__["queue"] = _lsf.jobFinishLog_queue_set
    __swig_getmethods__["queue"] = _lsf.jobFinishLog_queue_get
    if _newclass:queue = property(_lsf.jobFinishLog_queue_get, _lsf.jobFinishLog_queue_set)
    __swig_setmethods__["resReq"] = _lsf.jobFinishLog_resReq_set
    __swig_getmethods__["resReq"] = _lsf.jobFinishLog_resReq_get
    if _newclass:resReq = property(_lsf.jobFinishLog_resReq_get, _lsf.jobFinishLog_resReq_set)
    __swig_setmethods__["fromHost"] = _lsf.jobFinishLog_fromHost_set
    __swig_getmethods__["fromHost"] = _lsf.jobFinishLog_fromHost_get
    if _newclass:fromHost = property(_lsf.jobFinishLog_fromHost_get, _lsf.jobFinishLog_fromHost_set)
    __swig_setmethods__["cwd"] = _lsf.jobFinishLog_cwd_set
    __swig_getmethods__["cwd"] = _lsf.jobFinishLog_cwd_get
    if _newclass:cwd = property(_lsf.jobFinishLog_cwd_get, _lsf.jobFinishLog_cwd_set)
    __swig_setmethods__["inFile"] = _lsf.jobFinishLog_inFile_set
    __swig_getmethods__["inFile"] = _lsf.jobFinishLog_inFile_get
    if _newclass:inFile = property(_lsf.jobFinishLog_inFile_get, _lsf.jobFinishLog_inFile_set)
    __swig_setmethods__["outFile"] = _lsf.jobFinishLog_outFile_set
    __swig_getmethods__["outFile"] = _lsf.jobFinishLog_outFile_get
    if _newclass:outFile = property(_lsf.jobFinishLog_outFile_get, _lsf.jobFinishLog_outFile_set)
    __swig_setmethods__["errFile"] = _lsf.jobFinishLog_errFile_set
    __swig_getmethods__["errFile"] = _lsf.jobFinishLog_errFile_get
    if _newclass:errFile = property(_lsf.jobFinishLog_errFile_get, _lsf.jobFinishLog_errFile_set)
    __swig_setmethods__["inFileSpool"] = _lsf.jobFinishLog_inFileSpool_set
    __swig_getmethods__["inFileSpool"] = _lsf.jobFinishLog_inFileSpool_get
    if _newclass:inFileSpool = property(_lsf.jobFinishLog_inFileSpool_get, _lsf.jobFinishLog_inFileSpool_set)
    __swig_setmethods__["commandSpool"] = _lsf.jobFinishLog_commandSpool_set
    __swig_getmethods__["commandSpool"] = _lsf.jobFinishLog_commandSpool_get
    if _newclass:commandSpool = property(_lsf.jobFinishLog_commandSpool_get, _lsf.jobFinishLog_commandSpool_set)
    __swig_setmethods__["jobFile"] = _lsf.jobFinishLog_jobFile_set
    __swig_getmethods__["jobFile"] = _lsf.jobFinishLog_jobFile_get
    if _newclass:jobFile = property(_lsf.jobFinishLog_jobFile_get, _lsf.jobFinishLog_jobFile_set)
    __swig_setmethods__["numAskedHosts"] = _lsf.jobFinishLog_numAskedHosts_set
    __swig_getmethods__["numAskedHosts"] = _lsf.jobFinishLog_numAskedHosts_get
    if _newclass:numAskedHosts = property(_lsf.jobFinishLog_numAskedHosts_get, _lsf.jobFinishLog_numAskedHosts_set)
    __swig_setmethods__["askedHosts"] = _lsf.jobFinishLog_askedHosts_set
    __swig_getmethods__["askedHosts"] = _lsf.jobFinishLog_askedHosts_get
    if _newclass:askedHosts = property(_lsf.jobFinishLog_askedHosts_get, _lsf.jobFinishLog_askedHosts_set)
    __swig_setmethods__["hostFactor"] = _lsf.jobFinishLog_hostFactor_set
    __swig_getmethods__["hostFactor"] = _lsf.jobFinishLog_hostFactor_get
    if _newclass:hostFactor = property(_lsf.jobFinishLog_hostFactor_get, _lsf.jobFinishLog_hostFactor_set)
    __swig_setmethods__["numExHosts"] = _lsf.jobFinishLog_numExHosts_set
    __swig_getmethods__["numExHosts"] = _lsf.jobFinishLog_numExHosts_get
    if _newclass:numExHosts = property(_lsf.jobFinishLog_numExHosts_get, _lsf.jobFinishLog_numExHosts_set)
    __swig_setmethods__["execHosts"] = _lsf.jobFinishLog_execHosts_set
    __swig_getmethods__["execHosts"] = _lsf.jobFinishLog_execHosts_get
    if _newclass:execHosts = property(_lsf.jobFinishLog_execHosts_get, _lsf.jobFinishLog_execHosts_set)
    __swig_setmethods__["cpuTime"] = _lsf.jobFinishLog_cpuTime_set
    __swig_getmethods__["cpuTime"] = _lsf.jobFinishLog_cpuTime_get
    if _newclass:cpuTime = property(_lsf.jobFinishLog_cpuTime_get, _lsf.jobFinishLog_cpuTime_set)
    __swig_setmethods__["jobName"] = _lsf.jobFinishLog_jobName_set
    __swig_getmethods__["jobName"] = _lsf.jobFinishLog_jobName_get
    if _newclass:jobName = property(_lsf.jobFinishLog_jobName_get, _lsf.jobFinishLog_jobName_set)
    __swig_setmethods__["command"] = _lsf.jobFinishLog_command_set
    __swig_getmethods__["command"] = _lsf.jobFinishLog_command_get
    if _newclass:command = property(_lsf.jobFinishLog_command_get, _lsf.jobFinishLog_command_set)
    __swig_setmethods__["lsfRusage"] = _lsf.jobFinishLog_lsfRusage_set
    __swig_getmethods__["lsfRusage"] = _lsf.jobFinishLog_lsfRusage_get
    if _newclass:lsfRusage = property(_lsf.jobFinishLog_lsfRusage_get, _lsf.jobFinishLog_lsfRusage_set)
    __swig_setmethods__["dependCond"] = _lsf.jobFinishLog_dependCond_set
    __swig_getmethods__["dependCond"] = _lsf.jobFinishLog_dependCond_get
    if _newclass:dependCond = property(_lsf.jobFinishLog_dependCond_get, _lsf.jobFinishLog_dependCond_set)
    __swig_setmethods__["timeEvent"] = _lsf.jobFinishLog_timeEvent_set
    __swig_getmethods__["timeEvent"] = _lsf.jobFinishLog_timeEvent_get
    if _newclass:timeEvent = property(_lsf.jobFinishLog_timeEvent_get, _lsf.jobFinishLog_timeEvent_set)
    __swig_setmethods__["preExecCmd"] = _lsf.jobFinishLog_preExecCmd_set
    __swig_getmethods__["preExecCmd"] = _lsf.jobFinishLog_preExecCmd_get
    if _newclass:preExecCmd = property(_lsf.jobFinishLog_preExecCmd_get, _lsf.jobFinishLog_preExecCmd_set)
    __swig_setmethods__["mailUser"] = _lsf.jobFinishLog_mailUser_set
    __swig_getmethods__["mailUser"] = _lsf.jobFinishLog_mailUser_get
    if _newclass:mailUser = property(_lsf.jobFinishLog_mailUser_get, _lsf.jobFinishLog_mailUser_set)
    __swig_setmethods__["projectName"] = _lsf.jobFinishLog_projectName_set
    __swig_getmethods__["projectName"] = _lsf.jobFinishLog_projectName_get
    if _newclass:projectName = property(_lsf.jobFinishLog_projectName_get, _lsf.jobFinishLog_projectName_set)
    __swig_setmethods__["exitStatus"] = _lsf.jobFinishLog_exitStatus_set
    __swig_getmethods__["exitStatus"] = _lsf.jobFinishLog_exitStatus_get
    if _newclass:exitStatus = property(_lsf.jobFinishLog_exitStatus_get, _lsf.jobFinishLog_exitStatus_set)
    __swig_setmethods__["maxNumProcessors"] = _lsf.jobFinishLog_maxNumProcessors_set
    __swig_getmethods__["maxNumProcessors"] = _lsf.jobFinishLog_maxNumProcessors_get
    if _newclass:maxNumProcessors = property(_lsf.jobFinishLog_maxNumProcessors_get, _lsf.jobFinishLog_maxNumProcessors_set)
    __swig_setmethods__["loginShell"] = _lsf.jobFinishLog_loginShell_set
    __swig_getmethods__["loginShell"] = _lsf.jobFinishLog_loginShell_get
    if _newclass:loginShell = property(_lsf.jobFinishLog_loginShell_get, _lsf.jobFinishLog_loginShell_set)
    __swig_setmethods__["idx"] = _lsf.jobFinishLog_idx_set
    __swig_getmethods__["idx"] = _lsf.jobFinishLog_idx_get
    if _newclass:idx = property(_lsf.jobFinishLog_idx_get, _lsf.jobFinishLog_idx_set)
    __swig_setmethods__["maxRMem"] = _lsf.jobFinishLog_maxRMem_set
    __swig_getmethods__["maxRMem"] = _lsf.jobFinishLog_maxRMem_get
    if _newclass:maxRMem = property(_lsf.jobFinishLog_maxRMem_get, _lsf.jobFinishLog_maxRMem_set)
    __swig_setmethods__["maxRSwap"] = _lsf.jobFinishLog_maxRSwap_set
    __swig_getmethods__["maxRSwap"] = _lsf.jobFinishLog_maxRSwap_get
    if _newclass:maxRSwap = property(_lsf.jobFinishLog_maxRSwap_get, _lsf.jobFinishLog_maxRSwap_set)
    __swig_setmethods__["rsvId"] = _lsf.jobFinishLog_rsvId_set
    __swig_getmethods__["rsvId"] = _lsf.jobFinishLog_rsvId_get
    if _newclass:rsvId = property(_lsf.jobFinishLog_rsvId_get, _lsf.jobFinishLog_rsvId_set)
    __swig_setmethods__["sla"] = _lsf.jobFinishLog_sla_set
    __swig_getmethods__["sla"] = _lsf.jobFinishLog_sla_get
    if _newclass:sla = property(_lsf.jobFinishLog_sla_get, _lsf.jobFinishLog_sla_set)
    __swig_setmethods__["exceptMask"] = _lsf.jobFinishLog_exceptMask_set
    __swig_getmethods__["exceptMask"] = _lsf.jobFinishLog_exceptMask_get
    if _newclass:exceptMask = property(_lsf.jobFinishLog_exceptMask_get, _lsf.jobFinishLog_exceptMask_set)
    __swig_setmethods__["additionalInfo"] = _lsf.jobFinishLog_additionalInfo_set
    __swig_getmethods__["additionalInfo"] = _lsf.jobFinishLog_additionalInfo_get
    if _newclass:additionalInfo = property(_lsf.jobFinishLog_additionalInfo_get, _lsf.jobFinishLog_additionalInfo_set)
    __swig_setmethods__["exitInfo"] = _lsf.jobFinishLog_exitInfo_set
    __swig_getmethods__["exitInfo"] = _lsf.jobFinishLog_exitInfo_get
    if _newclass:exitInfo = property(_lsf.jobFinishLog_exitInfo_get, _lsf.jobFinishLog_exitInfo_set)
    __swig_setmethods__["warningTimePeriod"] = _lsf.jobFinishLog_warningTimePeriod_set
    __swig_getmethods__["warningTimePeriod"] = _lsf.jobFinishLog_warningTimePeriod_get
    if _newclass:warningTimePeriod = property(_lsf.jobFinishLog_warningTimePeriod_get, _lsf.jobFinishLog_warningTimePeriod_set)
    __swig_setmethods__["warningAction"] = _lsf.jobFinishLog_warningAction_set
    __swig_getmethods__["warningAction"] = _lsf.jobFinishLog_warningAction_get
    if _newclass:warningAction = property(_lsf.jobFinishLog_warningAction_get, _lsf.jobFinishLog_warningAction_set)
    __swig_setmethods__["chargedSAAP"] = _lsf.jobFinishLog_chargedSAAP_set
    __swig_getmethods__["chargedSAAP"] = _lsf.jobFinishLog_chargedSAAP_get
    if _newclass:chargedSAAP = property(_lsf.jobFinishLog_chargedSAAP_get, _lsf.jobFinishLog_chargedSAAP_set)
    __swig_setmethods__["licenseProject"] = _lsf.jobFinishLog_licenseProject_set
    __swig_getmethods__["licenseProject"] = _lsf.jobFinishLog_licenseProject_get
    if _newclass:licenseProject = property(_lsf.jobFinishLog_licenseProject_get, _lsf.jobFinishLog_licenseProject_set)
    __swig_setmethods__["app"] = _lsf.jobFinishLog_app_set
    __swig_getmethods__["app"] = _lsf.jobFinishLog_app_get
    if _newclass:app = property(_lsf.jobFinishLog_app_get, _lsf.jobFinishLog_app_set)
    __swig_setmethods__["postExecCmd"] = _lsf.jobFinishLog_postExecCmd_set
    __swig_getmethods__["postExecCmd"] = _lsf.jobFinishLog_postExecCmd_get
    if _newclass:postExecCmd = property(_lsf.jobFinishLog_postExecCmd_get, _lsf.jobFinishLog_postExecCmd_set)
    __swig_setmethods__["runtimeEstimation"] = _lsf.jobFinishLog_runtimeEstimation_set
    __swig_getmethods__["runtimeEstimation"] = _lsf.jobFinishLog_runtimeEstimation_get
    if _newclass:runtimeEstimation = property(_lsf.jobFinishLog_runtimeEstimation_get, _lsf.jobFinishLog_runtimeEstimation_set)
    __swig_setmethods__["jgroup"] = _lsf.jobFinishLog_jgroup_set
    __swig_getmethods__["jgroup"] = _lsf.jobFinishLog_jgroup_get
    if _newclass:jgroup = property(_lsf.jobFinishLog_jgroup_get, _lsf.jobFinishLog_jgroup_set)
    __swig_setmethods__["options2"] = _lsf.jobFinishLog_options2_set
    __swig_getmethods__["options2"] = _lsf.jobFinishLog_options2_get
    if _newclass:options2 = property(_lsf.jobFinishLog_options2_get, _lsf.jobFinishLog_options2_set)
    __swig_setmethods__["requeueEValues"] = _lsf.jobFinishLog_requeueEValues_set
    __swig_getmethods__["requeueEValues"] = _lsf.jobFinishLog_requeueEValues_get
    if _newclass:requeueEValues = property(_lsf.jobFinishLog_requeueEValues_get, _lsf.jobFinishLog_requeueEValues_set)
    __swig_setmethods__["notifyCmd"] = _lsf.jobFinishLog_notifyCmd_set
    __swig_getmethods__["notifyCmd"] = _lsf.jobFinishLog_notifyCmd_get
    if _newclass:notifyCmd = property(_lsf.jobFinishLog_notifyCmd_get, _lsf.jobFinishLog_notifyCmd_set)
    __swig_setmethods__["lastResizeTime"] = _lsf.jobFinishLog_lastResizeTime_set
    __swig_getmethods__["lastResizeTime"] = _lsf.jobFinishLog_lastResizeTime_get
    if _newclass:lastResizeTime = property(_lsf.jobFinishLog_lastResizeTime_get, _lsf.jobFinishLog_lastResizeTime_set)
    __swig_setmethods__["jobDescription"] = _lsf.jobFinishLog_jobDescription_set
    __swig_getmethods__["jobDescription"] = _lsf.jobFinishLog_jobDescription_get
    if _newclass:jobDescription = property(_lsf.jobFinishLog_jobDescription_get, _lsf.jobFinishLog_jobDescription_set)
    __swig_setmethods__["submitExt"] = _lsf.jobFinishLog_submitExt_set
    __swig_getmethods__["submitExt"] = _lsf.jobFinishLog_submitExt_get
    if _newclass:submitExt = property(_lsf.jobFinishLog_submitExt_get, _lsf.jobFinishLog_submitExt_set)
    __swig_setmethods__["numhRusages"] = _lsf.jobFinishLog_numhRusages_set
    __swig_getmethods__["numhRusages"] = _lsf.jobFinishLog_numhRusages_get
    if _newclass:numhRusages = property(_lsf.jobFinishLog_numhRusages_get, _lsf.jobFinishLog_numhRusages_set)
    __swig_setmethods__["hostRusage"] = _lsf.jobFinishLog_hostRusage_set
    __swig_getmethods__["hostRusage"] = _lsf.jobFinishLog_hostRusage_get
    if _newclass:hostRusage = property(_lsf.jobFinishLog_hostRusage_get, _lsf.jobFinishLog_hostRusage_set)
    def __init__(self, *args): 
        this = _lsf.new_jobFinishLog(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _lsf.delete_jobFinishLog
    __del__ = lambda self : None;
jobFinishLog_swigregister = _lsf.jobFinishLog_swigregister
jobFinishLog_swigregister(jobFinishLog)

class jobFinish2Log(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, jobFinish2Log, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, jobFinish2Log, name)
    __repr__ = _swig_repr
    __swig_setmethods__["jobId"] = _lsf.jobFinish2Log_jobId_set
    __swig_getmethods__["jobId"] = _lsf.jobFinish2Log_jobId_get
    if _newclass:jobId = property(_lsf.jobFinish2Log_jobId_get, _lsf.jobFinish2Log_jobId_set)
    __swig_setmethods__["userId"] = _lsf.jobFinish2Log_userId_set
    __swig_getmethods__["userId"] = _lsf.jobFinish2Log_userId_get
    if _newclass:userId = property(_lsf.jobFinish2Log_userId_get, _lsf.jobFinish2Log_userId_set)
    __swig_setmethods__["userName"] = _lsf.jobFinish2Log_userName_set
    __swig_getmethods__["userName"] = _lsf.jobFinish2Log_userName_get
    if _newclass:userName = property(_lsf.jobFinish2Log_userName_get, _lsf.jobFinish2Log_userName_set)
    __swig_setmethods__["options"] = _lsf.jobFinish2Log_options_set
    __swig_getmethods__["options"] = _lsf.jobFinish2Log_options_get
    if _newclass:options = property(_lsf.jobFinish2Log_options_get, _lsf.jobFinish2Log_options_set)
    __swig_setmethods__["numProcessors"] = _lsf.jobFinish2Log_numProcessors_set
    __swig_getmethods__["numProcessors"] = _lsf.jobFinish2Log_numProcessors_get
    if _newclass:numProcessors = property(_lsf.jobFinish2Log_numProcessors_get, _lsf.jobFinish2Log_numProcessors_set)
    __swig_setmethods__["jStatus"] = _lsf.jobFinish2Log_jStatus_set
    __swig_getmethods__["jStatus"] = _lsf.jobFinish2Log_jStatus_get
    if _newclass:jStatus = property(_lsf.jobFinish2Log_jStatus_get, _lsf.jobFinish2Log_jStatus_set)
    __swig_setmethods__["submitTime"] = _lsf.jobFinish2Log_submitTime_set
    __swig_getmethods__["submitTime"] = _lsf.jobFinish2Log_submitTime_get
    if _newclass:submitTime = property(_lsf.jobFinish2Log_submitTime_get, _lsf.jobFinish2Log_submitTime_set)
    __swig_setmethods__["termTime"] = _lsf.jobFinish2Log_termTime_set
    __swig_getmethods__["termTime"] = _lsf.jobFinish2Log_termTime_get
    if _newclass:termTime = property(_lsf.jobFinish2Log_termTime_get, _lsf.jobFinish2Log_termTime_set)
    __swig_setmethods__["startTime"] = _lsf.jobFinish2Log_startTime_set
    __swig_getmethods__["startTime"] = _lsf.jobFinish2Log_startTime_get
    if _newclass:startTime = property(_lsf.jobFinish2Log_startTime_get, _lsf.jobFinish2Log_startTime_set)
    __swig_setmethods__["endTime"] = _lsf.jobFinish2Log_endTime_set
    __swig_getmethods__["endTime"] = _lsf.jobFinish2Log_endTime_get
    if _newclass:endTime = property(_lsf.jobFinish2Log_endTime_get, _lsf.jobFinish2Log_endTime_set)
    __swig_setmethods__["queue"] = _lsf.jobFinish2Log_queue_set
    __swig_getmethods__["queue"] = _lsf.jobFinish2Log_queue_get
    if _newclass:queue = property(_lsf.jobFinish2Log_queue_get, _lsf.jobFinish2Log_queue_set)
    __swig_setmethods__["resReq"] = _lsf.jobFinish2Log_resReq_set
    __swig_getmethods__["resReq"] = _lsf.jobFinish2Log_resReq_get
    if _newclass:resReq = property(_lsf.jobFinish2Log_resReq_get, _lsf.jobFinish2Log_resReq_set)
    __swig_setmethods__["fromHost"] = _lsf.jobFinish2Log_fromHost_set
    __swig_getmethods__["fromHost"] = _lsf.jobFinish2Log_fromHost_get
    if _newclass:fromHost = property(_lsf.jobFinish2Log_fromHost_get, _lsf.jobFinish2Log_fromHost_set)
    __swig_setmethods__["cwd"] = _lsf.jobFinish2Log_cwd_set
    __swig_getmethods__["cwd"] = _lsf.jobFinish2Log_cwd_get
    if _newclass:cwd = property(_lsf.jobFinish2Log_cwd_get, _lsf.jobFinish2Log_cwd_set)
    __swig_setmethods__["inFile"] = _lsf.jobFinish2Log_inFile_set
    __swig_getmethods__["inFile"] = _lsf.jobFinish2Log_inFile_get
    if _newclass:inFile = property(_lsf.jobFinish2Log_inFile_get, _lsf.jobFinish2Log_inFile_set)
    __swig_setmethods__["outFile"] = _lsf.jobFinish2Log_outFile_set
    __swig_getmethods__["outFile"] = _lsf.jobFinish2Log_outFile_get
    if _newclass:outFile = property(_lsf.jobFinish2Log_outFile_get, _lsf.jobFinish2Log_outFile_set)
    __swig_setmethods__["jobFile"] = _lsf.jobFinish2Log_jobFile_set
    __swig_getmethods__["jobFile"] = _lsf.jobFinish2Log_jobFile_get
    if _newclass:jobFile = property(_lsf.jobFinish2Log_jobFile_get, _lsf.jobFinish2Log_jobFile_set)
    __swig_setmethods__["numExHosts"] = _lsf.jobFinish2Log_numExHosts_set
    __swig_getmethods__["numExHosts"] = _lsf.jobFinish2Log_numExHosts_get
    if _newclass:numExHosts = property(_lsf.jobFinish2Log_numExHosts_get, _lsf.jobFinish2Log_numExHosts_set)
    __swig_setmethods__["execHosts"] = _lsf.jobFinish2Log_execHosts_set
    __swig_getmethods__["execHosts"] = _lsf.jobFinish2Log_execHosts_get
    if _newclass:execHosts = property(_lsf.jobFinish2Log_execHosts_get, _lsf.jobFinish2Log_execHosts_set)
    __swig_setmethods__["slotUsages"] = _lsf.jobFinish2Log_slotUsages_set
    __swig_getmethods__["slotUsages"] = _lsf.jobFinish2Log_slotUsages_get
    if _newclass:slotUsages = property(_lsf.jobFinish2Log_slotUsages_get, _lsf.jobFinish2Log_slotUsages_set)
    __swig_setmethods__["cpuTime"] = _lsf.jobFinish2Log_cpuTime_set
    __swig_getmethods__["cpuTime"] = _lsf.jobFinish2Log_cpuTime_get
    if _newclass:cpuTime = property(_lsf.jobFinish2Log_cpuTime_get, _lsf.jobFinish2Log_cpuTime_set)
    __swig_setmethods__["jobName"] = _lsf.jobFinish2Log_jobName_set
    __swig_getmethods__["jobName"] = _lsf.jobFinish2Log_jobName_get
    if _newclass:jobName = property(_lsf.jobFinish2Log_jobName_get, _lsf.jobFinish2Log_jobName_set)
    __swig_setmethods__["command"] = _lsf.jobFinish2Log_command_set
    __swig_getmethods__["command"] = _lsf.jobFinish2Log_command_get
    if _newclass:command = property(_lsf.jobFinish2Log_command_get, _lsf.jobFinish2Log_command_set)
    __swig_setmethods__["lsfRusage"] = _lsf.jobFinish2Log_lsfRusage_set
    __swig_getmethods__["lsfRusage"] = _lsf.jobFinish2Log_lsfRusage_get
    if _newclass:lsfRusage = property(_lsf.jobFinish2Log_lsfRusage_get, _lsf.jobFinish2Log_lsfRusage_set)
    __swig_setmethods__["preExecCmd"] = _lsf.jobFinish2Log_preExecCmd_set
    __swig_getmethods__["preExecCmd"] = _lsf.jobFinish2Log_preExecCmd_get
    if _newclass:preExecCmd = property(_lsf.jobFinish2Log_preExecCmd_get, _lsf.jobFinish2Log_preExecCmd_set)
    __swig_setmethods__["projectName"] = _lsf.jobFinish2Log_projectName_set
    __swig_getmethods__["projectName"] = _lsf.jobFinish2Log_projectName_get
    if _newclass:projectName = property(_lsf.jobFinish2Log_projectName_get, _lsf.jobFinish2Log_projectName_set)
    __swig_setmethods__["exitStatus"] = _lsf.jobFinish2Log_exitStatus_set
    __swig_getmethods__["exitStatus"] = _lsf.jobFinish2Log_exitStatus_get
    if _newclass:exitStatus = property(_lsf.jobFinish2Log_exitStatus_get, _lsf.jobFinish2Log_exitStatus_set)
    __swig_setmethods__["maxNumProcessors"] = _lsf.jobFinish2Log_maxNumProcessors_set
    __swig_getmethods__["maxNumProcessors"] = _lsf.jobFinish2Log_maxNumProcessors_get
    if _newclass:maxNumProcessors = property(_lsf.jobFinish2Log_maxNumProcessors_get, _lsf.jobFinish2Log_maxNumProcessors_set)
    __swig_setmethods__["sla"] = _lsf.jobFinish2Log_sla_set
    __swig_getmethods__["sla"] = _lsf.jobFinish2Log_sla_get
    if _newclass:sla = property(_lsf.jobFinish2Log_sla_get, _lsf.jobFinish2Log_sla_set)
    __swig_setmethods__["exitInfo"] = _lsf.jobFinish2Log_exitInfo_set
    __swig_getmethods__["exitInfo"] = _lsf.jobFinish2Log_exitInfo_get
    if _newclass:exitInfo = property(_lsf.jobFinish2Log_exitInfo_get, _lsf.jobFinish2Log_exitInfo_set)
    __swig_setmethods__["chargedSAAP"] = _lsf.jobFinish2Log_chargedSAAP_set
    __swig_getmethods__["chargedSAAP"] = _lsf.jobFinish2Log_chargedSAAP_get
    if _newclass:chargedSAAP = property(_lsf.jobFinish2Log_chargedSAAP_get, _lsf.jobFinish2Log_chargedSAAP_set)
    __swig_setmethods__["licenseProject"] = _lsf.jobFinish2Log_licenseProject_set
    __swig_getmethods__["licenseProject"] = _lsf.jobFinish2Log_licenseProject_get
    if _newclass:licenseProject = property(_lsf.jobFinish2Log_licenseProject_get, _lsf.jobFinish2Log_licenseProject_set)
    __swig_setmethods__["app"] = _lsf.jobFinish2Log_app_set
    __swig_getmethods__["app"] = _lsf.jobFinish2Log_app_get
    if _newclass:app = property(_lsf.jobFinish2Log_app_get, _lsf.jobFinish2Log_app_set)
    __swig_setmethods__["postExecCmd"] = _lsf.jobFinish2Log_postExecCmd_set
    __swig_getmethods__["postExecCmd"] = _lsf.jobFinish2Log_postExecCmd_get
    if _newclass:postExecCmd = property(_lsf.jobFinish2Log_postExecCmd_get, _lsf.jobFinish2Log_postExecCmd_set)
    __swig_setmethods__["jgroup"] = _lsf.jobFinish2Log_jgroup_set
    __swig_getmethods__["jgroup"] = _lsf.jobFinish2Log_jgroup_get
    if _newclass:jgroup = property(_lsf.jobFinish2Log_jgroup_get, _lsf.jobFinish2Log_jgroup_set)
    __swig_setmethods__["numhRusages"] = _lsf.jobFinish2Log_numhRusages_set
    __swig_getmethods__["numhRusages"] = _lsf.jobFinish2Log_numhRusages_get
    if _newclass:numhRusages = property(_lsf.jobFinish2Log_numhRusages_get, _lsf.jobFinish2Log_numhRusages_set)
    __swig_setmethods__["hostRusage"] = _lsf.jobFinish2Log_hostRusage_set
    __swig_getmethods__["hostRusage"] = _lsf.jobFinish2Log_hostRusage_get
    if _newclass:hostRusage = property(_lsf.jobFinish2Log_hostRusage_get, _lsf.jobFinish2Log_hostRusage_set)
    __swig_setmethods__["execRusage"] = _lsf.jobFinish2Log_execRusage_set
    __swig_getmethods__["execRusage"] = _lsf.jobFinish2Log_execRusage_get
    if _newclass:execRusage = property(_lsf.jobFinish2Log_execRusage_get, _lsf.jobFinish2Log_execRusage_set)
    __swig_setmethods__["clusterName"] = _lsf.jobFinish2Log_clusterName_set
    __swig_getmethods__["clusterName"] = _lsf.jobFinish2Log_clusterName_get
    if _newclass:clusterName = property(_lsf.jobFinish2Log_clusterName_get, _lsf.jobFinish2Log_clusterName_set)
    __swig_setmethods__["userGroup"] = _lsf.jobFinish2Log_userGroup_set
    __swig_getmethods__["userGroup"] = _lsf.jobFinish2Log_userGroup_get
    if _newclass:userGroup = property(_lsf.jobFinish2Log_userGroup_get, _lsf.jobFinish2Log_userGroup_set)
    __swig_setmethods__["runtime"] = _lsf.jobFinish2Log_runtime_set
    __swig_getmethods__["runtime"] = _lsf.jobFinish2Log_runtime_get
    if _newclass:runtime = property(_lsf.jobFinish2Log_runtime_get, _lsf.jobFinish2Log_runtime_set)
    def __init__(self, *args): 
        this = _lsf.new_jobFinish2Log(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _lsf.delete_jobFinish2Log
    __del__ = lambda self : None;
jobFinish2Log_swigregister = _lsf.jobFinish2Log_swigregister
jobFinish2Log_swigregister(jobFinish2Log)

class jobStartLimitLog(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, jobStartLimitLog, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, jobStartLimitLog, name)
    __repr__ = _swig_repr
    __swig_setmethods__["clusterName"] = _lsf.jobStartLimitLog_clusterName_set
    __swig_getmethods__["clusterName"] = _lsf.jobStartLimitLog_clusterName_get
    if _newclass:clusterName = property(_lsf.jobStartLimitLog_clusterName_get, _lsf.jobStartLimitLog_clusterName_set)
    __swig_setmethods__["jobId"] = _lsf.jobStartLimitLog_jobId_set
    __swig_getmethods__["jobId"] = _lsf.jobStartLimitLog_jobId_get
    if _newclass:jobId = property(_lsf.jobStartLimitLog_jobId_get, _lsf.jobStartLimitLog_jobId_set)
    __swig_setmethods__["options"] = _lsf.jobStartLimitLog_options_set
    __swig_getmethods__["options"] = _lsf.jobStartLimitLog_options_get
    if _newclass:options = property(_lsf.jobStartLimitLog_options_get, _lsf.jobStartLimitLog_options_set)
    __swig_setmethods__["lsfLimits"] = _lsf.jobStartLimitLog_lsfLimits_set
    __swig_getmethods__["lsfLimits"] = _lsf.jobStartLimitLog_lsfLimits_get
    if _newclass:lsfLimits = property(_lsf.jobStartLimitLog_lsfLimits_get, _lsf.jobStartLimitLog_lsfLimits_set)
    __swig_setmethods__["jobRlimits"] = _lsf.jobStartLimitLog_jobRlimits_set
    __swig_getmethods__["jobRlimits"] = _lsf.jobStartLimitLog_jobRlimits_get
    if _newclass:jobRlimits = property(_lsf.jobStartLimitLog_jobRlimits_get, _lsf.jobStartLimitLog_jobRlimits_set)
    def __init__(self, *args): 
        this = _lsf.new_jobStartLimitLog(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _lsf.delete_jobStartLimitLog
    __del__ = lambda self : None;
jobStartLimitLog_swigregister = _lsf.jobStartLimitLog_swigregister
jobStartLimitLog_swigregister(jobStartLimitLog)

class jobStatus2Log(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, jobStatus2Log, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, jobStatus2Log, name)
    __repr__ = _swig_repr
    __swig_setmethods__["currentTime"] = _lsf.jobStatus2Log_currentTime_set
    __swig_getmethods__["currentTime"] = _lsf.jobStatus2Log_currentTime_get
    if _newclass:currentTime = property(_lsf.jobStatus2Log_currentTime_get, _lsf.jobStatus2Log_currentTime_set)
    __swig_setmethods__["sampleInterval"] = _lsf.jobStatus2Log_sampleInterval_set
    __swig_getmethods__["sampleInterval"] = _lsf.jobStatus2Log_sampleInterval_get
    if _newclass:sampleInterval = property(_lsf.jobStatus2Log_sampleInterval_get, _lsf.jobStatus2Log_sampleInterval_set)
    __swig_setmethods__["jStatus"] = _lsf.jobStatus2Log_jStatus_set
    __swig_getmethods__["jStatus"] = _lsf.jobStatus2Log_jStatus_get
    if _newclass:jStatus = property(_lsf.jobStatus2Log_jStatus_get, _lsf.jobStatus2Log_jStatus_set)
    __swig_setmethods__["jobId"] = _lsf.jobStatus2Log_jobId_set
    __swig_getmethods__["jobId"] = _lsf.jobStatus2Log_jobId_get
    if _newclass:jobId = property(_lsf.jobStatus2Log_jobId_get, _lsf.jobStatus2Log_jobId_set)
    __swig_setmethods__["userName"] = _lsf.jobStatus2Log_userName_set
    __swig_getmethods__["userName"] = _lsf.jobStatus2Log_userName_get
    if _newclass:userName = property(_lsf.jobStatus2Log_userName_get, _lsf.jobStatus2Log_userName_set)
    __swig_setmethods__["submitTime"] = _lsf.jobStatus2Log_submitTime_set
    __swig_getmethods__["submitTime"] = _lsf.jobStatus2Log_submitTime_get
    if _newclass:submitTime = property(_lsf.jobStatus2Log_submitTime_get, _lsf.jobStatus2Log_submitTime_set)
    __swig_setmethods__["startTime"] = _lsf.jobStatus2Log_startTime_set
    __swig_getmethods__["startTime"] = _lsf.jobStatus2Log_startTime_get
    if _newclass:startTime = property(_lsf.jobStatus2Log_startTime_get, _lsf.jobStatus2Log_startTime_set)
    __swig_setmethods__["endTime"] = _lsf.jobStatus2Log_endTime_set
    __swig_getmethods__["endTime"] = _lsf.jobStatus2Log_endTime_get
    if _newclass:endTime = property(_lsf.jobStatus2Log_endTime_get, _lsf.jobStatus2Log_endTime_set)
    __swig_setmethods__["queue"] = _lsf.jobStatus2Log_queue_set
    __swig_getmethods__["queue"] = _lsf.jobStatus2Log_queue_get
    if _newclass:queue = property(_lsf.jobStatus2Log_queue_get, _lsf.jobStatus2Log_queue_set)
    __swig_setmethods__["resReq"] = _lsf.jobStatus2Log_resReq_set
    __swig_getmethods__["resReq"] = _lsf.jobStatus2Log_resReq_get
    if _newclass:resReq = property(_lsf.jobStatus2Log_resReq_get, _lsf.jobStatus2Log_resReq_set)
    __swig_setmethods__["projectName"] = _lsf.jobStatus2Log_projectName_set
    __swig_getmethods__["projectName"] = _lsf.jobStatus2Log_projectName_get
    if _newclass:projectName = property(_lsf.jobStatus2Log_projectName_get, _lsf.jobStatus2Log_projectName_set)
    __swig_setmethods__["app"] = _lsf.jobStatus2Log_app_set
    __swig_getmethods__["app"] = _lsf.jobStatus2Log_app_get
    if _newclass:app = property(_lsf.jobStatus2Log_app_get, _lsf.jobStatus2Log_app_set)
    __swig_setmethods__["clusterName"] = _lsf.jobStatus2Log_clusterName_set
    __swig_getmethods__["clusterName"] = _lsf.jobStatus2Log_clusterName_get
    if _newclass:clusterName = property(_lsf.jobStatus2Log_clusterName_get, _lsf.jobStatus2Log_clusterName_set)
    __swig_setmethods__["userGroup"] = _lsf.jobStatus2Log_userGroup_set
    __swig_getmethods__["userGroup"] = _lsf.jobStatus2Log_userGroup_get
    if _newclass:userGroup = property(_lsf.jobStatus2Log_userGroup_get, _lsf.jobStatus2Log_userGroup_set)
    __swig_setmethods__["numProcessors"] = _lsf.jobStatus2Log_numProcessors_set
    __swig_getmethods__["numProcessors"] = _lsf.jobStatus2Log_numProcessors_get
    if _newclass:numProcessors = property(_lsf.jobStatus2Log_numProcessors_get, _lsf.jobStatus2Log_numProcessors_set)
    __swig_setmethods__["numJobs"] = _lsf.jobStatus2Log_numJobs_set
    __swig_getmethods__["numJobs"] = _lsf.jobStatus2Log_numJobs_get
    if _newclass:numJobs = property(_lsf.jobStatus2Log_numJobs_get, _lsf.jobStatus2Log_numJobs_set)
    __swig_setmethods__["runtimeDelta"] = _lsf.jobStatus2Log_runtimeDelta_set
    __swig_getmethods__["runtimeDelta"] = _lsf.jobStatus2Log_runtimeDelta_get
    if _newclass:runtimeDelta = property(_lsf.jobStatus2Log_runtimeDelta_get, _lsf.jobStatus2Log_runtimeDelta_set)
    __swig_setmethods__["lsfRusage"] = _lsf.jobStatus2Log_lsfRusage_set
    __swig_getmethods__["lsfRusage"] = _lsf.jobStatus2Log_lsfRusage_get
    if _newclass:lsfRusage = property(_lsf.jobStatus2Log_lsfRusage_get, _lsf.jobStatus2Log_lsfRusage_set)
    __swig_setmethods__["numhRusages"] = _lsf.jobStatus2Log_numhRusages_set
    __swig_getmethods__["numhRusages"] = _lsf.jobStatus2Log_numhRusages_get
    if _newclass:numhRusages = property(_lsf.jobStatus2Log_numhRusages_get, _lsf.jobStatus2Log_numhRusages_set)
    __swig_setmethods__["hostRusage"] = _lsf.jobStatus2Log_hostRusage_set
    __swig_getmethods__["hostRusage"] = _lsf.jobStatus2Log_hostRusage_get
    if _newclass:hostRusage = property(_lsf.jobStatus2Log_hostRusage_get, _lsf.jobStatus2Log_hostRusage_set)
    __swig_setmethods__["numExHosts"] = _lsf.jobStatus2Log_numExHosts_set
    __swig_getmethods__["numExHosts"] = _lsf.jobStatus2Log_numExHosts_get
    if _newclass:numExHosts = property(_lsf.jobStatus2Log_numExHosts_get, _lsf.jobStatus2Log_numExHosts_set)
    __swig_setmethods__["execHosts"] = _lsf.jobStatus2Log_execHosts_set
    __swig_getmethods__["execHosts"] = _lsf.jobStatus2Log_execHosts_get
    if _newclass:execHosts = property(_lsf.jobStatus2Log_execHosts_get, _lsf.jobStatus2Log_execHosts_set)
    __swig_setmethods__["slotUsages"] = _lsf.jobStatus2Log_slotUsages_set
    __swig_getmethods__["slotUsages"] = _lsf.jobStatus2Log_slotUsages_get
    if _newclass:slotUsages = property(_lsf.jobStatus2Log_slotUsages_get, _lsf.jobStatus2Log_slotUsages_set)
    __swig_setmethods__["jobRmtAttr"] = _lsf.jobStatus2Log_jobRmtAttr_set
    __swig_getmethods__["jobRmtAttr"] = _lsf.jobStatus2Log_jobRmtAttr_get
    if _newclass:jobRmtAttr = property(_lsf.jobStatus2Log_jobRmtAttr_get, _lsf.jobStatus2Log_jobRmtAttr_set)
    __swig_setmethods__["jgroup"] = _lsf.jobStatus2Log_jgroup_set
    __swig_getmethods__["jgroup"] = _lsf.jobStatus2Log_jgroup_get
    if _newclass:jgroup = property(_lsf.jobStatus2Log_jgroup_get, _lsf.jobStatus2Log_jgroup_set)
    __swig_setmethods__["execRusage"] = _lsf.jobStatus2Log_execRusage_set
    __swig_getmethods__["execRusage"] = _lsf.jobStatus2Log_execRusage_get
    if _newclass:execRusage = property(_lsf.jobStatus2Log_execRusage_get, _lsf.jobStatus2Log_execRusage_set)
    __swig_setmethods__["num_processors"] = _lsf.jobStatus2Log_num_processors_set
    __swig_getmethods__["num_processors"] = _lsf.jobStatus2Log_num_processors_get
    if _newclass:num_processors = property(_lsf.jobStatus2Log_num_processors_get, _lsf.jobStatus2Log_num_processors_set)
    __swig_setmethods__["reason"] = _lsf.jobStatus2Log_reason_set
    __swig_getmethods__["reason"] = _lsf.jobStatus2Log_reason_get
    if _newclass:reason = property(_lsf.jobStatus2Log_reason_get, _lsf.jobStatus2Log_reason_set)
    def __init__(self, *args): 
        this = _lsf.new_jobStatus2Log(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _lsf.delete_jobStatus2Log
    __del__ = lambda self : None;
jobStatus2Log_swigregister = _lsf.jobStatus2Log_swigregister
jobStatus2Log_swigregister(jobStatus2Log)

class jobPendingReasonsLog(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, jobPendingReasonsLog, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, jobPendingReasonsLog, name)
    __repr__ = _swig_repr
    __swig_setmethods__["userName"] = _lsf.jobPendingReasonsLog_userName_set
    __swig_getmethods__["userName"] = _lsf.jobPendingReasonsLog_userName_get
    if _newclass:userName = property(_lsf.jobPendingReasonsLog_userName_get, _lsf.jobPendingReasonsLog_userName_set)
    __swig_setmethods__["queue"] = _lsf.jobPendingReasonsLog_queue_set
    __swig_getmethods__["queue"] = _lsf.jobPendingReasonsLog_queue_get
    if _newclass:queue = property(_lsf.jobPendingReasonsLog_queue_get, _lsf.jobPendingReasonsLog_queue_set)
    __swig_setmethods__["projectName"] = _lsf.jobPendingReasonsLog_projectName_set
    __swig_getmethods__["projectName"] = _lsf.jobPendingReasonsLog_projectName_get
    if _newclass:projectName = property(_lsf.jobPendingReasonsLog_projectName_get, _lsf.jobPendingReasonsLog_projectName_set)
    __swig_setmethods__["licenseProject"] = _lsf.jobPendingReasonsLog_licenseProject_set
    __swig_getmethods__["licenseProject"] = _lsf.jobPendingReasonsLog_licenseProject_get
    if _newclass:licenseProject = property(_lsf.jobPendingReasonsLog_licenseProject_get, _lsf.jobPendingReasonsLog_licenseProject_set)
    __swig_setmethods__["resReq"] = _lsf.jobPendingReasonsLog_resReq_set
    __swig_getmethods__["resReq"] = _lsf.jobPendingReasonsLog_resReq_get
    if _newclass:resReq = property(_lsf.jobPendingReasonsLog_resReq_get, _lsf.jobPendingReasonsLog_resReq_set)
    __swig_setmethods__["app"] = _lsf.jobPendingReasonsLog_app_set
    __swig_getmethods__["app"] = _lsf.jobPendingReasonsLog_app_get
    if _newclass:app = property(_lsf.jobPendingReasonsLog_app_get, _lsf.jobPendingReasonsLog_app_set)
    __swig_setmethods__["num_processors"] = _lsf.jobPendingReasonsLog_num_processors_set
    __swig_getmethods__["num_processors"] = _lsf.jobPendingReasonsLog_num_processors_get
    if _newclass:num_processors = property(_lsf.jobPendingReasonsLog_num_processors_get, _lsf.jobPendingReasonsLog_num_processors_set)
    __swig_setmethods__["mainReason"] = _lsf.jobPendingReasonsLog_mainReason_set
    __swig_getmethods__["mainReason"] = _lsf.jobPendingReasonsLog_mainReason_get
    if _newclass:mainReason = property(_lsf.jobPendingReasonsLog_mainReason_get, _lsf.jobPendingReasonsLog_mainReason_set)
    __swig_setmethods__["subReason"] = _lsf.jobPendingReasonsLog_subReason_set
    __swig_getmethods__["subReason"] = _lsf.jobPendingReasonsLog_subReason_get
    if _newclass:subReason = property(_lsf.jobPendingReasonsLog_subReason_get, _lsf.jobPendingReasonsLog_subReason_set)
    __swig_setmethods__["detailedReason"] = _lsf.jobPendingReasonsLog_detailedReason_set
    __swig_getmethods__["detailedReason"] = _lsf.jobPendingReasonsLog_detailedReason_get
    if _newclass:detailedReason = property(_lsf.jobPendingReasonsLog_detailedReason_get, _lsf.jobPendingReasonsLog_detailedReason_set)
    __swig_setmethods__["detail"] = _lsf.jobPendingReasonsLog_detail_set
    __swig_getmethods__["detail"] = _lsf.jobPendingReasonsLog_detail_get
    if _newclass:detail = property(_lsf.jobPendingReasonsLog_detail_get, _lsf.jobPendingReasonsLog_detail_set)
    __swig_setmethods__["numJobs"] = _lsf.jobPendingReasonsLog_numJobs_set
    __swig_getmethods__["numJobs"] = _lsf.jobPendingReasonsLog_numJobs_get
    if _newclass:numJobs = property(_lsf.jobPendingReasonsLog_numJobs_get, _lsf.jobPendingReasonsLog_numJobs_set)
    __swig_setmethods__["pendingTime"] = _lsf.jobPendingReasonsLog_pendingTime_set
    __swig_getmethods__["pendingTime"] = _lsf.jobPendingReasonsLog_pendingTime_get
    if _newclass:pendingTime = property(_lsf.jobPendingReasonsLog_pendingTime_get, _lsf.jobPendingReasonsLog_pendingTime_set)
    __swig_setmethods__["sumDetailReasonHosts"] = _lsf.jobPendingReasonsLog_sumDetailReasonHosts_set
    __swig_getmethods__["sumDetailReasonHosts"] = _lsf.jobPendingReasonsLog_sumDetailReasonHosts_get
    if _newclass:sumDetailReasonHosts = property(_lsf.jobPendingReasonsLog_sumDetailReasonHosts_get, _lsf.jobPendingReasonsLog_sumDetailReasonHosts_set)
    __swig_setmethods__["averagePendingTime"] = _lsf.jobPendingReasonsLog_averagePendingTime_set
    __swig_getmethods__["averagePendingTime"] = _lsf.jobPendingReasonsLog_averagePendingTime_get
    if _newclass:averagePendingTime = property(_lsf.jobPendingReasonsLog_averagePendingTime_get, _lsf.jobPendingReasonsLog_averagePendingTime_set)
    __swig_setmethods__["currentTime"] = _lsf.jobPendingReasonsLog_currentTime_set
    __swig_getmethods__["currentTime"] = _lsf.jobPendingReasonsLog_currentTime_get
    if _newclass:currentTime = property(_lsf.jobPendingReasonsLog_currentTime_get, _lsf.jobPendingReasonsLog_currentTime_set)
    __swig_setmethods__["sampleInterval"] = _lsf.jobPendingReasonsLog_sampleInterval_set
    __swig_getmethods__["sampleInterval"] = _lsf.jobPendingReasonsLog_sampleInterval_get
    if _newclass:sampleInterval = property(_lsf.jobPendingReasonsLog_sampleInterval_get, _lsf.jobPendingReasonsLog_sampleInterval_set)
    __swig_setmethods__["clusterName"] = _lsf.jobPendingReasonsLog_clusterName_set
    __swig_getmethods__["clusterName"] = _lsf.jobPendingReasonsLog_clusterName_get
    if _newclass:clusterName = property(_lsf.jobPendingReasonsLog_clusterName_get, _lsf.jobPendingReasonsLog_clusterName_set)
    __swig_setmethods__["pendingTimeRanking"] = _lsf.jobPendingReasonsLog_pendingTimeRanking_set
    __swig_getmethods__["pendingTimeRanking"] = _lsf.jobPendingReasonsLog_pendingTimeRanking_get
    if _newclass:pendingTimeRanking = property(_lsf.jobPendingReasonsLog_pendingTimeRanking_get, _lsf.jobPendingReasonsLog_pendingTimeRanking_set)
    __swig_setmethods__["hostType"] = _lsf.jobPendingReasonsLog_hostType_set
    __swig_getmethods__["hostType"] = _lsf.jobPendingReasonsLog_hostType_get
    if _newclass:hostType = property(_lsf.jobPendingReasonsLog_hostType_get, _lsf.jobPendingReasonsLog_hostType_set)
    def __init__(self, *args): 
        this = _lsf.new_jobPendingReasonsLog(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _lsf.delete_jobPendingReasonsLog
    __del__ = lambda self : None;
jobPendingReasonsLog_swigregister = _lsf.jobPendingReasonsLog_swigregister
jobPendingReasonsLog_swigregister(jobPendingReasonsLog)

class loadIndexLog(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, loadIndexLog, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, loadIndexLog, name)
    __repr__ = _swig_repr
    __swig_setmethods__["nIdx"] = _lsf.loadIndexLog_nIdx_set
    __swig_getmethods__["nIdx"] = _lsf.loadIndexLog_nIdx_get
    if _newclass:nIdx = property(_lsf.loadIndexLog_nIdx_get, _lsf.loadIndexLog_nIdx_set)
    __swig_setmethods__["name"] = _lsf.loadIndexLog_name_set
    __swig_getmethods__["name"] = _lsf.loadIndexLog_name_get
    if _newclass:name = property(_lsf.loadIndexLog_name_get, _lsf.loadIndexLog_name_set)
    def __init__(self, *args): 
        this = _lsf.new_loadIndexLog(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _lsf.delete_loadIndexLog
    __del__ = lambda self : None;
loadIndexLog_swigregister = _lsf.loadIndexLog_swigregister
loadIndexLog_swigregister(loadIndexLog)

class calendarLog(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, calendarLog, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, calendarLog, name)
    __repr__ = _swig_repr
    __swig_setmethods__["options"] = _lsf.calendarLog_options_set
    __swig_getmethods__["options"] = _lsf.calendarLog_options_get
    if _newclass:options = property(_lsf.calendarLog_options_get, _lsf.calendarLog_options_set)
    __swig_setmethods__["userId"] = _lsf.calendarLog_userId_set
    __swig_getmethods__["userId"] = _lsf.calendarLog_userId_get
    if _newclass:userId = property(_lsf.calendarLog_userId_get, _lsf.calendarLog_userId_set)
    __swig_setmethods__["name"] = _lsf.calendarLog_name_set
    __swig_getmethods__["name"] = _lsf.calendarLog_name_get
    if _newclass:name = property(_lsf.calendarLog_name_get, _lsf.calendarLog_name_set)
    __swig_setmethods__["desc"] = _lsf.calendarLog_desc_set
    __swig_getmethods__["desc"] = _lsf.calendarLog_desc_get
    if _newclass:desc = property(_lsf.calendarLog_desc_get, _lsf.calendarLog_desc_set)
    __swig_setmethods__["calExpr"] = _lsf.calendarLog_calExpr_set
    __swig_getmethods__["calExpr"] = _lsf.calendarLog_calExpr_get
    if _newclass:calExpr = property(_lsf.calendarLog_calExpr_get, _lsf.calendarLog_calExpr_set)
    def __init__(self, *args): 
        this = _lsf.new_calendarLog(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _lsf.delete_calendarLog
    __del__ = lambda self : None;
calendarLog_swigregister = _lsf.calendarLog_swigregister
calendarLog_swigregister(calendarLog)

class jobForwardLog(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, jobForwardLog, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, jobForwardLog, name)
    __repr__ = _swig_repr
    __swig_setmethods__["jobId"] = _lsf.jobForwardLog_jobId_set
    __swig_getmethods__["jobId"] = _lsf.jobForwardLog_jobId_get
    if _newclass:jobId = property(_lsf.jobForwardLog_jobId_get, _lsf.jobForwardLog_jobId_set)
    __swig_setmethods__["cluster"] = _lsf.jobForwardLog_cluster_set
    __swig_getmethods__["cluster"] = _lsf.jobForwardLog_cluster_get
    if _newclass:cluster = property(_lsf.jobForwardLog_cluster_get, _lsf.jobForwardLog_cluster_set)
    __swig_setmethods__["numReserHosts"] = _lsf.jobForwardLog_numReserHosts_set
    __swig_getmethods__["numReserHosts"] = _lsf.jobForwardLog_numReserHosts_get
    if _newclass:numReserHosts = property(_lsf.jobForwardLog_numReserHosts_get, _lsf.jobForwardLog_numReserHosts_set)
    __swig_setmethods__["reserHosts"] = _lsf.jobForwardLog_reserHosts_set
    __swig_getmethods__["reserHosts"] = _lsf.jobForwardLog_reserHosts_get
    if _newclass:reserHosts = property(_lsf.jobForwardLog_reserHosts_get, _lsf.jobForwardLog_reserHosts_set)
    __swig_setmethods__["idx"] = _lsf.jobForwardLog_idx_set
    __swig_getmethods__["idx"] = _lsf.jobForwardLog_idx_get
    if _newclass:idx = property(_lsf.jobForwardLog_idx_get, _lsf.jobForwardLog_idx_set)
    __swig_setmethods__["jobRmtAttr"] = _lsf.jobForwardLog_jobRmtAttr_set
    __swig_getmethods__["jobRmtAttr"] = _lsf.jobForwardLog_jobRmtAttr_get
    if _newclass:jobRmtAttr = property(_lsf.jobForwardLog_jobRmtAttr_get, _lsf.jobForwardLog_jobRmtAttr_set)
    def __init__(self, *args): 
        this = _lsf.new_jobForwardLog(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _lsf.delete_jobForwardLog
    __del__ = lambda self : None;
jobForwardLog_swigregister = _lsf.jobForwardLog_swigregister
jobForwardLog_swigregister(jobForwardLog)

class jobAcceptLog(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, jobAcceptLog, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, jobAcceptLog, name)
    __repr__ = _swig_repr
    __swig_setmethods__["jobId"] = _lsf.jobAcceptLog_jobId_set
    __swig_getmethods__["jobId"] = _lsf.jobAcceptLog_jobId_get
    if _newclass:jobId = property(_lsf.jobAcceptLog_jobId_get, _lsf.jobAcceptLog_jobId_set)
    __swig_setmethods__["remoteJid"] = _lsf.jobAcceptLog_remoteJid_set
    __swig_getmethods__["remoteJid"] = _lsf.jobAcceptLog_remoteJid_get
    if _newclass:remoteJid = property(_lsf.jobAcceptLog_remoteJid_get, _lsf.jobAcceptLog_remoteJid_set)
    __swig_setmethods__["cluster"] = _lsf.jobAcceptLog_cluster_set
    __swig_getmethods__["cluster"] = _lsf.jobAcceptLog_cluster_get
    if _newclass:cluster = property(_lsf.jobAcceptLog_cluster_get, _lsf.jobAcceptLog_cluster_set)
    __swig_setmethods__["idx"] = _lsf.jobAcceptLog_idx_set
    __swig_getmethods__["idx"] = _lsf.jobAcceptLog_idx_get
    if _newclass:idx = property(_lsf.jobAcceptLog_idx_get, _lsf.jobAcceptLog_idx_set)
    __swig_setmethods__["jobRmtAttr"] = _lsf.jobAcceptLog_jobRmtAttr_set
    __swig_getmethods__["jobRmtAttr"] = _lsf.jobAcceptLog_jobRmtAttr_get
    if _newclass:jobRmtAttr = property(_lsf.jobAcceptLog_jobRmtAttr_get, _lsf.jobAcceptLog_jobRmtAttr_set)
    def __init__(self, *args): 
        this = _lsf.new_jobAcceptLog(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _lsf.delete_jobAcceptLog
    __del__ = lambda self : None;
jobAcceptLog_swigregister = _lsf.jobAcceptLog_swigregister
jobAcceptLog_swigregister(jobAcceptLog)

class statusAckLog(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, statusAckLog, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, statusAckLog, name)
    __repr__ = _swig_repr
    __swig_setmethods__["jobId"] = _lsf.statusAckLog_jobId_set
    __swig_getmethods__["jobId"] = _lsf.statusAckLog_jobId_get
    if _newclass:jobId = property(_lsf.statusAckLog_jobId_get, _lsf.statusAckLog_jobId_set)
    __swig_setmethods__["statusNum"] = _lsf.statusAckLog_statusNum_set
    __swig_getmethods__["statusNum"] = _lsf.statusAckLog_statusNum_get
    if _newclass:statusNum = property(_lsf.statusAckLog_statusNum_get, _lsf.statusAckLog_statusNum_set)
    __swig_setmethods__["idx"] = _lsf.statusAckLog_idx_set
    __swig_getmethods__["idx"] = _lsf.statusAckLog_idx_get
    if _newclass:idx = property(_lsf.statusAckLog_idx_get, _lsf.statusAckLog_idx_set)
    def __init__(self, *args): 
        this = _lsf.new_statusAckLog(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _lsf.delete_statusAckLog
    __del__ = lambda self : None;
statusAckLog_swigregister = _lsf.statusAckLog_swigregister
statusAckLog_swigregister(statusAckLog)

class jobMsgLog(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, jobMsgLog, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, jobMsgLog, name)
    __repr__ = _swig_repr
    __swig_setmethods__["usrId"] = _lsf.jobMsgLog_usrId_set
    __swig_getmethods__["usrId"] = _lsf.jobMsgLog_usrId_get
    if _newclass:usrId = property(_lsf.jobMsgLog_usrId_get, _lsf.jobMsgLog_usrId_set)
    __swig_setmethods__["jobId"] = _lsf.jobMsgLog_jobId_set
    __swig_getmethods__["jobId"] = _lsf.jobMsgLog_jobId_get
    if _newclass:jobId = property(_lsf.jobMsgLog_jobId_get, _lsf.jobMsgLog_jobId_set)
    __swig_setmethods__["msgId"] = _lsf.jobMsgLog_msgId_set
    __swig_getmethods__["msgId"] = _lsf.jobMsgLog_msgId_get
    if _newclass:msgId = property(_lsf.jobMsgLog_msgId_get, _lsf.jobMsgLog_msgId_set)
    __swig_setmethods__["type"] = _lsf.jobMsgLog_type_set
    __swig_getmethods__["type"] = _lsf.jobMsgLog_type_get
    if _newclass:type = property(_lsf.jobMsgLog_type_get, _lsf.jobMsgLog_type_set)
    __swig_setmethods__["src"] = _lsf.jobMsgLog_src_set
    __swig_getmethods__["src"] = _lsf.jobMsgLog_src_get
    if _newclass:src = property(_lsf.jobMsgLog_src_get, _lsf.jobMsgLog_src_set)
    __swig_setmethods__["dest"] = _lsf.jobMsgLog_dest_set
    __swig_getmethods__["dest"] = _lsf.jobMsgLog_dest_get
    if _newclass:dest = property(_lsf.jobMsgLog_dest_get, _lsf.jobMsgLog_dest_set)
    __swig_setmethods__["msg"] = _lsf.jobMsgLog_msg_set
    __swig_getmethods__["msg"] = _lsf.jobMsgLog_msg_get
    if _newclass:msg = property(_lsf.jobMsgLog_msg_get, _lsf.jobMsgLog_msg_set)
    __swig_setmethods__["idx"] = _lsf.jobMsgLog_idx_set
    __swig_getmethods__["idx"] = _lsf.jobMsgLog_idx_get
    if _newclass:idx = property(_lsf.jobMsgLog_idx_get, _lsf.jobMsgLog_idx_set)
    def __init__(self, *args): 
        this = _lsf.new_jobMsgLog(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _lsf.delete_jobMsgLog
    __del__ = lambda self : None;
jobMsgLog_swigregister = _lsf.jobMsgLog_swigregister
jobMsgLog_swigregister(jobMsgLog)

class jobMsgAckLog(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, jobMsgAckLog, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, jobMsgAckLog, name)
    __repr__ = _swig_repr
    __swig_setmethods__["usrId"] = _lsf.jobMsgAckLog_usrId_set
    __swig_getmethods__["usrId"] = _lsf.jobMsgAckLog_usrId_get
    if _newclass:usrId = property(_lsf.jobMsgAckLog_usrId_get, _lsf.jobMsgAckLog_usrId_set)
    __swig_setmethods__["jobId"] = _lsf.jobMsgAckLog_jobId_set
    __swig_getmethods__["jobId"] = _lsf.jobMsgAckLog_jobId_get
    if _newclass:jobId = property(_lsf.jobMsgAckLog_jobId_get, _lsf.jobMsgAckLog_jobId_set)
    __swig_setmethods__["msgId"] = _lsf.jobMsgAckLog_msgId_set
    __swig_getmethods__["msgId"] = _lsf.jobMsgAckLog_msgId_get
    if _newclass:msgId = property(_lsf.jobMsgAckLog_msgId_get, _lsf.jobMsgAckLog_msgId_set)
    __swig_setmethods__["type"] = _lsf.jobMsgAckLog_type_set
    __swig_getmethods__["type"] = _lsf.jobMsgAckLog_type_get
    if _newclass:type = property(_lsf.jobMsgAckLog_type_get, _lsf.jobMsgAckLog_type_set)
    __swig_setmethods__["src"] = _lsf.jobMsgAckLog_src_set
    __swig_getmethods__["src"] = _lsf.jobMsgAckLog_src_get
    if _newclass:src = property(_lsf.jobMsgAckLog_src_get, _lsf.jobMsgAckLog_src_set)
    __swig_setmethods__["dest"] = _lsf.jobMsgAckLog_dest_set
    __swig_getmethods__["dest"] = _lsf.jobMsgAckLog_dest_get
    if _newclass:dest = property(_lsf.jobMsgAckLog_dest_get, _lsf.jobMsgAckLog_dest_set)
    __swig_setmethods__["msg"] = _lsf.jobMsgAckLog_msg_set
    __swig_getmethods__["msg"] = _lsf.jobMsgAckLog_msg_get
    if _newclass:msg = property(_lsf.jobMsgAckLog_msg_get, _lsf.jobMsgAckLog_msg_set)
    __swig_setmethods__["idx"] = _lsf.jobMsgAckLog_idx_set
    __swig_getmethods__["idx"] = _lsf.jobMsgAckLog_idx_get
    if _newclass:idx = property(_lsf.jobMsgAckLog_idx_get, _lsf.jobMsgAckLog_idx_set)
    def __init__(self, *args): 
        this = _lsf.new_jobMsgAckLog(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _lsf.delete_jobMsgAckLog
    __del__ = lambda self : None;
jobMsgAckLog_swigregister = _lsf.jobMsgAckLog_swigregister
jobMsgAckLog_swigregister(jobMsgAckLog)

class jobOccupyReqLog(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, jobOccupyReqLog, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, jobOccupyReqLog, name)
    __repr__ = _swig_repr
    __swig_setmethods__["userId"] = _lsf.jobOccupyReqLog_userId_set
    __swig_getmethods__["userId"] = _lsf.jobOccupyReqLog_userId_get
    if _newclass:userId = property(_lsf.jobOccupyReqLog_userId_get, _lsf.jobOccupyReqLog_userId_set)
    __swig_setmethods__["jobId"] = _lsf.jobOccupyReqLog_jobId_set
    __swig_getmethods__["jobId"] = _lsf.jobOccupyReqLog_jobId_get
    if _newclass:jobId = property(_lsf.jobOccupyReqLog_jobId_get, _lsf.jobOccupyReqLog_jobId_set)
    __swig_setmethods__["numOccupyRequests"] = _lsf.jobOccupyReqLog_numOccupyRequests_set
    __swig_getmethods__["numOccupyRequests"] = _lsf.jobOccupyReqLog_numOccupyRequests_get
    if _newclass:numOccupyRequests = property(_lsf.jobOccupyReqLog_numOccupyRequests_get, _lsf.jobOccupyReqLog_numOccupyRequests_set)
    __swig_setmethods__["occupyReqList"] = _lsf.jobOccupyReqLog_occupyReqList_set
    __swig_getmethods__["occupyReqList"] = _lsf.jobOccupyReqLog_occupyReqList_get
    if _newclass:occupyReqList = property(_lsf.jobOccupyReqLog_occupyReqList_get, _lsf.jobOccupyReqLog_occupyReqList_set)
    __swig_setmethods__["idx"] = _lsf.jobOccupyReqLog_idx_set
    __swig_getmethods__["idx"] = _lsf.jobOccupyReqLog_idx_get
    if _newclass:idx = property(_lsf.jobOccupyReqLog_idx_get, _lsf.jobOccupyReqLog_idx_set)
    __swig_setmethods__["userName"] = _lsf.jobOccupyReqLog_userName_set
    __swig_getmethods__["userName"] = _lsf.jobOccupyReqLog_userName_get
    if _newclass:userName = property(_lsf.jobOccupyReqLog_userName_get, _lsf.jobOccupyReqLog_userName_set)
    def __init__(self, *args): 
        this = _lsf.new_jobOccupyReqLog(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _lsf.delete_jobOccupyReqLog
    __del__ = lambda self : None;
jobOccupyReqLog_swigregister = _lsf.jobOccupyReqLog_swigregister
jobOccupyReqLog_swigregister(jobOccupyReqLog)

class jobVacatedLog(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, jobVacatedLog, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, jobVacatedLog, name)
    __repr__ = _swig_repr
    __swig_setmethods__["userId"] = _lsf.jobVacatedLog_userId_set
    __swig_getmethods__["userId"] = _lsf.jobVacatedLog_userId_get
    if _newclass:userId = property(_lsf.jobVacatedLog_userId_get, _lsf.jobVacatedLog_userId_set)
    __swig_setmethods__["jobId"] = _lsf.jobVacatedLog_jobId_set
    __swig_getmethods__["jobId"] = _lsf.jobVacatedLog_jobId_get
    if _newclass:jobId = property(_lsf.jobVacatedLog_jobId_get, _lsf.jobVacatedLog_jobId_set)
    __swig_setmethods__["idx"] = _lsf.jobVacatedLog_idx_set
    __swig_getmethods__["idx"] = _lsf.jobVacatedLog_idx_get
    if _newclass:idx = property(_lsf.jobVacatedLog_idx_get, _lsf.jobVacatedLog_idx_set)
    __swig_setmethods__["userName"] = _lsf.jobVacatedLog_userName_set
    __swig_getmethods__["userName"] = _lsf.jobVacatedLog_userName_get
    if _newclass:userName = property(_lsf.jobVacatedLog_userName_get, _lsf.jobVacatedLog_userName_set)
    def __init__(self, *args): 
        this = _lsf.new_jobVacatedLog(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _lsf.delete_jobVacatedLog
    __del__ = lambda self : None;
jobVacatedLog_swigregister = _lsf.jobVacatedLog_swigregister
jobVacatedLog_swigregister(jobVacatedLog)

class jobForceRequestLog(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, jobForceRequestLog, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, jobForceRequestLog, name)
    __repr__ = _swig_repr
    __swig_setmethods__["userId"] = _lsf.jobForceRequestLog_userId_set
    __swig_getmethods__["userId"] = _lsf.jobForceRequestLog_userId_get
    if _newclass:userId = property(_lsf.jobForceRequestLog_userId_get, _lsf.jobForceRequestLog_userId_set)
    __swig_setmethods__["numExecHosts"] = _lsf.jobForceRequestLog_numExecHosts_set
    __swig_getmethods__["numExecHosts"] = _lsf.jobForceRequestLog_numExecHosts_get
    if _newclass:numExecHosts = property(_lsf.jobForceRequestLog_numExecHosts_get, _lsf.jobForceRequestLog_numExecHosts_set)
    __swig_setmethods__["execHosts"] = _lsf.jobForceRequestLog_execHosts_set
    __swig_getmethods__["execHosts"] = _lsf.jobForceRequestLog_execHosts_get
    if _newclass:execHosts = property(_lsf.jobForceRequestLog_execHosts_get, _lsf.jobForceRequestLog_execHosts_set)
    __swig_setmethods__["jobId"] = _lsf.jobForceRequestLog_jobId_set
    __swig_getmethods__["jobId"] = _lsf.jobForceRequestLog_jobId_get
    if _newclass:jobId = property(_lsf.jobForceRequestLog_jobId_get, _lsf.jobForceRequestLog_jobId_set)
    __swig_setmethods__["idx"] = _lsf.jobForceRequestLog_idx_set
    __swig_getmethods__["idx"] = _lsf.jobForceRequestLog_idx_get
    if _newclass:idx = property(_lsf.jobForceRequestLog_idx_get, _lsf.jobForceRequestLog_idx_set)
    __swig_setmethods__["options"] = _lsf.jobForceRequestLog_options_set
    __swig_getmethods__["options"] = _lsf.jobForceRequestLog_options_get
    if _newclass:options = property(_lsf.jobForceRequestLog_options_get, _lsf.jobForceRequestLog_options_set)
    __swig_setmethods__["userName"] = _lsf.jobForceRequestLog_userName_set
    __swig_getmethods__["userName"] = _lsf.jobForceRequestLog_userName_get
    if _newclass:userName = property(_lsf.jobForceRequestLog_userName_get, _lsf.jobForceRequestLog_userName_set)
    __swig_setmethods__["queue"] = _lsf.jobForceRequestLog_queue_set
    __swig_getmethods__["queue"] = _lsf.jobForceRequestLog_queue_get
    if _newclass:queue = property(_lsf.jobForceRequestLog_queue_get, _lsf.jobForceRequestLog_queue_set)
    def __init__(self, *args): 
        this = _lsf.new_jobForceRequestLog(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _lsf.delete_jobForceRequestLog
    __del__ = lambda self : None;
jobForceRequestLog_swigregister = _lsf.jobForceRequestLog_swigregister
jobForceRequestLog_swigregister(jobForceRequestLog)

class jobChunkLog(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, jobChunkLog, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, jobChunkLog, name)
    __repr__ = _swig_repr
    __swig_setmethods__["membSize"] = _lsf.jobChunkLog_membSize_set
    __swig_getmethods__["membSize"] = _lsf.jobChunkLog_membSize_get
    if _newclass:membSize = property(_lsf.jobChunkLog_membSize_get, _lsf.jobChunkLog_membSize_set)
    __swig_setmethods__["membJobId"] = _lsf.jobChunkLog_membJobId_set
    __swig_getmethods__["membJobId"] = _lsf.jobChunkLog_membJobId_get
    if _newclass:membJobId = property(_lsf.jobChunkLog_membJobId_get, _lsf.jobChunkLog_membJobId_set)
    __swig_setmethods__["numExHosts"] = _lsf.jobChunkLog_numExHosts_set
    __swig_getmethods__["numExHosts"] = _lsf.jobChunkLog_numExHosts_get
    if _newclass:numExHosts = property(_lsf.jobChunkLog_numExHosts_get, _lsf.jobChunkLog_numExHosts_set)
    __swig_setmethods__["execHosts"] = _lsf.jobChunkLog_execHosts_set
    __swig_getmethods__["execHosts"] = _lsf.jobChunkLog_execHosts_get
    if _newclass:execHosts = property(_lsf.jobChunkLog_execHosts_get, _lsf.jobChunkLog_execHosts_set)
    def __init__(self, *args): 
        this = _lsf.new_jobChunkLog(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _lsf.delete_jobChunkLog
    __del__ = lambda self : None;
jobChunkLog_swigregister = _lsf.jobChunkLog_swigregister
jobChunkLog_swigregister(jobChunkLog)

class jobExternalMsgLog(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, jobExternalMsgLog, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, jobExternalMsgLog, name)
    __repr__ = _swig_repr
    __swig_setmethods__["jobId"] = _lsf.jobExternalMsgLog_jobId_set
    __swig_getmethods__["jobId"] = _lsf.jobExternalMsgLog_jobId_get
    if _newclass:jobId = property(_lsf.jobExternalMsgLog_jobId_get, _lsf.jobExternalMsgLog_jobId_set)
    __swig_setmethods__["idx"] = _lsf.jobExternalMsgLog_idx_set
    __swig_getmethods__["idx"] = _lsf.jobExternalMsgLog_idx_get
    if _newclass:idx = property(_lsf.jobExternalMsgLog_idx_get, _lsf.jobExternalMsgLog_idx_set)
    __swig_setmethods__["msgIdx"] = _lsf.jobExternalMsgLog_msgIdx_set
    __swig_getmethods__["msgIdx"] = _lsf.jobExternalMsgLog_msgIdx_get
    if _newclass:msgIdx = property(_lsf.jobExternalMsgLog_msgIdx_get, _lsf.jobExternalMsgLog_msgIdx_set)
    __swig_setmethods__["desc"] = _lsf.jobExternalMsgLog_desc_set
    __swig_getmethods__["desc"] = _lsf.jobExternalMsgLog_desc_get
    if _newclass:desc = property(_lsf.jobExternalMsgLog_desc_get, _lsf.jobExternalMsgLog_desc_set)
    __swig_setmethods__["userId"] = _lsf.jobExternalMsgLog_userId_set
    __swig_getmethods__["userId"] = _lsf.jobExternalMsgLog_userId_get
    if _newclass:userId = property(_lsf.jobExternalMsgLog_userId_get, _lsf.jobExternalMsgLog_userId_set)
    __swig_setmethods__["dataSize"] = _lsf.jobExternalMsgLog_dataSize_set
    __swig_getmethods__["dataSize"] = _lsf.jobExternalMsgLog_dataSize_get
    if _newclass:dataSize = property(_lsf.jobExternalMsgLog_dataSize_get, _lsf.jobExternalMsgLog_dataSize_set)
    __swig_setmethods__["postTime"] = _lsf.jobExternalMsgLog_postTime_set
    __swig_getmethods__["postTime"] = _lsf.jobExternalMsgLog_postTime_get
    if _newclass:postTime = property(_lsf.jobExternalMsgLog_postTime_get, _lsf.jobExternalMsgLog_postTime_set)
    __swig_setmethods__["dataStatus"] = _lsf.jobExternalMsgLog_dataStatus_set
    __swig_getmethods__["dataStatus"] = _lsf.jobExternalMsgLog_dataStatus_get
    if _newclass:dataStatus = property(_lsf.jobExternalMsgLog_dataStatus_get, _lsf.jobExternalMsgLog_dataStatus_set)
    __swig_setmethods__["fileName"] = _lsf.jobExternalMsgLog_fileName_set
    __swig_getmethods__["fileName"] = _lsf.jobExternalMsgLog_fileName_get
    if _newclass:fileName = property(_lsf.jobExternalMsgLog_fileName_get, _lsf.jobExternalMsgLog_fileName_set)
    __swig_setmethods__["userName"] = _lsf.jobExternalMsgLog_userName_set
    __swig_getmethods__["userName"] = _lsf.jobExternalMsgLog_userName_get
    if _newclass:userName = property(_lsf.jobExternalMsgLog_userName_get, _lsf.jobExternalMsgLog_userName_set)
    def __init__(self, *args): 
        this = _lsf.new_jobExternalMsgLog(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _lsf.delete_jobExternalMsgLog
    __del__ = lambda self : None;
jobExternalMsgLog_swigregister = _lsf.jobExternalMsgLog_swigregister
jobExternalMsgLog_swigregister(jobExternalMsgLog)

class rsvRes(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, rsvRes, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, rsvRes, name)
    __repr__ = _swig_repr
    __swig_setmethods__["resName"] = _lsf.rsvRes_resName_set
    __swig_getmethods__["resName"] = _lsf.rsvRes_resName_get
    if _newclass:resName = property(_lsf.rsvRes_resName_get, _lsf.rsvRes_resName_set)
    __swig_setmethods__["count"] = _lsf.rsvRes_count_set
    __swig_getmethods__["count"] = _lsf.rsvRes_count_get
    if _newclass:count = property(_lsf.rsvRes_count_get, _lsf.rsvRes_count_set)
    __swig_setmethods__["usedAmt"] = _lsf.rsvRes_usedAmt_set
    __swig_getmethods__["usedAmt"] = _lsf.rsvRes_usedAmt_get
    if _newclass:usedAmt = property(_lsf.rsvRes_usedAmt_get, _lsf.rsvRes_usedAmt_set)
    def __init__(self, *args): 
        this = _lsf.new_rsvRes(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _lsf.delete_rsvRes
    __del__ = lambda self : None;
rsvRes_swigregister = _lsf.rsvRes_swigregister
rsvRes_swigregister(rsvRes)

class rsvFinishLog(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, rsvFinishLog, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, rsvFinishLog, name)
    __repr__ = _swig_repr
    __swig_setmethods__["rsvReqTime"] = _lsf.rsvFinishLog_rsvReqTime_set
    __swig_getmethods__["rsvReqTime"] = _lsf.rsvFinishLog_rsvReqTime_get
    if _newclass:rsvReqTime = property(_lsf.rsvFinishLog_rsvReqTime_get, _lsf.rsvFinishLog_rsvReqTime_set)
    __swig_setmethods__["options"] = _lsf.rsvFinishLog_options_set
    __swig_getmethods__["options"] = _lsf.rsvFinishLog_options_get
    if _newclass:options = property(_lsf.rsvFinishLog_options_get, _lsf.rsvFinishLog_options_set)
    __swig_setmethods__["uid"] = _lsf.rsvFinishLog_uid_set
    __swig_getmethods__["uid"] = _lsf.rsvFinishLog_uid_get
    if _newclass:uid = property(_lsf.rsvFinishLog_uid_get, _lsf.rsvFinishLog_uid_set)
    __swig_setmethods__["rsvId"] = _lsf.rsvFinishLog_rsvId_set
    __swig_getmethods__["rsvId"] = _lsf.rsvFinishLog_rsvId_get
    if _newclass:rsvId = property(_lsf.rsvFinishLog_rsvId_get, _lsf.rsvFinishLog_rsvId_set)
    __swig_setmethods__["name"] = _lsf.rsvFinishLog_name_set
    __swig_getmethods__["name"] = _lsf.rsvFinishLog_name_get
    if _newclass:name = property(_lsf.rsvFinishLog_name_get, _lsf.rsvFinishLog_name_set)
    __swig_setmethods__["numReses"] = _lsf.rsvFinishLog_numReses_set
    __swig_getmethods__["numReses"] = _lsf.rsvFinishLog_numReses_get
    if _newclass:numReses = property(_lsf.rsvFinishLog_numReses_get, _lsf.rsvFinishLog_numReses_set)
    __swig_setmethods__["alloc"] = _lsf.rsvFinishLog_alloc_set
    __swig_getmethods__["alloc"] = _lsf.rsvFinishLog_alloc_get
    if _newclass:alloc = property(_lsf.rsvFinishLog_alloc_get, _lsf.rsvFinishLog_alloc_set)
    __swig_setmethods__["timeWindow"] = _lsf.rsvFinishLog_timeWindow_set
    __swig_getmethods__["timeWindow"] = _lsf.rsvFinishLog_timeWindow_get
    if _newclass:timeWindow = property(_lsf.rsvFinishLog_timeWindow_get, _lsf.rsvFinishLog_timeWindow_set)
    __swig_setmethods__["duration"] = _lsf.rsvFinishLog_duration_set
    __swig_getmethods__["duration"] = _lsf.rsvFinishLog_duration_get
    if _newclass:duration = property(_lsf.rsvFinishLog_duration_get, _lsf.rsvFinishLog_duration_set)
    __swig_setmethods__["creator"] = _lsf.rsvFinishLog_creator_set
    __swig_getmethods__["creator"] = _lsf.rsvFinishLog_creator_get
    if _newclass:creator = property(_lsf.rsvFinishLog_creator_get, _lsf.rsvFinishLog_creator_set)
    def __init__(self, *args): 
        this = _lsf.new_rsvFinishLog(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _lsf.delete_rsvFinishLog
    __del__ = lambda self : None;
rsvFinishLog_swigregister = _lsf.rsvFinishLog_swigregister
rsvFinishLog_swigregister(rsvFinishLog)

class cpuProfileLog(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, cpuProfileLog, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, cpuProfileLog, name)
    __repr__ = _swig_repr
    __swig_setmethods__["servicePartition"] = _lsf.cpuProfileLog_servicePartition_set
    __swig_getmethods__["servicePartition"] = _lsf.cpuProfileLog_servicePartition_get
    if _newclass:servicePartition = property(_lsf.cpuProfileLog_servicePartition_get, _lsf.cpuProfileLog_servicePartition_set)
    __swig_setmethods__["slotsRequired"] = _lsf.cpuProfileLog_slotsRequired_set
    __swig_getmethods__["slotsRequired"] = _lsf.cpuProfileLog_slotsRequired_get
    if _newclass:slotsRequired = property(_lsf.cpuProfileLog_slotsRequired_get, _lsf.cpuProfileLog_slotsRequired_set)
    __swig_setmethods__["slotsAllocated"] = _lsf.cpuProfileLog_slotsAllocated_set
    __swig_getmethods__["slotsAllocated"] = _lsf.cpuProfileLog_slotsAllocated_get
    if _newclass:slotsAllocated = property(_lsf.cpuProfileLog_slotsAllocated_get, _lsf.cpuProfileLog_slotsAllocated_set)
    __swig_setmethods__["slotsBorrowed"] = _lsf.cpuProfileLog_slotsBorrowed_set
    __swig_getmethods__["slotsBorrowed"] = _lsf.cpuProfileLog_slotsBorrowed_get
    if _newclass:slotsBorrowed = property(_lsf.cpuProfileLog_slotsBorrowed_get, _lsf.cpuProfileLog_slotsBorrowed_set)
    __swig_setmethods__["slotsLent"] = _lsf.cpuProfileLog_slotsLent_set
    __swig_getmethods__["slotsLent"] = _lsf.cpuProfileLog_slotsLent_get
    if _newclass:slotsLent = property(_lsf.cpuProfileLog_slotsLent_get, _lsf.cpuProfileLog_slotsLent_set)
    def __init__(self, *args): 
        this = _lsf.new_cpuProfileLog(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _lsf.delete_cpuProfileLog
    __del__ = lambda self : None;
cpuProfileLog_swigregister = _lsf.cpuProfileLog_swigregister
cpuProfileLog_swigregister(cpuProfileLog)

class jobResizeNotifyStartLog(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, jobResizeNotifyStartLog, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, jobResizeNotifyStartLog, name)
    __repr__ = _swig_repr
    __swig_setmethods__["jobId"] = _lsf.jobResizeNotifyStartLog_jobId_set
    __swig_getmethods__["jobId"] = _lsf.jobResizeNotifyStartLog_jobId_get
    if _newclass:jobId = property(_lsf.jobResizeNotifyStartLog_jobId_get, _lsf.jobResizeNotifyStartLog_jobId_set)
    __swig_setmethods__["idx"] = _lsf.jobResizeNotifyStartLog_idx_set
    __swig_getmethods__["idx"] = _lsf.jobResizeNotifyStartLog_idx_get
    if _newclass:idx = property(_lsf.jobResizeNotifyStartLog_idx_get, _lsf.jobResizeNotifyStartLog_idx_set)
    __swig_setmethods__["notifyId"] = _lsf.jobResizeNotifyStartLog_notifyId_set
    __swig_getmethods__["notifyId"] = _lsf.jobResizeNotifyStartLog_notifyId_get
    if _newclass:notifyId = property(_lsf.jobResizeNotifyStartLog_notifyId_get, _lsf.jobResizeNotifyStartLog_notifyId_set)
    __swig_setmethods__["numResizeHosts"] = _lsf.jobResizeNotifyStartLog_numResizeHosts_set
    __swig_getmethods__["numResizeHosts"] = _lsf.jobResizeNotifyStartLog_numResizeHosts_get
    if _newclass:numResizeHosts = property(_lsf.jobResizeNotifyStartLog_numResizeHosts_get, _lsf.jobResizeNotifyStartLog_numResizeHosts_set)
    __swig_setmethods__["resizeHosts"] = _lsf.jobResizeNotifyStartLog_resizeHosts_set
    __swig_getmethods__["resizeHosts"] = _lsf.jobResizeNotifyStartLog_resizeHosts_get
    if _newclass:resizeHosts = property(_lsf.jobResizeNotifyStartLog_resizeHosts_get, _lsf.jobResizeNotifyStartLog_resizeHosts_set)
    def __init__(self, *args): 
        this = _lsf.new_jobResizeNotifyStartLog(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _lsf.delete_jobResizeNotifyStartLog
    __del__ = lambda self : None;
jobResizeNotifyStartLog_swigregister = _lsf.jobResizeNotifyStartLog_swigregister
jobResizeNotifyStartLog_swigregister(jobResizeNotifyStartLog)

class jobResizeNotifyAcceptLog(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, jobResizeNotifyAcceptLog, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, jobResizeNotifyAcceptLog, name)
    __repr__ = _swig_repr
    __swig_setmethods__["jobId"] = _lsf.jobResizeNotifyAcceptLog_jobId_set
    __swig_getmethods__["jobId"] = _lsf.jobResizeNotifyAcceptLog_jobId_get
    if _newclass:jobId = property(_lsf.jobResizeNotifyAcceptLog_jobId_get, _lsf.jobResizeNotifyAcceptLog_jobId_set)
    __swig_setmethods__["idx"] = _lsf.jobResizeNotifyAcceptLog_idx_set
    __swig_getmethods__["idx"] = _lsf.jobResizeNotifyAcceptLog_idx_get
    if _newclass:idx = property(_lsf.jobResizeNotifyAcceptLog_idx_get, _lsf.jobResizeNotifyAcceptLog_idx_set)
    __swig_setmethods__["notifyId"] = _lsf.jobResizeNotifyAcceptLog_notifyId_set
    __swig_getmethods__["notifyId"] = _lsf.jobResizeNotifyAcceptLog_notifyId_get
    if _newclass:notifyId = property(_lsf.jobResizeNotifyAcceptLog_notifyId_get, _lsf.jobResizeNotifyAcceptLog_notifyId_set)
    __swig_setmethods__["resizeNotifyCmdPid"] = _lsf.jobResizeNotifyAcceptLog_resizeNotifyCmdPid_set
    __swig_getmethods__["resizeNotifyCmdPid"] = _lsf.jobResizeNotifyAcceptLog_resizeNotifyCmdPid_get
    if _newclass:resizeNotifyCmdPid = property(_lsf.jobResizeNotifyAcceptLog_resizeNotifyCmdPid_get, _lsf.jobResizeNotifyAcceptLog_resizeNotifyCmdPid_set)
    __swig_setmethods__["resizeNotifyCmdPGid"] = _lsf.jobResizeNotifyAcceptLog_resizeNotifyCmdPGid_set
    __swig_getmethods__["resizeNotifyCmdPGid"] = _lsf.jobResizeNotifyAcceptLog_resizeNotifyCmdPGid_get
    if _newclass:resizeNotifyCmdPGid = property(_lsf.jobResizeNotifyAcceptLog_resizeNotifyCmdPGid_get, _lsf.jobResizeNotifyAcceptLog_resizeNotifyCmdPGid_set)
    __swig_setmethods__["status"] = _lsf.jobResizeNotifyAcceptLog_status_set
    __swig_getmethods__["status"] = _lsf.jobResizeNotifyAcceptLog_status_get
    if _newclass:status = property(_lsf.jobResizeNotifyAcceptLog_status_get, _lsf.jobResizeNotifyAcceptLog_status_set)
    def __init__(self, *args): 
        this = _lsf.new_jobResizeNotifyAcceptLog(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _lsf.delete_jobResizeNotifyAcceptLog
    __del__ = lambda self : None;
jobResizeNotifyAcceptLog_swigregister = _lsf.jobResizeNotifyAcceptLog_swigregister
jobResizeNotifyAcceptLog_swigregister(jobResizeNotifyAcceptLog)

class jobResizeNotifyDoneLog(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, jobResizeNotifyDoneLog, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, jobResizeNotifyDoneLog, name)
    __repr__ = _swig_repr
    __swig_setmethods__["jobId"] = _lsf.jobResizeNotifyDoneLog_jobId_set
    __swig_getmethods__["jobId"] = _lsf.jobResizeNotifyDoneLog_jobId_get
    if _newclass:jobId = property(_lsf.jobResizeNotifyDoneLog_jobId_get, _lsf.jobResizeNotifyDoneLog_jobId_set)
    __swig_setmethods__["idx"] = _lsf.jobResizeNotifyDoneLog_idx_set
    __swig_getmethods__["idx"] = _lsf.jobResizeNotifyDoneLog_idx_get
    if _newclass:idx = property(_lsf.jobResizeNotifyDoneLog_idx_get, _lsf.jobResizeNotifyDoneLog_idx_set)
    __swig_setmethods__["notifyId"] = _lsf.jobResizeNotifyDoneLog_notifyId_set
    __swig_getmethods__["notifyId"] = _lsf.jobResizeNotifyDoneLog_notifyId_get
    if _newclass:notifyId = property(_lsf.jobResizeNotifyDoneLog_notifyId_get, _lsf.jobResizeNotifyDoneLog_notifyId_set)
    __swig_setmethods__["status"] = _lsf.jobResizeNotifyDoneLog_status_set
    __swig_getmethods__["status"] = _lsf.jobResizeNotifyDoneLog_status_get
    if _newclass:status = property(_lsf.jobResizeNotifyDoneLog_status_get, _lsf.jobResizeNotifyDoneLog_status_set)
    def __init__(self, *args): 
        this = _lsf.new_jobResizeNotifyDoneLog(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _lsf.delete_jobResizeNotifyDoneLog
    __del__ = lambda self : None;
jobResizeNotifyDoneLog_swigregister = _lsf.jobResizeNotifyDoneLog_swigregister
jobResizeNotifyDoneLog_swigregister(jobResizeNotifyDoneLog)

class jobResizeReleaseLog(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, jobResizeReleaseLog, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, jobResizeReleaseLog, name)
    __repr__ = _swig_repr
    __swig_setmethods__["jobId"] = _lsf.jobResizeReleaseLog_jobId_set
    __swig_getmethods__["jobId"] = _lsf.jobResizeReleaseLog_jobId_get
    if _newclass:jobId = property(_lsf.jobResizeReleaseLog_jobId_get, _lsf.jobResizeReleaseLog_jobId_set)
    __swig_setmethods__["idx"] = _lsf.jobResizeReleaseLog_idx_set
    __swig_getmethods__["idx"] = _lsf.jobResizeReleaseLog_idx_get
    if _newclass:idx = property(_lsf.jobResizeReleaseLog_idx_get, _lsf.jobResizeReleaseLog_idx_set)
    __swig_setmethods__["reqId"] = _lsf.jobResizeReleaseLog_reqId_set
    __swig_getmethods__["reqId"] = _lsf.jobResizeReleaseLog_reqId_get
    if _newclass:reqId = property(_lsf.jobResizeReleaseLog_reqId_get, _lsf.jobResizeReleaseLog_reqId_set)
    __swig_setmethods__["options"] = _lsf.jobResizeReleaseLog_options_set
    __swig_getmethods__["options"] = _lsf.jobResizeReleaseLog_options_get
    if _newclass:options = property(_lsf.jobResizeReleaseLog_options_get, _lsf.jobResizeReleaseLog_options_set)
    __swig_setmethods__["userId"] = _lsf.jobResizeReleaseLog_userId_set
    __swig_getmethods__["userId"] = _lsf.jobResizeReleaseLog_userId_get
    if _newclass:userId = property(_lsf.jobResizeReleaseLog_userId_get, _lsf.jobResizeReleaseLog_userId_set)
    __swig_setmethods__["userName"] = _lsf.jobResizeReleaseLog_userName_set
    __swig_getmethods__["userName"] = _lsf.jobResizeReleaseLog_userName_get
    if _newclass:userName = property(_lsf.jobResizeReleaseLog_userName_get, _lsf.jobResizeReleaseLog_userName_set)
    __swig_setmethods__["resizeNotifyCmd"] = _lsf.jobResizeReleaseLog_resizeNotifyCmd_set
    __swig_getmethods__["resizeNotifyCmd"] = _lsf.jobResizeReleaseLog_resizeNotifyCmd_get
    if _newclass:resizeNotifyCmd = property(_lsf.jobResizeReleaseLog_resizeNotifyCmd_get, _lsf.jobResizeReleaseLog_resizeNotifyCmd_set)
    __swig_setmethods__["numResizeHosts"] = _lsf.jobResizeReleaseLog_numResizeHosts_set
    __swig_getmethods__["numResizeHosts"] = _lsf.jobResizeReleaseLog_numResizeHosts_get
    if _newclass:numResizeHosts = property(_lsf.jobResizeReleaseLog_numResizeHosts_get, _lsf.jobResizeReleaseLog_numResizeHosts_set)
    __swig_setmethods__["resizeHosts"] = _lsf.jobResizeReleaseLog_resizeHosts_set
    __swig_getmethods__["resizeHosts"] = _lsf.jobResizeReleaseLog_resizeHosts_get
    if _newclass:resizeHosts = property(_lsf.jobResizeReleaseLog_resizeHosts_get, _lsf.jobResizeReleaseLog_resizeHosts_set)
    def __init__(self, *args): 
        this = _lsf.new_jobResizeReleaseLog(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _lsf.delete_jobResizeReleaseLog
    __del__ = lambda self : None;
jobResizeReleaseLog_swigregister = _lsf.jobResizeReleaseLog_swigregister
jobResizeReleaseLog_swigregister(jobResizeReleaseLog)

class jobResizeCancelLog(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, jobResizeCancelLog, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, jobResizeCancelLog, name)
    __repr__ = _swig_repr
    __swig_setmethods__["jobId"] = _lsf.jobResizeCancelLog_jobId_set
    __swig_getmethods__["jobId"] = _lsf.jobResizeCancelLog_jobId_get
    if _newclass:jobId = property(_lsf.jobResizeCancelLog_jobId_get, _lsf.jobResizeCancelLog_jobId_set)
    __swig_setmethods__["idx"] = _lsf.jobResizeCancelLog_idx_set
    __swig_getmethods__["idx"] = _lsf.jobResizeCancelLog_idx_get
    if _newclass:idx = property(_lsf.jobResizeCancelLog_idx_get, _lsf.jobResizeCancelLog_idx_set)
    __swig_setmethods__["userId"] = _lsf.jobResizeCancelLog_userId_set
    __swig_getmethods__["userId"] = _lsf.jobResizeCancelLog_userId_get
    if _newclass:userId = property(_lsf.jobResizeCancelLog_userId_get, _lsf.jobResizeCancelLog_userId_set)
    __swig_setmethods__["userName"] = _lsf.jobResizeCancelLog_userName_set
    __swig_getmethods__["userName"] = _lsf.jobResizeCancelLog_userName_get
    if _newclass:userName = property(_lsf.jobResizeCancelLog_userName_get, _lsf.jobResizeCancelLog_userName_set)
    def __init__(self, *args): 
        this = _lsf.new_jobResizeCancelLog(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _lsf.delete_jobResizeCancelLog
    __del__ = lambda self : None;
jobResizeCancelLog_swigregister = _lsf.jobResizeCancelLog_swigregister
jobResizeCancelLog_swigregister(jobResizeCancelLog)

class jobRunRusageLog(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, jobRunRusageLog, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, jobRunRusageLog, name)
    __repr__ = _swig_repr
    __swig_setmethods__["jobid"] = _lsf.jobRunRusageLog_jobid_set
    __swig_getmethods__["jobid"] = _lsf.jobRunRusageLog_jobid_get
    if _newclass:jobid = property(_lsf.jobRunRusageLog_jobid_get, _lsf.jobRunRusageLog_jobid_set)
    __swig_setmethods__["idx"] = _lsf.jobRunRusageLog_idx_set
    __swig_getmethods__["idx"] = _lsf.jobRunRusageLog_idx_get
    if _newclass:idx = property(_lsf.jobRunRusageLog_idx_get, _lsf.jobRunRusageLog_idx_set)
    __swig_setmethods__["jrusage"] = _lsf.jobRunRusageLog_jrusage_set
    __swig_getmethods__["jrusage"] = _lsf.jobRunRusageLog_jrusage_get
    if _newclass:jrusage = property(_lsf.jobRunRusageLog_jrusage_get, _lsf.jobRunRusageLog_jrusage_set)
    def __init__(self, *args): 
        this = _lsf.new_jobRunRusageLog(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _lsf.delete_jobRunRusageLog
    __del__ = lambda self : None;
jobRunRusageLog_swigregister = _lsf.jobRunRusageLog_swigregister
jobRunRusageLog_swigregister(jobRunRusageLog)

class slaLog(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, slaLog, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, slaLog, name)
    __repr__ = _swig_repr
    __swig_setmethods__["name"] = _lsf.slaLog_name_set
    __swig_getmethods__["name"] = _lsf.slaLog_name_get
    if _newclass:name = property(_lsf.slaLog_name_get, _lsf.slaLog_name_set)
    __swig_setmethods__["consumer"] = _lsf.slaLog_consumer_set
    __swig_getmethods__["consumer"] = _lsf.slaLog_consumer_get
    if _newclass:consumer = property(_lsf.slaLog_consumer_get, _lsf.slaLog_consumer_set)
    __swig_setmethods__["goaltype"] = _lsf.slaLog_goaltype_set
    __swig_getmethods__["goaltype"] = _lsf.slaLog_goaltype_get
    if _newclass:goaltype = property(_lsf.slaLog_goaltype_get, _lsf.slaLog_goaltype_set)
    __swig_setmethods__["state"] = _lsf.slaLog_state_set
    __swig_getmethods__["state"] = _lsf.slaLog_state_get
    if _newclass:state = property(_lsf.slaLog_state_get, _lsf.slaLog_state_set)
    __swig_setmethods__["optimum"] = _lsf.slaLog_optimum_set
    __swig_getmethods__["optimum"] = _lsf.slaLog_optimum_get
    if _newclass:optimum = property(_lsf.slaLog_optimum_get, _lsf.slaLog_optimum_set)
    __swig_setmethods__["counters"] = _lsf.slaLog_counters_set
    __swig_getmethods__["counters"] = _lsf.slaLog_counters_get
    if _newclass:counters = property(_lsf.slaLog_counters_get, _lsf.slaLog_counters_set)
    def __init__(self, *args): 
        this = _lsf.new_slaLog(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _lsf.delete_slaLog
    __del__ = lambda self : None;
slaLog_swigregister = _lsf.slaLog_swigregister
slaLog_swigregister(slaLog)

class perfmonLogInfo(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, perfmonLogInfo, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, perfmonLogInfo, name)
    __repr__ = _swig_repr
    __swig_setmethods__["samplePeriod"] = _lsf.perfmonLogInfo_samplePeriod_set
    __swig_getmethods__["samplePeriod"] = _lsf.perfmonLogInfo_samplePeriod_get
    if _newclass:samplePeriod = property(_lsf.perfmonLogInfo_samplePeriod_get, _lsf.perfmonLogInfo_samplePeriod_set)
    __swig_setmethods__["metrics"] = _lsf.perfmonLogInfo_metrics_set
    __swig_getmethods__["metrics"] = _lsf.perfmonLogInfo_metrics_get
    if _newclass:metrics = property(_lsf.perfmonLogInfo_metrics_get, _lsf.perfmonLogInfo_metrics_set)
    __swig_setmethods__["startTime"] = _lsf.perfmonLogInfo_startTime_set
    __swig_getmethods__["startTime"] = _lsf.perfmonLogInfo_startTime_get
    if _newclass:startTime = property(_lsf.perfmonLogInfo_startTime_get, _lsf.perfmonLogInfo_startTime_set)
    __swig_setmethods__["logTime"] = _lsf.perfmonLogInfo_logTime_set
    __swig_getmethods__["logTime"] = _lsf.perfmonLogInfo_logTime_get
    if _newclass:logTime = property(_lsf.perfmonLogInfo_logTime_get, _lsf.perfmonLogInfo_logTime_set)
    def __init__(self, *args): 
        this = _lsf.new_perfmonLogInfo(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _lsf.delete_perfmonLogInfo
    __del__ = lambda self : None;
perfmonLogInfo_swigregister = _lsf.perfmonLogInfo_swigregister
perfmonLogInfo_swigregister(perfmonLogInfo)

class perfmonLog(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, perfmonLog, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, perfmonLog, name)
    __repr__ = _swig_repr
    __swig_setmethods__["samplePeriod"] = _lsf.perfmonLog_samplePeriod_set
    __swig_getmethods__["samplePeriod"] = _lsf.perfmonLog_samplePeriod_get
    if _newclass:samplePeriod = property(_lsf.perfmonLog_samplePeriod_get, _lsf.perfmonLog_samplePeriod_set)
    __swig_setmethods__["totalQueries"] = _lsf.perfmonLog_totalQueries_set
    __swig_getmethods__["totalQueries"] = _lsf.perfmonLog_totalQueries_get
    if _newclass:totalQueries = property(_lsf.perfmonLog_totalQueries_get, _lsf.perfmonLog_totalQueries_set)
    __swig_setmethods__["jobQuries"] = _lsf.perfmonLog_jobQuries_set
    __swig_getmethods__["jobQuries"] = _lsf.perfmonLog_jobQuries_get
    if _newclass:jobQuries = property(_lsf.perfmonLog_jobQuries_get, _lsf.perfmonLog_jobQuries_set)
    __swig_setmethods__["queueQuries"] = _lsf.perfmonLog_queueQuries_set
    __swig_getmethods__["queueQuries"] = _lsf.perfmonLog_queueQuries_get
    if _newclass:queueQuries = property(_lsf.perfmonLog_queueQuries_get, _lsf.perfmonLog_queueQuries_set)
    __swig_setmethods__["hostQuries"] = _lsf.perfmonLog_hostQuries_set
    __swig_getmethods__["hostQuries"] = _lsf.perfmonLog_hostQuries_get
    if _newclass:hostQuries = property(_lsf.perfmonLog_hostQuries_get, _lsf.perfmonLog_hostQuries_set)
    __swig_setmethods__["submissionRequest"] = _lsf.perfmonLog_submissionRequest_set
    __swig_getmethods__["submissionRequest"] = _lsf.perfmonLog_submissionRequest_get
    if _newclass:submissionRequest = property(_lsf.perfmonLog_submissionRequest_get, _lsf.perfmonLog_submissionRequest_set)
    __swig_setmethods__["jobSubmitted"] = _lsf.perfmonLog_jobSubmitted_set
    __swig_getmethods__["jobSubmitted"] = _lsf.perfmonLog_jobSubmitted_get
    if _newclass:jobSubmitted = property(_lsf.perfmonLog_jobSubmitted_get, _lsf.perfmonLog_jobSubmitted_set)
    __swig_setmethods__["dispatchedjobs"] = _lsf.perfmonLog_dispatchedjobs_set
    __swig_getmethods__["dispatchedjobs"] = _lsf.perfmonLog_dispatchedjobs_get
    if _newclass:dispatchedjobs = property(_lsf.perfmonLog_dispatchedjobs_get, _lsf.perfmonLog_dispatchedjobs_set)
    __swig_setmethods__["jobcompleted"] = _lsf.perfmonLog_jobcompleted_set
    __swig_getmethods__["jobcompleted"] = _lsf.perfmonLog_jobcompleted_get
    if _newclass:jobcompleted = property(_lsf.perfmonLog_jobcompleted_get, _lsf.perfmonLog_jobcompleted_set)
    __swig_setmethods__["jobMCSend"] = _lsf.perfmonLog_jobMCSend_set
    __swig_getmethods__["jobMCSend"] = _lsf.perfmonLog_jobMCSend_get
    if _newclass:jobMCSend = property(_lsf.perfmonLog_jobMCSend_get, _lsf.perfmonLog_jobMCSend_set)
    __swig_setmethods__["jobMCReceive"] = _lsf.perfmonLog_jobMCReceive_set
    __swig_getmethods__["jobMCReceive"] = _lsf.perfmonLog_jobMCReceive_get
    if _newclass:jobMCReceive = property(_lsf.perfmonLog_jobMCReceive_get, _lsf.perfmonLog_jobMCReceive_set)
    __swig_setmethods__["startTime"] = _lsf.perfmonLog_startTime_set
    __swig_getmethods__["startTime"] = _lsf.perfmonLog_startTime_get
    if _newclass:startTime = property(_lsf.perfmonLog_startTime_get, _lsf.perfmonLog_startTime_set)
    def __init__(self, *args): 
        this = _lsf.new_perfmonLog(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _lsf.delete_perfmonLog
    __del__ = lambda self : None;
perfmonLog_swigregister = _lsf.perfmonLog_swigregister
perfmonLog_swigregister(perfmonLog)

class taskFinishLog(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, taskFinishLog, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, taskFinishLog, name)
    __repr__ = _swig_repr
    __swig_setmethods__["jobFinishLog"] = _lsf.taskFinishLog_jobFinishLog_set
    __swig_getmethods__["jobFinishLog"] = _lsf.taskFinishLog_jobFinishLog_get
    if _newclass:jobFinishLog = property(_lsf.taskFinishLog_jobFinishLog_get, _lsf.taskFinishLog_jobFinishLog_set)
    __swig_setmethods__["taskId"] = _lsf.taskFinishLog_taskId_set
    __swig_getmethods__["taskId"] = _lsf.taskFinishLog_taskId_get
    if _newclass:taskId = property(_lsf.taskFinishLog_taskId_get, _lsf.taskFinishLog_taskId_set)
    __swig_setmethods__["taskIdx"] = _lsf.taskFinishLog_taskIdx_set
    __swig_getmethods__["taskIdx"] = _lsf.taskFinishLog_taskIdx_get
    if _newclass:taskIdx = property(_lsf.taskFinishLog_taskIdx_get, _lsf.taskFinishLog_taskIdx_set)
    __swig_setmethods__["taskName"] = _lsf.taskFinishLog_taskName_set
    __swig_getmethods__["taskName"] = _lsf.taskFinishLog_taskName_get
    if _newclass:taskName = property(_lsf.taskFinishLog_taskName_get, _lsf.taskFinishLog_taskName_set)
    __swig_setmethods__["taskOptions"] = _lsf.taskFinishLog_taskOptions_set
    __swig_getmethods__["taskOptions"] = _lsf.taskFinishLog_taskOptions_get
    if _newclass:taskOptions = property(_lsf.taskFinishLog_taskOptions_get, _lsf.taskFinishLog_taskOptions_set)
    __swig_setmethods__["taskExitReason"] = _lsf.taskFinishLog_taskExitReason_set
    __swig_getmethods__["taskExitReason"] = _lsf.taskFinishLog_taskExitReason_get
    if _newclass:taskExitReason = property(_lsf.taskFinishLog_taskExitReason_get, _lsf.taskFinishLog_taskExitReason_set)
    def __init__(self, *args): 
        this = _lsf.new_taskFinishLog(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _lsf.delete_taskFinishLog
    __del__ = lambda self : None;
taskFinishLog_swigregister = _lsf.taskFinishLog_swigregister
taskFinishLog_swigregister(taskFinishLog)

class eventEOSLog(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, eventEOSLog, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, eventEOSLog, name)
    __repr__ = _swig_repr
    __swig_setmethods__["eos"] = _lsf.eventEOSLog_eos_set
    __swig_getmethods__["eos"] = _lsf.eventEOSLog_eos_get
    if _newclass:eos = property(_lsf.eventEOSLog_eos_get, _lsf.eventEOSLog_eos_set)
    def __init__(self, *args): 
        this = _lsf.new_eventEOSLog(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _lsf.delete_eventEOSLog
    __del__ = lambda self : None;
eventEOSLog_swigregister = _lsf.eventEOSLog_swigregister
eventEOSLog_swigregister(eventEOSLog)

class jobResizeLog(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, jobResizeLog, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, jobResizeLog, name)
    __repr__ = _swig_repr
    __swig_setmethods__["jobId"] = _lsf.jobResizeLog_jobId_set
    __swig_getmethods__["jobId"] = _lsf.jobResizeLog_jobId_get
    if _newclass:jobId = property(_lsf.jobResizeLog_jobId_get, _lsf.jobResizeLog_jobId_set)
    __swig_setmethods__["idx"] = _lsf.jobResizeLog_idx_set
    __swig_getmethods__["idx"] = _lsf.jobResizeLog_idx_get
    if _newclass:idx = property(_lsf.jobResizeLog_idx_get, _lsf.jobResizeLog_idx_set)
    __swig_setmethods__["startTime"] = _lsf.jobResizeLog_startTime_set
    __swig_getmethods__["startTime"] = _lsf.jobResizeLog_startTime_get
    if _newclass:startTime = property(_lsf.jobResizeLog_startTime_get, _lsf.jobResizeLog_startTime_set)
    __swig_setmethods__["userId"] = _lsf.jobResizeLog_userId_set
    __swig_getmethods__["userId"] = _lsf.jobResizeLog_userId_get
    if _newclass:userId = property(_lsf.jobResizeLog_userId_get, _lsf.jobResizeLog_userId_set)
    __swig_setmethods__["userName"] = _lsf.jobResizeLog_userName_set
    __swig_getmethods__["userName"] = _lsf.jobResizeLog_userName_get
    if _newclass:userName = property(_lsf.jobResizeLog_userName_get, _lsf.jobResizeLog_userName_set)
    __swig_setmethods__["resizeType"] = _lsf.jobResizeLog_resizeType_set
    __swig_getmethods__["resizeType"] = _lsf.jobResizeLog_resizeType_get
    if _newclass:resizeType = property(_lsf.jobResizeLog_resizeType_get, _lsf.jobResizeLog_resizeType_set)
    __swig_setmethods__["lastResizeStartTime"] = _lsf.jobResizeLog_lastResizeStartTime_set
    __swig_getmethods__["lastResizeStartTime"] = _lsf.jobResizeLog_lastResizeStartTime_get
    if _newclass:lastResizeStartTime = property(_lsf.jobResizeLog_lastResizeStartTime_get, _lsf.jobResizeLog_lastResizeStartTime_set)
    __swig_setmethods__["lastResizeFinishTime"] = _lsf.jobResizeLog_lastResizeFinishTime_set
    __swig_getmethods__["lastResizeFinishTime"] = _lsf.jobResizeLog_lastResizeFinishTime_get
    if _newclass:lastResizeFinishTime = property(_lsf.jobResizeLog_lastResizeFinishTime_get, _lsf.jobResizeLog_lastResizeFinishTime_set)
    __swig_setmethods__["numExecHosts"] = _lsf.jobResizeLog_numExecHosts_set
    __swig_getmethods__["numExecHosts"] = _lsf.jobResizeLog_numExecHosts_get
    if _newclass:numExecHosts = property(_lsf.jobResizeLog_numExecHosts_get, _lsf.jobResizeLog_numExecHosts_set)
    __swig_setmethods__["execHosts"] = _lsf.jobResizeLog_execHosts_set
    __swig_getmethods__["execHosts"] = _lsf.jobResizeLog_execHosts_get
    if _newclass:execHosts = property(_lsf.jobResizeLog_execHosts_get, _lsf.jobResizeLog_execHosts_set)
    __swig_setmethods__["numResizeHosts"] = _lsf.jobResizeLog_numResizeHosts_set
    __swig_getmethods__["numResizeHosts"] = _lsf.jobResizeLog_numResizeHosts_get
    if _newclass:numResizeHosts = property(_lsf.jobResizeLog_numResizeHosts_get, _lsf.jobResizeLog_numResizeHosts_set)
    __swig_setmethods__["resizeHosts"] = _lsf.jobResizeLog_resizeHosts_set
    __swig_getmethods__["resizeHosts"] = _lsf.jobResizeLog_resizeHosts_get
    if _newclass:resizeHosts = property(_lsf.jobResizeLog_resizeHosts_get, _lsf.jobResizeLog_resizeHosts_set)
    def __init__(self, *args): 
        this = _lsf.new_jobResizeLog(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _lsf.delete_jobResizeLog
    __del__ = lambda self : None;
jobResizeLog_swigregister = _lsf.jobResizeLog_swigregister
jobResizeLog_swigregister(jobResizeLog)

class eventLog(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, eventLog, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, eventLog, name)
    __repr__ = _swig_repr
    __swig_setmethods__["jobNewLog"] = _lsf.eventLog_jobNewLog_set
    __swig_getmethods__["jobNewLog"] = _lsf.eventLog_jobNewLog_get
    if _newclass:jobNewLog = property(_lsf.eventLog_jobNewLog_get, _lsf.eventLog_jobNewLog_set)
    __swig_setmethods__["jobStartLog"] = _lsf.eventLog_jobStartLog_set
    __swig_getmethods__["jobStartLog"] = _lsf.eventLog_jobStartLog_get
    if _newclass:jobStartLog = property(_lsf.eventLog_jobStartLog_get, _lsf.eventLog_jobStartLog_set)
    __swig_setmethods__["jobStatusLog"] = _lsf.eventLog_jobStatusLog_set
    __swig_getmethods__["jobStatusLog"] = _lsf.eventLog_jobStatusLog_get
    if _newclass:jobStatusLog = property(_lsf.eventLog_jobStatusLog_get, _lsf.eventLog_jobStatusLog_set)
    __swig_setmethods__["sbdJobStatusLog"] = _lsf.eventLog_sbdJobStatusLog_set
    __swig_getmethods__["sbdJobStatusLog"] = _lsf.eventLog_sbdJobStatusLog_get
    if _newclass:sbdJobStatusLog = property(_lsf.eventLog_sbdJobStatusLog_get, _lsf.eventLog_sbdJobStatusLog_set)
    __swig_setmethods__["jobSwitchLog"] = _lsf.eventLog_jobSwitchLog_set
    __swig_getmethods__["jobSwitchLog"] = _lsf.eventLog_jobSwitchLog_get
    if _newclass:jobSwitchLog = property(_lsf.eventLog_jobSwitchLog_get, _lsf.eventLog_jobSwitchLog_set)
    __swig_setmethods__["jobMoveLog"] = _lsf.eventLog_jobMoveLog_set
    __swig_getmethods__["jobMoveLog"] = _lsf.eventLog_jobMoveLog_get
    if _newclass:jobMoveLog = property(_lsf.eventLog_jobMoveLog_get, _lsf.eventLog_jobMoveLog_set)
    __swig_setmethods__["queueCtrlLog"] = _lsf.eventLog_queueCtrlLog_set
    __swig_getmethods__["queueCtrlLog"] = _lsf.eventLog_queueCtrlLog_get
    if _newclass:queueCtrlLog = property(_lsf.eventLog_queueCtrlLog_get, _lsf.eventLog_queueCtrlLog_set)
    __swig_setmethods__["newDebugLog"] = _lsf.eventLog_newDebugLog_set
    __swig_getmethods__["newDebugLog"] = _lsf.eventLog_newDebugLog_get
    if _newclass:newDebugLog = property(_lsf.eventLog_newDebugLog_get, _lsf.eventLog_newDebugLog_set)
    __swig_setmethods__["hostCtrlLog"] = _lsf.eventLog_hostCtrlLog_set
    __swig_getmethods__["hostCtrlLog"] = _lsf.eventLog_hostCtrlLog_get
    if _newclass:hostCtrlLog = property(_lsf.eventLog_hostCtrlLog_get, _lsf.eventLog_hostCtrlLog_set)
    __swig_setmethods__["mbdStartLog"] = _lsf.eventLog_mbdStartLog_set
    __swig_getmethods__["mbdStartLog"] = _lsf.eventLog_mbdStartLog_get
    if _newclass:mbdStartLog = property(_lsf.eventLog_mbdStartLog_get, _lsf.eventLog_mbdStartLog_set)
    __swig_setmethods__["mbdDieLog"] = _lsf.eventLog_mbdDieLog_set
    __swig_getmethods__["mbdDieLog"] = _lsf.eventLog_mbdDieLog_get
    if _newclass:mbdDieLog = property(_lsf.eventLog_mbdDieLog_get, _lsf.eventLog_mbdDieLog_set)
    __swig_setmethods__["unfulfillLog"] = _lsf.eventLog_unfulfillLog_set
    __swig_getmethods__["unfulfillLog"] = _lsf.eventLog_unfulfillLog_get
    if _newclass:unfulfillLog = property(_lsf.eventLog_unfulfillLog_get, _lsf.eventLog_unfulfillLog_set)
    __swig_setmethods__["jobFinishLog"] = _lsf.eventLog_jobFinishLog_set
    __swig_getmethods__["jobFinishLog"] = _lsf.eventLog_jobFinishLog_get
    if _newclass:jobFinishLog = property(_lsf.eventLog_jobFinishLog_get, _lsf.eventLog_jobFinishLog_set)
    __swig_setmethods__["loadIndexLog"] = _lsf.eventLog_loadIndexLog_set
    __swig_getmethods__["loadIndexLog"] = _lsf.eventLog_loadIndexLog_get
    if _newclass:loadIndexLog = property(_lsf.eventLog_loadIndexLog_get, _lsf.eventLog_loadIndexLog_set)
    __swig_setmethods__["migLog"] = _lsf.eventLog_migLog_set
    __swig_getmethods__["migLog"] = _lsf.eventLog_migLog_get
    if _newclass:migLog = property(_lsf.eventLog_migLog_get, _lsf.eventLog_migLog_set)
    __swig_setmethods__["calendarLog"] = _lsf.eventLog_calendarLog_set
    __swig_getmethods__["calendarLog"] = _lsf.eventLog_calendarLog_get
    if _newclass:calendarLog = property(_lsf.eventLog_calendarLog_get, _lsf.eventLog_calendarLog_set)
    __swig_setmethods__["jobForwardLog"] = _lsf.eventLog_jobForwardLog_set
    __swig_getmethods__["jobForwardLog"] = _lsf.eventLog_jobForwardLog_get
    if _newclass:jobForwardLog = property(_lsf.eventLog_jobForwardLog_get, _lsf.eventLog_jobForwardLog_set)
    __swig_setmethods__["jobAcceptLog"] = _lsf.eventLog_jobAcceptLog_set
    __swig_getmethods__["jobAcceptLog"] = _lsf.eventLog_jobAcceptLog_get
    if _newclass:jobAcceptLog = property(_lsf.eventLog_jobAcceptLog_get, _lsf.eventLog_jobAcceptLog_set)
    __swig_setmethods__["statusAckLog"] = _lsf.eventLog_statusAckLog_set
    __swig_getmethods__["statusAckLog"] = _lsf.eventLog_statusAckLog_get
    if _newclass:statusAckLog = property(_lsf.eventLog_statusAckLog_get, _lsf.eventLog_statusAckLog_set)
    __swig_setmethods__["signalLog"] = _lsf.eventLog_signalLog_set
    __swig_getmethods__["signalLog"] = _lsf.eventLog_signalLog_get
    if _newclass:signalLog = property(_lsf.eventLog_signalLog_get, _lsf.eventLog_signalLog_set)
    __swig_setmethods__["jobExecuteLog"] = _lsf.eventLog_jobExecuteLog_set
    __swig_getmethods__["jobExecuteLog"] = _lsf.eventLog_jobExecuteLog_get
    if _newclass:jobExecuteLog = property(_lsf.eventLog_jobExecuteLog_get, _lsf.eventLog_jobExecuteLog_set)
    __swig_setmethods__["jobMsgLog"] = _lsf.eventLog_jobMsgLog_set
    __swig_getmethods__["jobMsgLog"] = _lsf.eventLog_jobMsgLog_get
    if _newclass:jobMsgLog = property(_lsf.eventLog_jobMsgLog_get, _lsf.eventLog_jobMsgLog_set)
    __swig_setmethods__["jobMsgAckLog"] = _lsf.eventLog_jobMsgAckLog_set
    __swig_getmethods__["jobMsgAckLog"] = _lsf.eventLog_jobMsgAckLog_get
    if _newclass:jobMsgAckLog = property(_lsf.eventLog_jobMsgAckLog_get, _lsf.eventLog_jobMsgAckLog_set)
    __swig_setmethods__["jobRequeueLog"] = _lsf.eventLog_jobRequeueLog_set
    __swig_getmethods__["jobRequeueLog"] = _lsf.eventLog_jobRequeueLog_get
    if _newclass:jobRequeueLog = property(_lsf.eventLog_jobRequeueLog_get, _lsf.eventLog_jobRequeueLog_set)
    __swig_setmethods__["chkpntLog"] = _lsf.eventLog_chkpntLog_set
    __swig_getmethods__["chkpntLog"] = _lsf.eventLog_chkpntLog_get
    if _newclass:chkpntLog = property(_lsf.eventLog_chkpntLog_get, _lsf.eventLog_chkpntLog_set)
    __swig_setmethods__["sigactLog"] = _lsf.eventLog_sigactLog_set
    __swig_getmethods__["sigactLog"] = _lsf.eventLog_sigactLog_get
    if _newclass:sigactLog = property(_lsf.eventLog_sigactLog_get, _lsf.eventLog_sigactLog_set)
    __swig_setmethods__["jobOccupyReqLog"] = _lsf.eventLog_jobOccupyReqLog_set
    __swig_getmethods__["jobOccupyReqLog"] = _lsf.eventLog_jobOccupyReqLog_get
    if _newclass:jobOccupyReqLog = property(_lsf.eventLog_jobOccupyReqLog_get, _lsf.eventLog_jobOccupyReqLog_set)
    __swig_setmethods__["jobVacatedLog"] = _lsf.eventLog_jobVacatedLog_set
    __swig_getmethods__["jobVacatedLog"] = _lsf.eventLog_jobVacatedLog_get
    if _newclass:jobVacatedLog = property(_lsf.eventLog_jobVacatedLog_get, _lsf.eventLog_jobVacatedLog_set)
    __swig_setmethods__["jobStartAcceptLog"] = _lsf.eventLog_jobStartAcceptLog_set
    __swig_getmethods__["jobStartAcceptLog"] = _lsf.eventLog_jobStartAcceptLog_get
    if _newclass:jobStartAcceptLog = property(_lsf.eventLog_jobStartAcceptLog_get, _lsf.eventLog_jobStartAcceptLog_set)
    __swig_setmethods__["jobCleanLog"] = _lsf.eventLog_jobCleanLog_set
    __swig_getmethods__["jobCleanLog"] = _lsf.eventLog_jobCleanLog_get
    if _newclass:jobCleanLog = property(_lsf.eventLog_jobCleanLog_get, _lsf.eventLog_jobCleanLog_set)
    __swig_setmethods__["jobExceptionLog"] = _lsf.eventLog_jobExceptionLog_set
    __swig_getmethods__["jobExceptionLog"] = _lsf.eventLog_jobExceptionLog_get
    if _newclass:jobExceptionLog = property(_lsf.eventLog_jobExceptionLog_get, _lsf.eventLog_jobExceptionLog_set)
    __swig_setmethods__["jgrpNewLog"] = _lsf.eventLog_jgrpNewLog_set
    __swig_getmethods__["jgrpNewLog"] = _lsf.eventLog_jgrpNewLog_get
    if _newclass:jgrpNewLog = property(_lsf.eventLog_jgrpNewLog_get, _lsf.eventLog_jgrpNewLog_set)
    __swig_setmethods__["jgrpCtrlLog"] = _lsf.eventLog_jgrpCtrlLog_set
    __swig_getmethods__["jgrpCtrlLog"] = _lsf.eventLog_jgrpCtrlLog_get
    if _newclass:jgrpCtrlLog = property(_lsf.eventLog_jgrpCtrlLog_get, _lsf.eventLog_jgrpCtrlLog_set)
    __swig_setmethods__["jobForceRequestLog"] = _lsf.eventLog_jobForceRequestLog_set
    __swig_getmethods__["jobForceRequestLog"] = _lsf.eventLog_jobForceRequestLog_get
    if _newclass:jobForceRequestLog = property(_lsf.eventLog_jobForceRequestLog_get, _lsf.eventLog_jobForceRequestLog_set)
    __swig_setmethods__["logSwitchLog"] = _lsf.eventLog_logSwitchLog_set
    __swig_getmethods__["logSwitchLog"] = _lsf.eventLog_logSwitchLog_get
    if _newclass:logSwitchLog = property(_lsf.eventLog_logSwitchLog_get, _lsf.eventLog_logSwitchLog_set)
    __swig_setmethods__["jobModLog"] = _lsf.eventLog_jobModLog_set
    __swig_getmethods__["jobModLog"] = _lsf.eventLog_jobModLog_get
    if _newclass:jobModLog = property(_lsf.eventLog_jobModLog_get, _lsf.eventLog_jobModLog_set)
    __swig_setmethods__["jgrpStatusLog"] = _lsf.eventLog_jgrpStatusLog_set
    __swig_getmethods__["jgrpStatusLog"] = _lsf.eventLog_jgrpStatusLog_get
    if _newclass:jgrpStatusLog = property(_lsf.eventLog_jgrpStatusLog_get, _lsf.eventLog_jgrpStatusLog_set)
    __swig_setmethods__["jobAttrSetLog"] = _lsf.eventLog_jobAttrSetLog_set
    __swig_getmethods__["jobAttrSetLog"] = _lsf.eventLog_jobAttrSetLog_get
    if _newclass:jobAttrSetLog = property(_lsf.eventLog_jobAttrSetLog_get, _lsf.eventLog_jobAttrSetLog_set)
    __swig_setmethods__["jobExternalMsgLog"] = _lsf.eventLog_jobExternalMsgLog_set
    __swig_getmethods__["jobExternalMsgLog"] = _lsf.eventLog_jobExternalMsgLog_get
    if _newclass:jobExternalMsgLog = property(_lsf.eventLog_jobExternalMsgLog_get, _lsf.eventLog_jobExternalMsgLog_set)
    __swig_setmethods__["jobChunkLog"] = _lsf.eventLog_jobChunkLog_set
    __swig_getmethods__["jobChunkLog"] = _lsf.eventLog_jobChunkLog_get
    if _newclass:jobChunkLog = property(_lsf.eventLog_jobChunkLog_get, _lsf.eventLog_jobChunkLog_set)
    __swig_setmethods__["sbdUnreportedStatusLog"] = _lsf.eventLog_sbdUnreportedStatusLog_set
    __swig_getmethods__["sbdUnreportedStatusLog"] = _lsf.eventLog_sbdUnreportedStatusLog_get
    if _newclass:sbdUnreportedStatusLog = property(_lsf.eventLog_sbdUnreportedStatusLog_get, _lsf.eventLog_sbdUnreportedStatusLog_set)
    __swig_setmethods__["rsvFinishLog"] = _lsf.eventLog_rsvFinishLog_set
    __swig_getmethods__["rsvFinishLog"] = _lsf.eventLog_rsvFinishLog_get
    if _newclass:rsvFinishLog = property(_lsf.eventLog_rsvFinishLog_get, _lsf.eventLog_rsvFinishLog_set)
    __swig_setmethods__["hgCtrlLog"] = _lsf.eventLog_hgCtrlLog_set
    __swig_getmethods__["hgCtrlLog"] = _lsf.eventLog_hgCtrlLog_get
    if _newclass:hgCtrlLog = property(_lsf.eventLog_hgCtrlLog_get, _lsf.eventLog_hgCtrlLog_set)
    __swig_setmethods__["cpuProfileLog"] = _lsf.eventLog_cpuProfileLog_set
    __swig_getmethods__["cpuProfileLog"] = _lsf.eventLog_cpuProfileLog_get
    if _newclass:cpuProfileLog = property(_lsf.eventLog_cpuProfileLog_get, _lsf.eventLog_cpuProfileLog_set)
    __swig_setmethods__["dataLoggingLog"] = _lsf.eventLog_dataLoggingLog_set
    __swig_getmethods__["dataLoggingLog"] = _lsf.eventLog_dataLoggingLog_get
    if _newclass:dataLoggingLog = property(_lsf.eventLog_dataLoggingLog_get, _lsf.eventLog_dataLoggingLog_set)
    __swig_setmethods__["jobRunRusageLog"] = _lsf.eventLog_jobRunRusageLog_set
    __swig_getmethods__["jobRunRusageLog"] = _lsf.eventLog_jobRunRusageLog_get
    if _newclass:jobRunRusageLog = property(_lsf.eventLog_jobRunRusageLog_get, _lsf.eventLog_jobRunRusageLog_set)
    __swig_setmethods__["eventEOSLog"] = _lsf.eventLog_eventEOSLog_set
    __swig_getmethods__["eventEOSLog"] = _lsf.eventLog_eventEOSLog_get
    if _newclass:eventEOSLog = property(_lsf.eventLog_eventEOSLog_get, _lsf.eventLog_eventEOSLog_set)
    __swig_setmethods__["slaLog"] = _lsf.eventLog_slaLog_set
    __swig_getmethods__["slaLog"] = _lsf.eventLog_slaLog_get
    if _newclass:slaLog = property(_lsf.eventLog_slaLog_get, _lsf.eventLog_slaLog_set)
    __swig_setmethods__["perfmonLog"] = _lsf.eventLog_perfmonLog_set
    __swig_getmethods__["perfmonLog"] = _lsf.eventLog_perfmonLog_get
    if _newclass:perfmonLog = property(_lsf.eventLog_perfmonLog_get, _lsf.eventLog_perfmonLog_set)
    __swig_setmethods__["taskFinishLog"] = _lsf.eventLog_taskFinishLog_set
    __swig_getmethods__["taskFinishLog"] = _lsf.eventLog_taskFinishLog_get
    if _newclass:taskFinishLog = property(_lsf.eventLog_taskFinishLog_get, _lsf.eventLog_taskFinishLog_set)
    __swig_setmethods__["jobResizeNotifyStartLog"] = _lsf.eventLog_jobResizeNotifyStartLog_set
    __swig_getmethods__["jobResizeNotifyStartLog"] = _lsf.eventLog_jobResizeNotifyStartLog_get
    if _newclass:jobResizeNotifyStartLog = property(_lsf.eventLog_jobResizeNotifyStartLog_get, _lsf.eventLog_jobResizeNotifyStartLog_set)
    __swig_setmethods__["jobResizeNotifyAcceptLog"] = _lsf.eventLog_jobResizeNotifyAcceptLog_set
    __swig_getmethods__["jobResizeNotifyAcceptLog"] = _lsf.eventLog_jobResizeNotifyAcceptLog_get
    if _newclass:jobResizeNotifyAcceptLog = property(_lsf.eventLog_jobResizeNotifyAcceptLog_get, _lsf.eventLog_jobResizeNotifyAcceptLog_set)
    __swig_setmethods__["jobResizeNotifyDoneLog"] = _lsf.eventLog_jobResizeNotifyDoneLog_set
    __swig_getmethods__["jobResizeNotifyDoneLog"] = _lsf.eventLog_jobResizeNotifyDoneLog_get
    if _newclass:jobResizeNotifyDoneLog = property(_lsf.eventLog_jobResizeNotifyDoneLog_get, _lsf.eventLog_jobResizeNotifyDoneLog_set)
    __swig_setmethods__["jobResizeReleaseLog"] = _lsf.eventLog_jobResizeReleaseLog_set
    __swig_getmethods__["jobResizeReleaseLog"] = _lsf.eventLog_jobResizeReleaseLog_get
    if _newclass:jobResizeReleaseLog = property(_lsf.eventLog_jobResizeReleaseLog_get, _lsf.eventLog_jobResizeReleaseLog_set)
    __swig_setmethods__["jobResizeCancelLog"] = _lsf.eventLog_jobResizeCancelLog_set
    __swig_getmethods__["jobResizeCancelLog"] = _lsf.eventLog_jobResizeCancelLog_get
    if _newclass:jobResizeCancelLog = property(_lsf.eventLog_jobResizeCancelLog_get, _lsf.eventLog_jobResizeCancelLog_set)
    __swig_setmethods__["jobResizeLog"] = _lsf.eventLog_jobResizeLog_set
    __swig_getmethods__["jobResizeLog"] = _lsf.eventLog_jobResizeLog_get
    if _newclass:jobResizeLog = property(_lsf.eventLog_jobResizeLog_get, _lsf.eventLog_jobResizeLog_set)
    __swig_setmethods__["jobFinish2Log"] = _lsf.eventLog_jobFinish2Log_set
    __swig_getmethods__["jobFinish2Log"] = _lsf.eventLog_jobFinish2Log_get
    if _newclass:jobFinish2Log = property(_lsf.eventLog_jobFinish2Log_get, _lsf.eventLog_jobFinish2Log_set)
    __swig_setmethods__["jobStartLimitLog"] = _lsf.eventLog_jobStartLimitLog_set
    __swig_getmethods__["jobStartLimitLog"] = _lsf.eventLog_jobStartLimitLog_get
    if _newclass:jobStartLimitLog = property(_lsf.eventLog_jobStartLimitLog_get, _lsf.eventLog_jobStartLimitLog_set)
    __swig_setmethods__["jobStatus2Log"] = _lsf.eventLog_jobStatus2Log_set
    __swig_getmethods__["jobStatus2Log"] = _lsf.eventLog_jobStatus2Log_get
    if _newclass:jobStatus2Log = property(_lsf.eventLog_jobStatus2Log_get, _lsf.eventLog_jobStatus2Log_set)
    __swig_setmethods__["jobPendingReasonsLog"] = _lsf.eventLog_jobPendingReasonsLog_set
    __swig_getmethods__["jobPendingReasonsLog"] = _lsf.eventLog_jobPendingReasonsLog_get
    if _newclass:jobPendingReasonsLog = property(_lsf.eventLog_jobPendingReasonsLog_get, _lsf.eventLog_jobPendingReasonsLog_set)
    def __init__(self, *args): 
        this = _lsf.new_eventLog(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _lsf.delete_eventLog
    __del__ = lambda self : None;
eventLog_swigregister = _lsf.eventLog_swigregister
eventLog_swigregister(eventLog)

class eventRec(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, eventRec, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, eventRec, name)
    __repr__ = _swig_repr
    __swig_setmethods__["version"] = _lsf.eventRec_version_set
    __swig_getmethods__["version"] = _lsf.eventRec_version_get
    if _newclass:version = property(_lsf.eventRec_version_get, _lsf.eventRec_version_set)
    __swig_setmethods__["type"] = _lsf.eventRec_type_set
    __swig_getmethods__["type"] = _lsf.eventRec_type_get
    if _newclass:type = property(_lsf.eventRec_type_get, _lsf.eventRec_type_set)
    __swig_setmethods__["eventTime"] = _lsf.eventRec_eventTime_set
    __swig_getmethods__["eventTime"] = _lsf.eventRec_eventTime_get
    if _newclass:eventTime = property(_lsf.eventRec_eventTime_get, _lsf.eventRec_eventTime_set)
    __swig_setmethods__["eventLog"] = _lsf.eventRec_eventLog_set
    __swig_getmethods__["eventLog"] = _lsf.eventRec_eventLog_get
    if _newclass:eventLog = property(_lsf.eventRec_eventLog_get, _lsf.eventRec_eventLog_set)
    def __init__(self, *args): 
        this = _lsf.new_eventRec(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _lsf.delete_eventRec
    __del__ = lambda self : None;
eventRec_swigregister = _lsf.eventRec_swigregister
eventRec_swigregister(eventRec)

class eventLogFile(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, eventLogFile, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, eventLogFile, name)
    __repr__ = _swig_repr
    __swig_setmethods__["eventDir"] = _lsf.eventLogFile_eventDir_set
    __swig_getmethods__["eventDir"] = _lsf.eventLogFile_eventDir_get
    if _newclass:eventDir = property(_lsf.eventLogFile_eventDir_get, _lsf.eventLogFile_eventDir_set)
    __swig_setmethods__["beginTime"] = _lsf.eventLogFile_beginTime_set
    __swig_getmethods__["beginTime"] = _lsf.eventLogFile_beginTime_get
    if _newclass:beginTime = property(_lsf.eventLogFile_beginTime_get, _lsf.eventLogFile_beginTime_set)
    __swig_setmethods__["endTime"] = _lsf.eventLogFile_endTime_set
    __swig_getmethods__["endTime"] = _lsf.eventLogFile_endTime_get
    if _newclass:endTime = property(_lsf.eventLogFile_endTime_get, _lsf.eventLogFile_endTime_set)
    def __init__(self, *args): 
        this = _lsf.new_eventLogFile(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _lsf.delete_eventLogFile
    __del__ = lambda self : None;
eventLogFile_swigregister = _lsf.eventLogFile_swigregister
eventLogFile_swigregister(eventLogFile)

class eventLogHandle(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, eventLogHandle, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, eventLogHandle, name)
    __repr__ = _swig_repr
    __swig_setmethods__["fp"] = _lsf.eventLogHandle_fp_set
    __swig_getmethods__["fp"] = _lsf.eventLogHandle_fp_get
    if _newclass:fp = property(_lsf.eventLogHandle_fp_get, _lsf.eventLogHandle_fp_set)
    __swig_setmethods__["openEventFile"] = _lsf.eventLogHandle_openEventFile_set
    __swig_getmethods__["openEventFile"] = _lsf.eventLogHandle_openEventFile_get
    if _newclass:openEventFile = property(_lsf.eventLogHandle_openEventFile_get, _lsf.eventLogHandle_openEventFile_set)
    __swig_setmethods__["curOpenFile"] = _lsf.eventLogHandle_curOpenFile_set
    __swig_getmethods__["curOpenFile"] = _lsf.eventLogHandle_curOpenFile_get
    if _newclass:curOpenFile = property(_lsf.eventLogHandle_curOpenFile_get, _lsf.eventLogHandle_curOpenFile_set)
    __swig_setmethods__["lastOpenFile"] = _lsf.eventLogHandle_lastOpenFile_set
    __swig_getmethods__["lastOpenFile"] = _lsf.eventLogHandle_lastOpenFile_get
    if _newclass:lastOpenFile = property(_lsf.eventLogHandle_lastOpenFile_get, _lsf.eventLogHandle_lastOpenFile_set)
    def __init__(self, *args): 
        this = _lsf.new_eventLogHandle(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _lsf.delete_eventLogHandle
    __del__ = lambda self : None;
eventLogHandle_swigregister = _lsf.eventLogHandle_swigregister
eventLogHandle_swigregister(eventLogHandle)

LSF_JOBIDINDEX_FILENAME = _lsf.LSF_JOBIDINDEX_FILENAME
LSF_JOBIDINDEX_FILETAG = _lsf.LSF_JOBIDINDEX_FILETAG
class jobIdIndexS(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, jobIdIndexS, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, jobIdIndexS, name)
    __repr__ = _swig_repr
    __swig_setmethods__["fileName"] = _lsf.jobIdIndexS_fileName_set
    __swig_getmethods__["fileName"] = _lsf.jobIdIndexS_fileName_get
    if _newclass:fileName = property(_lsf.jobIdIndexS_fileName_get, _lsf.jobIdIndexS_fileName_set)
    __swig_setmethods__["fp"] = _lsf.jobIdIndexS_fp_set
    __swig_getmethods__["fp"] = _lsf.jobIdIndexS_fp_get
    if _newclass:fp = property(_lsf.jobIdIndexS_fp_get, _lsf.jobIdIndexS_fp_set)
    __swig_setmethods__["version"] = _lsf.jobIdIndexS_version_set
    __swig_getmethods__["version"] = _lsf.jobIdIndexS_version_get
    if _newclass:version = property(_lsf.jobIdIndexS_version_get, _lsf.jobIdIndexS_version_set)
    __swig_setmethods__["totalRows"] = _lsf.jobIdIndexS_totalRows_set
    __swig_getmethods__["totalRows"] = _lsf.jobIdIndexS_totalRows_get
    if _newclass:totalRows = property(_lsf.jobIdIndexS_totalRows_get, _lsf.jobIdIndexS_totalRows_set)
    __swig_setmethods__["lastUpdate"] = _lsf.jobIdIndexS_lastUpdate_set
    __swig_getmethods__["lastUpdate"] = _lsf.jobIdIndexS_lastUpdate_get
    if _newclass:lastUpdate = property(_lsf.jobIdIndexS_lastUpdate_get, _lsf.jobIdIndexS_lastUpdate_set)
    __swig_setmethods__["curRow"] = _lsf.jobIdIndexS_curRow_set
    __swig_getmethods__["curRow"] = _lsf.jobIdIndexS_curRow_get
    if _newclass:curRow = property(_lsf.jobIdIndexS_curRow_get, _lsf.jobIdIndexS_curRow_set)
    __swig_setmethods__["timeStamp"] = _lsf.jobIdIndexS_timeStamp_set
    __swig_getmethods__["timeStamp"] = _lsf.jobIdIndexS_timeStamp_get
    if _newclass:timeStamp = property(_lsf.jobIdIndexS_timeStamp_get, _lsf.jobIdIndexS_timeStamp_set)
    __swig_setmethods__["minJobId"] = _lsf.jobIdIndexS_minJobId_set
    __swig_getmethods__["minJobId"] = _lsf.jobIdIndexS_minJobId_get
    if _newclass:minJobId = property(_lsf.jobIdIndexS_minJobId_get, _lsf.jobIdIndexS_minJobId_set)
    __swig_setmethods__["maxJobId"] = _lsf.jobIdIndexS_maxJobId_set
    __swig_getmethods__["maxJobId"] = _lsf.jobIdIndexS_maxJobId_get
    if _newclass:maxJobId = property(_lsf.jobIdIndexS_maxJobId_get, _lsf.jobIdIndexS_maxJobId_set)
    __swig_setmethods__["totalJobIds"] = _lsf.jobIdIndexS_totalJobIds_set
    __swig_getmethods__["totalJobIds"] = _lsf.jobIdIndexS_totalJobIds_get
    if _newclass:totalJobIds = property(_lsf.jobIdIndexS_totalJobIds_get, _lsf.jobIdIndexS_totalJobIds_set)
    __swig_setmethods__["jobIds"] = _lsf.jobIdIndexS_jobIds_set
    __swig_getmethods__["jobIds"] = _lsf.jobIdIndexS_jobIds_get
    if _newclass:jobIds = property(_lsf.jobIdIndexS_jobIds_get, _lsf.jobIdIndexS_jobIds_set)
    def __init__(self, *args): 
        this = _lsf.new_jobIdIndexS(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _lsf.delete_jobIdIndexS
    __del__ = lambda self : None;
jobIdIndexS_swigregister = _lsf.jobIdIndexS_swigregister
jobIdIndexS_swigregister(jobIdIndexS)

class sortIntList(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, sortIntList, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, sortIntList, name)
    __repr__ = _swig_repr
    __swig_setmethods__["value"] = _lsf.sortIntList_value_set
    __swig_getmethods__["value"] = _lsf.sortIntList_value_get
    if _newclass:value = property(_lsf.sortIntList_value_get, _lsf.sortIntList_value_set)
    __swig_setmethods__["forw"] = _lsf.sortIntList_forw_set
    __swig_getmethods__["forw"] = _lsf.sortIntList_forw_get
    if _newclass:forw = property(_lsf.sortIntList_forw_get, _lsf.sortIntList_forw_set)
    __swig_setmethods__["back"] = _lsf.sortIntList_back_set
    __swig_getmethods__["back"] = _lsf.sortIntList_back_get
    if _newclass:back = property(_lsf.sortIntList_back_get, _lsf.sortIntList_back_set)
    def __init__(self, *args): 
        this = _lsf.new_sortIntList(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _lsf.delete_sortIntList
    __del__ = lambda self : None;
sortIntList_swigregister = _lsf.sortIntList_swigregister
sortIntList_swigregister(sortIntList)

class nqsStatusReq(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, nqsStatusReq, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, nqsStatusReq, name)
    __repr__ = _swig_repr
    __swig_setmethods__["jobId"] = _lsf.nqsStatusReq_jobId_set
    __swig_getmethods__["jobId"] = _lsf.nqsStatusReq_jobId_get
    if _newclass:jobId = property(_lsf.nqsStatusReq_jobId_get, _lsf.nqsStatusReq_jobId_set)
    __swig_setmethods__["opCode"] = _lsf.nqsStatusReq_opCode_set
    __swig_getmethods__["opCode"] = _lsf.nqsStatusReq_opCode_get
    if _newclass:opCode = property(_lsf.nqsStatusReq_opCode_get, _lsf.nqsStatusReq_opCode_set)
    __swig_setmethods__["reportCode"] = _lsf.nqsStatusReq_reportCode_set
    __swig_getmethods__["reportCode"] = _lsf.nqsStatusReq_reportCode_get
    if _newclass:reportCode = property(_lsf.nqsStatusReq_reportCode_get, _lsf.nqsStatusReq_reportCode_set)
    __swig_setmethods__["nqsQueue"] = _lsf.nqsStatusReq_nqsQueue_set
    __swig_getmethods__["nqsQueue"] = _lsf.nqsStatusReq_nqsQueue_get
    if _newclass:nqsQueue = property(_lsf.nqsStatusReq_nqsQueue_get, _lsf.nqsStatusReq_nqsQueue_set)
    __swig_setmethods__["fromUid"] = _lsf.nqsStatusReq_fromUid_set
    __swig_getmethods__["fromUid"] = _lsf.nqsStatusReq_fromUid_get
    if _newclass:fromUid = property(_lsf.nqsStatusReq_fromUid_get, _lsf.nqsStatusReq_fromUid_set)
    __swig_setmethods__["fromUserName"] = _lsf.nqsStatusReq_fromUserName_set
    __swig_getmethods__["fromUserName"] = _lsf.nqsStatusReq_fromUserName_get
    if _newclass:fromUserName = property(_lsf.nqsStatusReq_fromUserName_get, _lsf.nqsStatusReq_fromUserName_set)
    __swig_setmethods__["fromHostName"] = _lsf.nqsStatusReq_fromHostName_set
    __swig_getmethods__["fromHostName"] = _lsf.nqsStatusReq_fromHostName_get
    if _newclass:fromHostName = property(_lsf.nqsStatusReq_fromHostName_get, _lsf.nqsStatusReq_fromHostName_set)
    __swig_setmethods__["idx"] = _lsf.nqsStatusReq_idx_set
    __swig_getmethods__["idx"] = _lsf.nqsStatusReq_idx_get
    if _newclass:idx = property(_lsf.nqsStatusReq_idx_get, _lsf.nqsStatusReq_idx_set)
    def __init__(self, *args): 
        this = _lsf.new_nqsStatusReq(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _lsf.delete_nqsStatusReq
    __del__ = lambda self : None;
nqsStatusReq_swigregister = _lsf.nqsStatusReq_swigregister
nqsStatusReq_swigregister(nqsStatusReq)

class nqsStatusReply(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, nqsStatusReply, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, nqsStatusReply, name)
    __repr__ = _swig_repr
    __swig_setmethods__["orgHost"] = _lsf.nqsStatusReply_orgHost_set
    __swig_getmethods__["orgHost"] = _lsf.nqsStatusReply_orgHost_get
    if _newclass:orgHost = property(_lsf.nqsStatusReply_orgHost_get, _lsf.nqsStatusReply_orgHost_set)
    __swig_setmethods__["orgUser"] = _lsf.nqsStatusReply_orgUser_set
    __swig_getmethods__["orgUser"] = _lsf.nqsStatusReply_orgUser_get
    if _newclass:orgUser = property(_lsf.nqsStatusReply_orgUser_get, _lsf.nqsStatusReply_orgUser_set)
    __swig_setmethods__["startTime"] = _lsf.nqsStatusReply_startTime_set
    __swig_getmethods__["startTime"] = _lsf.nqsStatusReply_startTime_get
    if _newclass:startTime = property(_lsf.nqsStatusReply_startTime_get, _lsf.nqsStatusReply_startTime_set)
    __swig_setmethods__["jobName"] = _lsf.nqsStatusReply_jobName_set
    __swig_getmethods__["jobName"] = _lsf.nqsStatusReply_jobName_get
    if _newclass:jobName = property(_lsf.nqsStatusReply_jobName_get, _lsf.nqsStatusReply_jobName_set)
    __swig_setmethods__["nqsQueue"] = _lsf.nqsStatusReply_nqsQueue_set
    __swig_getmethods__["nqsQueue"] = _lsf.nqsStatusReply_nqsQueue_get
    if _newclass:nqsQueue = property(_lsf.nqsStatusReply_nqsQueue_get, _lsf.nqsStatusReply_nqsQueue_set)
    __swig_setmethods__["lsbManager"] = _lsf.nqsStatusReply_lsbManager_set
    __swig_getmethods__["lsbManager"] = _lsf.nqsStatusReply_lsbManager_get
    if _newclass:lsbManager = property(_lsf.nqsStatusReply_lsbManager_get, _lsf.nqsStatusReply_lsbManager_set)
    __swig_setmethods__["options"] = _lsf.nqsStatusReply_options_set
    __swig_getmethods__["options"] = _lsf.nqsStatusReply_options_get
    if _newclass:options = property(_lsf.nqsStatusReply_options_get, _lsf.nqsStatusReply_options_set)
    __swig_setmethods__["outFile"] = _lsf.nqsStatusReply_outFile_set
    __swig_getmethods__["outFile"] = _lsf.nqsStatusReply_outFile_get
    if _newclass:outFile = property(_lsf.nqsStatusReply_outFile_get, _lsf.nqsStatusReply_outFile_set)
    __swig_setmethods__["errFile"] = _lsf.nqsStatusReply_errFile_set
    __swig_getmethods__["errFile"] = _lsf.nqsStatusReply_errFile_get
    if _newclass:errFile = property(_lsf.nqsStatusReply_errFile_get, _lsf.nqsStatusReply_errFile_set)
    def __init__(self, *args): 
        this = _lsf.new_nqsStatusReply(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _lsf.delete_nqsStatusReply
    __del__ = lambda self : None;
nqsStatusReply_swigregister = _lsf.nqsStatusReply_swigregister
nqsStatusReply_swigregister(nqsStatusReply)

LSB_MAX_SD_LENGTH = _lsf.LSB_MAX_SD_LENGTH
class lsbMsgHdr(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, lsbMsgHdr, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, lsbMsgHdr, name)
    __repr__ = _swig_repr
    __swig_setmethods__["usrId"] = _lsf.lsbMsgHdr_usrId_set
    __swig_getmethods__["usrId"] = _lsf.lsbMsgHdr_usrId_get
    if _newclass:usrId = property(_lsf.lsbMsgHdr_usrId_get, _lsf.lsbMsgHdr_usrId_set)
    __swig_setmethods__["jobId"] = _lsf.lsbMsgHdr_jobId_set
    __swig_getmethods__["jobId"] = _lsf.lsbMsgHdr_jobId_get
    if _newclass:jobId = property(_lsf.lsbMsgHdr_jobId_get, _lsf.lsbMsgHdr_jobId_set)
    __swig_setmethods__["msgId"] = _lsf.lsbMsgHdr_msgId_set
    __swig_getmethods__["msgId"] = _lsf.lsbMsgHdr_msgId_get
    if _newclass:msgId = property(_lsf.lsbMsgHdr_msgId_get, _lsf.lsbMsgHdr_msgId_set)
    __swig_setmethods__["type"] = _lsf.lsbMsgHdr_type_set
    __swig_getmethods__["type"] = _lsf.lsbMsgHdr_type_get
    if _newclass:type = property(_lsf.lsbMsgHdr_type_get, _lsf.lsbMsgHdr_type_set)
    __swig_setmethods__["src"] = _lsf.lsbMsgHdr_src_set
    __swig_getmethods__["src"] = _lsf.lsbMsgHdr_src_get
    if _newclass:src = property(_lsf.lsbMsgHdr_src_get, _lsf.lsbMsgHdr_src_set)
    __swig_setmethods__["dest"] = _lsf.lsbMsgHdr_dest_set
    __swig_getmethods__["dest"] = _lsf.lsbMsgHdr_dest_get
    if _newclass:dest = property(_lsf.lsbMsgHdr_dest_get, _lsf.lsbMsgHdr_dest_set)
    def __init__(self, *args): 
        this = _lsf.new_lsbMsgHdr(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _lsf.delete_lsbMsgHdr
    __del__ = lambda self : None;
lsbMsgHdr_swigregister = _lsf.lsbMsgHdr_swigregister
lsbMsgHdr_swigregister(lsbMsgHdr)

class lsbMsg(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, lsbMsg, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, lsbMsg, name)
    __repr__ = _swig_repr
    __swig_setmethods__["header"] = _lsf.lsbMsg_header_set
    __swig_getmethods__["header"] = _lsf.lsbMsg_header_get
    if _newclass:header = property(_lsf.lsbMsg_header_get, _lsf.lsbMsg_header_set)
    __swig_setmethods__["msg"] = _lsf.lsbMsg_msg_set
    __swig_getmethods__["msg"] = _lsf.lsbMsg_msg_get
    if _newclass:msg = property(_lsf.lsbMsg_msg_get, _lsf.lsbMsg_msg_set)
    def __init__(self, *args): 
        this = _lsf.new_lsbMsg(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _lsf.delete_lsbMsg
    __del__ = lambda self : None;
lsbMsg_swigregister = _lsf.lsbMsg_swigregister
lsbMsg_swigregister(lsbMsg)

CONF_NO_CHECK = _lsf.CONF_NO_CHECK
CONF_CHECK = _lsf.CONF_CHECK
CONF_EXPAND = _lsf.CONF_EXPAND
CONF_RETURN_HOSTSPEC = _lsf.CONF_RETURN_HOSTSPEC
CONF_NO_EXPAND = _lsf.CONF_NO_EXPAND
CONF_HAS_CU = _lsf.CONF_HAS_CU
CONF_ERROR_HANDLE = _lsf.CONF_ERROR_HANDLE
CONF_SYNTAX_CHECK = _lsf.CONF_SYNTAX_CHECK
CONF_IGNORE_OTHERS = _lsf.CONF_IGNORE_OTHERS
CONF_REJECT_NULLSHARE = _lsf.CONF_REJECT_NULLSHARE
CONF_NO_LOG = _lsf.CONF_NO_LOG
CONF_AT_BACK = _lsf.CONF_AT_BACK
CONF_RMSHARE = _lsf.CONF_RMSHARE
CONF_DUPLICATE_SECTION = _lsf.CONF_DUPLICATE_SECTION
CONF_IGNORE_CHECK = _lsf.CONF_IGNORE_CHECK
class paramConf(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, paramConf, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, paramConf, name)
    __repr__ = _swig_repr
    __swig_setmethods__["param"] = _lsf.paramConf_param_set
    __swig_getmethods__["param"] = _lsf.paramConf_param_get
    if _newclass:param = property(_lsf.paramConf_param_get, _lsf.paramConf_param_set)
    def __init__(self, *args): 
        this = _lsf.new_paramConf(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _lsf.delete_paramConf
    __del__ = lambda self : None;
paramConf_swigregister = _lsf.paramConf_swigregister
paramConf_swigregister(paramConf)

class userConf(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, userConf, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, userConf, name)
    __repr__ = _swig_repr
    __swig_setmethods__["numUgroups"] = _lsf.userConf_numUgroups_set
    __swig_getmethods__["numUgroups"] = _lsf.userConf_numUgroups_get
    if _newclass:numUgroups = property(_lsf.userConf_numUgroups_get, _lsf.userConf_numUgroups_set)
    __swig_setmethods__["ugroups"] = _lsf.userConf_ugroups_set
    __swig_getmethods__["ugroups"] = _lsf.userConf_ugroups_get
    if _newclass:ugroups = property(_lsf.userConf_ugroups_get, _lsf.userConf_ugroups_set)
    __swig_setmethods__["numUsers"] = _lsf.userConf_numUsers_set
    __swig_getmethods__["numUsers"] = _lsf.userConf_numUsers_get
    if _newclass:numUsers = property(_lsf.userConf_numUsers_get, _lsf.userConf_numUsers_set)
    __swig_setmethods__["users"] = _lsf.userConf_users_set
    __swig_getmethods__["users"] = _lsf.userConf_users_get
    if _newclass:users = property(_lsf.userConf_users_get, _lsf.userConf_users_set)
    __swig_setmethods__["numUserEquivalent"] = _lsf.userConf_numUserEquivalent_set
    __swig_getmethods__["numUserEquivalent"] = _lsf.userConf_numUserEquivalent_get
    if _newclass:numUserEquivalent = property(_lsf.userConf_numUserEquivalent_get, _lsf.userConf_numUserEquivalent_set)
    __swig_setmethods__["userEquivalent"] = _lsf.userConf_userEquivalent_set
    __swig_getmethods__["userEquivalent"] = _lsf.userConf_userEquivalent_get
    if _newclass:userEquivalent = property(_lsf.userConf_userEquivalent_get, _lsf.userConf_userEquivalent_set)
    __swig_setmethods__["numUserMapping"] = _lsf.userConf_numUserMapping_set
    __swig_getmethods__["numUserMapping"] = _lsf.userConf_numUserMapping_get
    if _newclass:numUserMapping = property(_lsf.userConf_numUserMapping_get, _lsf.userConf_numUserMapping_set)
    __swig_setmethods__["userMapping"] = _lsf.userConf_userMapping_set
    __swig_getmethods__["userMapping"] = _lsf.userConf_userMapping_get
    if _newclass:userMapping = property(_lsf.userConf_userMapping_get, _lsf.userConf_userMapping_set)
    def __init__(self, *args): 
        this = _lsf.new_userConf(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _lsf.delete_userConf
    __del__ = lambda self : None;
userConf_swigregister = _lsf.userConf_swigregister
userConf_swigregister(userConf)

class hostConf(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, hostConf, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, hostConf, name)
    __repr__ = _swig_repr
    __swig_setmethods__["numHosts"] = _lsf.hostConf_numHosts_set
    __swig_getmethods__["numHosts"] = _lsf.hostConf_numHosts_get
    if _newclass:numHosts = property(_lsf.hostConf_numHosts_get, _lsf.hostConf_numHosts_set)
    __swig_setmethods__["hosts"] = _lsf.hostConf_hosts_set
    __swig_getmethods__["hosts"] = _lsf.hostConf_hosts_get
    if _newclass:hosts = property(_lsf.hostConf_hosts_get, _lsf.hostConf_hosts_set)
    __swig_setmethods__["numHparts"] = _lsf.hostConf_numHparts_set
    __swig_getmethods__["numHparts"] = _lsf.hostConf_numHparts_get
    if _newclass:numHparts = property(_lsf.hostConf_numHparts_get, _lsf.hostConf_numHparts_set)
    __swig_setmethods__["hparts"] = _lsf.hostConf_hparts_set
    __swig_getmethods__["hparts"] = _lsf.hostConf_hparts_get
    if _newclass:hparts = property(_lsf.hostConf_hparts_get, _lsf.hostConf_hparts_set)
    __swig_setmethods__["numHgroups"] = _lsf.hostConf_numHgroups_set
    __swig_getmethods__["numHgroups"] = _lsf.hostConf_numHgroups_get
    if _newclass:numHgroups = property(_lsf.hostConf_numHgroups_get, _lsf.hostConf_numHgroups_set)
    __swig_setmethods__["hgroups"] = _lsf.hostConf_hgroups_set
    __swig_getmethods__["hgroups"] = _lsf.hostConf_hgroups_get
    if _newclass:hgroups = property(_lsf.hostConf_hgroups_get, _lsf.hostConf_hgroups_set)
    def __init__(self, *args): 
        this = _lsf.new_hostConf(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _lsf.delete_hostConf
    __del__ = lambda self : None;
hostConf_swigregister = _lsf.hostConf_swigregister
hostConf_swigregister(hostConf)

class LSB_SHARED_RESOURCE_INST_T(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, LSB_SHARED_RESOURCE_INST_T, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, LSB_SHARED_RESOURCE_INST_T, name)
    __repr__ = _swig_repr
    __swig_setmethods__["totalValue"] = _lsf.LSB_SHARED_RESOURCE_INST_T_totalValue_set
    __swig_getmethods__["totalValue"] = _lsf.LSB_SHARED_RESOURCE_INST_T_totalValue_get
    if _newclass:totalValue = property(_lsf.LSB_SHARED_RESOURCE_INST_T_totalValue_get, _lsf.LSB_SHARED_RESOURCE_INST_T_totalValue_set)
    __swig_setmethods__["rsvValue"] = _lsf.LSB_SHARED_RESOURCE_INST_T_rsvValue_set
    __swig_getmethods__["rsvValue"] = _lsf.LSB_SHARED_RESOURCE_INST_T_rsvValue_get
    if _newclass:rsvValue = property(_lsf.LSB_SHARED_RESOURCE_INST_T_rsvValue_get, _lsf.LSB_SHARED_RESOURCE_INST_T_rsvValue_set)
    __swig_setmethods__["nHosts"] = _lsf.LSB_SHARED_RESOURCE_INST_T_nHosts_set
    __swig_getmethods__["nHosts"] = _lsf.LSB_SHARED_RESOURCE_INST_T_nHosts_get
    if _newclass:nHosts = property(_lsf.LSB_SHARED_RESOURCE_INST_T_nHosts_get, _lsf.LSB_SHARED_RESOURCE_INST_T_nHosts_set)
    __swig_setmethods__["hostList"] = _lsf.LSB_SHARED_RESOURCE_INST_T_hostList_set
    __swig_getmethods__["hostList"] = _lsf.LSB_SHARED_RESOURCE_INST_T_hostList_get
    if _newclass:hostList = property(_lsf.LSB_SHARED_RESOURCE_INST_T_hostList_get, _lsf.LSB_SHARED_RESOURCE_INST_T_hostList_set)
    def __init__(self, *args): 
        this = _lsf.new_LSB_SHARED_RESOURCE_INST_T(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _lsf.delete_LSB_SHARED_RESOURCE_INST_T
    __del__ = lambda self : None;
LSB_SHARED_RESOURCE_INST_T_swigregister = _lsf.LSB_SHARED_RESOURCE_INST_T_swigregister
LSB_SHARED_RESOURCE_INST_T_swigregister(LSB_SHARED_RESOURCE_INST_T)

class LSB_SHARED_RESOURCE_INFO_T(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, LSB_SHARED_RESOURCE_INFO_T, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, LSB_SHARED_RESOURCE_INFO_T, name)
    __repr__ = _swig_repr
    __swig_setmethods__["resourceName"] = _lsf.LSB_SHARED_RESOURCE_INFO_T_resourceName_set
    __swig_getmethods__["resourceName"] = _lsf.LSB_SHARED_RESOURCE_INFO_T_resourceName_get
    if _newclass:resourceName = property(_lsf.LSB_SHARED_RESOURCE_INFO_T_resourceName_get, _lsf.LSB_SHARED_RESOURCE_INFO_T_resourceName_set)
    __swig_setmethods__["nInstances"] = _lsf.LSB_SHARED_RESOURCE_INFO_T_nInstances_set
    __swig_getmethods__["nInstances"] = _lsf.LSB_SHARED_RESOURCE_INFO_T_nInstances_get
    if _newclass:nInstances = property(_lsf.LSB_SHARED_RESOURCE_INFO_T_nInstances_get, _lsf.LSB_SHARED_RESOURCE_INFO_T_nInstances_set)
    __swig_setmethods__["instances"] = _lsf.LSB_SHARED_RESOURCE_INFO_T_instances_set
    __swig_getmethods__["instances"] = _lsf.LSB_SHARED_RESOURCE_INFO_T_instances_get
    if _newclass:instances = property(_lsf.LSB_SHARED_RESOURCE_INFO_T_instances_get, _lsf.LSB_SHARED_RESOURCE_INFO_T_instances_set)
    def __init__(self, *args): 
        this = _lsf.new_LSB_SHARED_RESOURCE_INFO_T(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _lsf.delete_LSB_SHARED_RESOURCE_INFO_T
    __del__ = lambda self : None;
LSB_SHARED_RESOURCE_INFO_T_swigregister = _lsf.LSB_SHARED_RESOURCE_INFO_T_swigregister
LSB_SHARED_RESOURCE_INFO_T_swigregister(LSB_SHARED_RESOURCE_INFO_T)

class queueConf(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, queueConf, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, queueConf, name)
    __repr__ = _swig_repr
    __swig_setmethods__["numQueues"] = _lsf.queueConf_numQueues_set
    __swig_getmethods__["numQueues"] = _lsf.queueConf_numQueues_get
    if _newclass:numQueues = property(_lsf.queueConf_numQueues_get, _lsf.queueConf_numQueues_set)
    __swig_setmethods__["queues"] = _lsf.queueConf_queues_set
    __swig_getmethods__["queues"] = _lsf.queueConf_queues_get
    if _newclass:queues = property(_lsf.queueConf_queues_get, _lsf.queueConf_queues_set)
    def __init__(self, *args): 
        this = _lsf.new_queueConf(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _lsf.delete_queueConf
    __del__ = lambda self : None;
queueConf_swigregister = _lsf.queueConf_swigregister
queueConf_swigregister(queueConf)

class frameElementInfo(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, frameElementInfo, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, frameElementInfo, name)
    __repr__ = _swig_repr
    __swig_setmethods__["jobindex"] = _lsf.frameElementInfo_jobindex_set
    __swig_getmethods__["jobindex"] = _lsf.frameElementInfo_jobindex_get
    if _newclass:jobindex = property(_lsf.frameElementInfo_jobindex_get, _lsf.frameElementInfo_jobindex_set)
    __swig_setmethods__["jobState"] = _lsf.frameElementInfo_jobState_set
    __swig_getmethods__["jobState"] = _lsf.frameElementInfo_jobState_get
    if _newclass:jobState = property(_lsf.frameElementInfo_jobState_get, _lsf.frameElementInfo_jobState_set)
    __swig_setmethods__["start"] = _lsf.frameElementInfo_start_set
    __swig_getmethods__["start"] = _lsf.frameElementInfo_start_get
    if _newclass:start = property(_lsf.frameElementInfo_start_get, _lsf.frameElementInfo_start_set)
    __swig_setmethods__["end"] = _lsf.frameElementInfo_end_set
    __swig_getmethods__["end"] = _lsf.frameElementInfo_end_get
    if _newclass:end = property(_lsf.frameElementInfo_end_get, _lsf.frameElementInfo_end_set)
    __swig_setmethods__["step"] = _lsf.frameElementInfo_step_set
    __swig_getmethods__["step"] = _lsf.frameElementInfo_step_get
    if _newclass:step = property(_lsf.frameElementInfo_step_get, _lsf.frameElementInfo_step_set)
    __swig_setmethods__["chunk"] = _lsf.frameElementInfo_chunk_set
    __swig_getmethods__["chunk"] = _lsf.frameElementInfo_chunk_get
    if _newclass:chunk = property(_lsf.frameElementInfo_chunk_get, _lsf.frameElementInfo_chunk_set)
    def __init__(self, *args): 
        this = _lsf.new_frameElementInfo(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _lsf.delete_frameElementInfo
    __del__ = lambda self : None;
frameElementInfo_swigregister = _lsf.frameElementInfo_swigregister
frameElementInfo_swigregister(frameElementInfo)

class frameJobInfo(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, frameJobInfo, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, frameJobInfo, name)
    __repr__ = _swig_repr
    __swig_setmethods__["jobGid"] = _lsf.frameJobInfo_jobGid_set
    __swig_getmethods__["jobGid"] = _lsf.frameJobInfo_jobGid_get
    if _newclass:jobGid = property(_lsf.frameJobInfo_jobGid_get, _lsf.frameJobInfo_jobGid_set)
    __swig_setmethods__["maxJob"] = _lsf.frameJobInfo_maxJob_set
    __swig_getmethods__["maxJob"] = _lsf.frameJobInfo_maxJob_get
    if _newclass:maxJob = property(_lsf.frameJobInfo_maxJob_get, _lsf.frameJobInfo_maxJob_set)
    __swig_setmethods__["userName"] = _lsf.frameJobInfo_userName_set
    __swig_getmethods__["userName"] = _lsf.frameJobInfo_userName_get
    if _newclass:userName = property(_lsf.frameJobInfo_userName_get, _lsf.frameJobInfo_userName_set)
    __swig_setmethods__["jobName"] = _lsf.frameJobInfo_jobName_set
    __swig_getmethods__["jobName"] = _lsf.frameJobInfo_jobName_get
    if _newclass:jobName = property(_lsf.frameJobInfo_jobName_get, _lsf.frameJobInfo_jobName_set)
    __swig_setmethods__["frameElementPtr"] = _lsf.frameJobInfo_frameElementPtr_set
    __swig_getmethods__["frameElementPtr"] = _lsf.frameJobInfo_frameElementPtr_get
    if _newclass:frameElementPtr = property(_lsf.frameJobInfo_frameElementPtr_get, _lsf.frameJobInfo_frameElementPtr_set)
    def __init__(self, *args): 
        this = _lsf.new_frameJobInfo(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _lsf.delete_frameJobInfo
    __del__ = lambda self : None;
frameJobInfo_swigregister = _lsf.frameJobInfo_swigregister
frameJobInfo_swigregister(frameJobInfo)

class RsvEventInfo_prePost_t(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, RsvEventInfo_prePost_t, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, RsvEventInfo_prePost_t, name)
    __repr__ = _swig_repr
    __swig_setmethods__["shift"] = _lsf.RsvEventInfo_prePost_t_shift_set
    __swig_getmethods__["shift"] = _lsf.RsvEventInfo_prePost_t_shift_get
    if _newclass:shift = property(_lsf.RsvEventInfo_prePost_t_shift_get, _lsf.RsvEventInfo_prePost_t_shift_set)
    def __init__(self, *args): 
        this = _lsf.new_RsvEventInfo_prePost_t(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _lsf.delete_RsvEventInfo_prePost_t
    __del__ = lambda self : None;
RsvEventInfo_prePost_t_swigregister = _lsf.RsvEventInfo_prePost_t_swigregister
RsvEventInfo_prePost_t_swigregister(RsvEventInfo_prePost_t)

RSV_EXECEVENTTYPE_PRE = _lsf.RSV_EXECEVENTTYPE_PRE
RSV_EXECEVENTTYPE_POST = _lsf.RSV_EXECEVENTTYPE_POST
RSV_EXECEVENTNAME_PRE = _lsf.RSV_EXECEVENTNAME_PRE
RSV_EXECEVENTNAME_POST = _lsf.RSV_EXECEVENTNAME_POST
class rsvExecEvent_t(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, rsvExecEvent_t, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, rsvExecEvent_t, name)
    __repr__ = _swig_repr
    __swig_setmethods__["type"] = _lsf.rsvExecEvent_t_type_set
    __swig_getmethods__["type"] = _lsf.rsvExecEvent_t_type_get
    if _newclass:type = property(_lsf.rsvExecEvent_t_type_get, _lsf.rsvExecEvent_t_type_set)
    __swig_setmethods__["infoAttached"] = _lsf.rsvExecEvent_t_infoAttached_set
    __swig_getmethods__["infoAttached"] = _lsf.rsvExecEvent_t_infoAttached_get
    if _newclass:infoAttached = property(_lsf.rsvExecEvent_t_infoAttached_get, _lsf.rsvExecEvent_t_infoAttached_set)
    __swig_setmethods__["info"] = _lsf.rsvExecEvent_t_info_set
    __swig_getmethods__["info"] = _lsf.rsvExecEvent_t_info_get
    if _newclass:info = property(_lsf.rsvExecEvent_t_info_get, _lsf.rsvExecEvent_t_info_set)
    def __init__(self, *args): 
        this = _lsf.new_rsvExecEvent_t(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _lsf.delete_rsvExecEvent_t
    __del__ = lambda self : None;
rsvExecEvent_t_swigregister = _lsf.rsvExecEvent_t_swigregister
rsvExecEvent_t_swigregister(rsvExecEvent_t)

class rsvExecCmd_t(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, rsvExecCmd_t, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, rsvExecCmd_t, name)
    __repr__ = _swig_repr
    __swig_setmethods__["path"] = _lsf.rsvExecCmd_t_path_set
    __swig_getmethods__["path"] = _lsf.rsvExecCmd_t_path_get
    if _newclass:path = property(_lsf.rsvExecCmd_t_path_get, _lsf.rsvExecCmd_t_path_set)
    __swig_setmethods__["numEvents"] = _lsf.rsvExecCmd_t_numEvents_set
    __swig_getmethods__["numEvents"] = _lsf.rsvExecCmd_t_numEvents_get
    if _newclass:numEvents = property(_lsf.rsvExecCmd_t_numEvents_get, _lsf.rsvExecCmd_t_numEvents_set)
    __swig_setmethods__["events"] = _lsf.rsvExecCmd_t_events_set
    __swig_getmethods__["events"] = _lsf.rsvExecCmd_t_events_get
    if _newclass:events = property(_lsf.rsvExecCmd_t_events_get, _lsf.rsvExecCmd_t_events_set)
    def __init__(self, *args): 
        this = _lsf.new_rsvExecCmd_t(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _lsf.delete_rsvExecCmd_t
    __del__ = lambda self : None;
rsvExecCmd_t_swigregister = _lsf.rsvExecCmd_t_swigregister
rsvExecCmd_t_swigregister(rsvExecCmd_t)

RSV_OPTION_USER = _lsf.RSV_OPTION_USER
RSV_OPTION_GROUP = _lsf.RSV_OPTION_GROUP
RSV_OPTION_SYSTEM = _lsf.RSV_OPTION_SYSTEM
RSV_OPTION_RECUR = _lsf.RSV_OPTION_RECUR
RSV_OPTION_RESREQ = _lsf.RSV_OPTION_RESREQ
RSV_OPTION_HOST = _lsf.RSV_OPTION_HOST
RSV_OPTION_OPEN = _lsf.RSV_OPTION_OPEN
RSV_OPTION_DELETE = _lsf.RSV_OPTION_DELETE
RSV_OPTION_CLOSED = _lsf.RSV_OPTION_CLOSED
RSV_OPTION_EXEC = _lsf.RSV_OPTION_EXEC
RSV_OPTION_RMEXEC = _lsf.RSV_OPTION_RMEXEC
RSV_OPTION_NEXTINSTANCE = _lsf.RSV_OPTION_NEXTINSTANCE
RSV_OPTION_DISABLE = _lsf.RSV_OPTION_DISABLE
RSV_OPTION_ADDHOST = _lsf.RSV_OPTION_ADDHOST
RSV_OPTION_RMHOST = _lsf.RSV_OPTION_RMHOST
RSV_OPTION_DESCRIPTION = _lsf.RSV_OPTION_DESCRIPTION
RSV_OPTION_TWMOD = _lsf.RSV_OPTION_TWMOD
RSV_OPTION_SWITCHOPENCLOSE = _lsf.RSV_OPTION_SWITCHOPENCLOSE
RSV_OPTION_USERMOD = _lsf.RSV_OPTION_USERMOD
RSV_OPTION_RSVNAME = _lsf.RSV_OPTION_RSVNAME
RSV_OPTION_EXPIRED = _lsf.RSV_OPTION_EXPIRED
class addRsvRequest(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, addRsvRequest, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, addRsvRequest, name)
    __repr__ = _swig_repr
    __swig_setmethods__["options"] = _lsf.addRsvRequest_options_set
    __swig_getmethods__["options"] = _lsf.addRsvRequest_options_get
    if _newclass:options = property(_lsf.addRsvRequest_options_get, _lsf.addRsvRequest_options_set)
    __swig_setmethods__["name"] = _lsf.addRsvRequest_name_set
    __swig_getmethods__["name"] = _lsf.addRsvRequest_name_get
    if _newclass:name = property(_lsf.addRsvRequest_name_get, _lsf.addRsvRequest_name_set)
    __swig_setmethods__["numAskedHosts"] = _lsf.addRsvRequest_numAskedHosts_set
    __swig_getmethods__["numAskedHosts"] = _lsf.addRsvRequest_numAskedHosts_get
    if _newclass:numAskedHosts = property(_lsf.addRsvRequest_numAskedHosts_get, _lsf.addRsvRequest_numAskedHosts_set)
    __swig_setmethods__["askedHosts"] = _lsf.addRsvRequest_askedHosts_set
    __swig_getmethods__["askedHosts"] = _lsf.addRsvRequest_askedHosts_get
    if _newclass:askedHosts = property(_lsf.addRsvRequest_askedHosts_get, _lsf.addRsvRequest_askedHosts_set)
    __swig_setmethods__["resReq"] = _lsf.addRsvRequest_resReq_set
    __swig_getmethods__["resReq"] = _lsf.addRsvRequest_resReq_get
    if _newclass:resReq = property(_lsf.addRsvRequest_resReq_get, _lsf.addRsvRequest_resReq_set)
    __swig_setmethods__["timeWindow"] = _lsf.addRsvRequest_timeWindow_set
    __swig_getmethods__["timeWindow"] = _lsf.addRsvRequest_timeWindow_get
    if _newclass:timeWindow = property(_lsf.addRsvRequest_timeWindow_get, _lsf.addRsvRequest_timeWindow_set)
    __swig_setmethods__["execCmd"] = _lsf.addRsvRequest_execCmd_set
    __swig_getmethods__["execCmd"] = _lsf.addRsvRequest_execCmd_get
    if _newclass:execCmd = property(_lsf.addRsvRequest_execCmd_get, _lsf.addRsvRequest_execCmd_set)
    __swig_setmethods__["desc"] = _lsf.addRsvRequest_desc_set
    __swig_getmethods__["desc"] = _lsf.addRsvRequest_desc_get
    if _newclass:desc = property(_lsf.addRsvRequest_desc_get, _lsf.addRsvRequest_desc_set)
    __swig_setmethods__["rsvName"] = _lsf.addRsvRequest_rsvName_set
    __swig_getmethods__["rsvName"] = _lsf.addRsvRequest_rsvName_get
    if _newclass:rsvName = property(_lsf.addRsvRequest_rsvName_get, _lsf.addRsvRequest_rsvName_set)
    __swig_getmethods__["procRange"] = _lsf.addRsvRequest_procRange_get
    if _newclass:procRange = property(_lsf.addRsvRequest_procRange_get)
    def __init__(self, *args): 
        this = _lsf.new_addRsvRequest(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _lsf.delete_addRsvRequest
    __del__ = lambda self : None;
addRsvRequest_swigregister = _lsf.addRsvRequest_swigregister
addRsvRequest_swigregister(addRsvRequest)

class addRsvRequest_procRange(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, addRsvRequest_procRange, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, addRsvRequest_procRange, name)
    __repr__ = _swig_repr
    __swig_setmethods__["minNumProcs"] = _lsf.addRsvRequest_procRange_minNumProcs_set
    __swig_getmethods__["minNumProcs"] = _lsf.addRsvRequest_procRange_minNumProcs_get
    if _newclass:minNumProcs = property(_lsf.addRsvRequest_procRange_minNumProcs_get, _lsf.addRsvRequest_procRange_minNumProcs_set)
    __swig_setmethods__["maxNumProcs"] = _lsf.addRsvRequest_procRange_maxNumProcs_set
    __swig_getmethods__["maxNumProcs"] = _lsf.addRsvRequest_procRange_maxNumProcs_get
    if _newclass:maxNumProcs = property(_lsf.addRsvRequest_procRange_maxNumProcs_get, _lsf.addRsvRequest_procRange_maxNumProcs_set)
    def __init__(self, *args): 
        this = _lsf.new_addRsvRequest_procRange(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _lsf.delete_addRsvRequest_procRange
    __del__ = lambda self : None;
addRsvRequest_procRange_swigregister = _lsf.addRsvRequest_procRange_swigregister
addRsvRequest_procRange_swigregister(addRsvRequest_procRange)

class rmRsvRequest(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, rmRsvRequest, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, rmRsvRequest, name)
    __repr__ = _swig_repr
    __swig_setmethods__["rsvId"] = _lsf.rmRsvRequest_rsvId_set
    __swig_getmethods__["rsvId"] = _lsf.rmRsvRequest_rsvId_get
    if _newclass:rsvId = property(_lsf.rmRsvRequest_rsvId_get, _lsf.rmRsvRequest_rsvId_set)
    def __init__(self, *args): 
        this = _lsf.new_rmRsvRequest(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _lsf.delete_rmRsvRequest
    __del__ = lambda self : None;
rmRsvRequest_swigregister = _lsf.rmRsvRequest_swigregister
rmRsvRequest_swigregister(rmRsvRequest)

class modRsvRequest(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, modRsvRequest, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, modRsvRequest, name)
    __repr__ = _swig_repr
    __swig_setmethods__["rsvId"] = _lsf.modRsvRequest_rsvId_set
    __swig_getmethods__["rsvId"] = _lsf.modRsvRequest_rsvId_get
    if _newclass:rsvId = property(_lsf.modRsvRequest_rsvId_get, _lsf.modRsvRequest_rsvId_set)
    __swig_setmethods__["fieldsFromAddReq"] = _lsf.modRsvRequest_fieldsFromAddReq_set
    __swig_getmethods__["fieldsFromAddReq"] = _lsf.modRsvRequest_fieldsFromAddReq_get
    if _newclass:fieldsFromAddReq = property(_lsf.modRsvRequest_fieldsFromAddReq_get, _lsf.modRsvRequest_fieldsFromAddReq_set)
    __swig_setmethods__["disabledDuration"] = _lsf.modRsvRequest_disabledDuration_set
    __swig_getmethods__["disabledDuration"] = _lsf.modRsvRequest_disabledDuration_get
    if _newclass:disabledDuration = property(_lsf.modRsvRequest_disabledDuration_get, _lsf.modRsvRequest_disabledDuration_set)
    def __init__(self, *args): 
        this = _lsf.new_modRsvRequest(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _lsf.delete_modRsvRequest
    __del__ = lambda self : None;
modRsvRequest_swigregister = _lsf.modRsvRequest_swigregister
modRsvRequest_swigregister(modRsvRequest)

class hostRsvInfoEnt(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, hostRsvInfoEnt, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, hostRsvInfoEnt, name)
    __repr__ = _swig_repr
    __swig_setmethods__["host"] = _lsf.hostRsvInfoEnt_host_set
    __swig_getmethods__["host"] = _lsf.hostRsvInfoEnt_host_get
    if _newclass:host = property(_lsf.hostRsvInfoEnt_host_get, _lsf.hostRsvInfoEnt_host_set)
    __swig_setmethods__["numCPUs"] = _lsf.hostRsvInfoEnt_numCPUs_set
    __swig_getmethods__["numCPUs"] = _lsf.hostRsvInfoEnt_numCPUs_get
    if _newclass:numCPUs = property(_lsf.hostRsvInfoEnt_numCPUs_get, _lsf.hostRsvInfoEnt_numCPUs_set)
    __swig_setmethods__["numSlots"] = _lsf.hostRsvInfoEnt_numSlots_set
    __swig_getmethods__["numSlots"] = _lsf.hostRsvInfoEnt_numSlots_get
    if _newclass:numSlots = property(_lsf.hostRsvInfoEnt_numSlots_get, _lsf.hostRsvInfoEnt_numSlots_set)
    __swig_setmethods__["numRsvProcs"] = _lsf.hostRsvInfoEnt_numRsvProcs_set
    __swig_getmethods__["numRsvProcs"] = _lsf.hostRsvInfoEnt_numRsvProcs_get
    if _newclass:numRsvProcs = property(_lsf.hostRsvInfoEnt_numRsvProcs_get, _lsf.hostRsvInfoEnt_numRsvProcs_set)
    __swig_setmethods__["numusedRsvProcs"] = _lsf.hostRsvInfoEnt_numusedRsvProcs_set
    __swig_getmethods__["numusedRsvProcs"] = _lsf.hostRsvInfoEnt_numusedRsvProcs_get
    if _newclass:numusedRsvProcs = property(_lsf.hostRsvInfoEnt_numusedRsvProcs_get, _lsf.hostRsvInfoEnt_numusedRsvProcs_set)
    __swig_setmethods__["numUsedProcs"] = _lsf.hostRsvInfoEnt_numUsedProcs_set
    __swig_getmethods__["numUsedProcs"] = _lsf.hostRsvInfoEnt_numUsedProcs_get
    if _newclass:numUsedProcs = property(_lsf.hostRsvInfoEnt_numUsedProcs_get, _lsf.hostRsvInfoEnt_numUsedProcs_set)
    def __init__(self, *args): 
        this = _lsf.new_hostRsvInfoEnt(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _lsf.delete_hostRsvInfoEnt
    __del__ = lambda self : None;
hostRsvInfoEnt_swigregister = _lsf.hostRsvInfoEnt_swigregister
hostRsvInfoEnt_swigregister(hostRsvInfoEnt)

class rsvInfoEnt(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, rsvInfoEnt, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, rsvInfoEnt, name)
    __repr__ = _swig_repr
    __swig_setmethods__["options"] = _lsf.rsvInfoEnt_options_set
    __swig_getmethods__["options"] = _lsf.rsvInfoEnt_options_get
    if _newclass:options = property(_lsf.rsvInfoEnt_options_get, _lsf.rsvInfoEnt_options_set)
    __swig_setmethods__["rsvId"] = _lsf.rsvInfoEnt_rsvId_set
    __swig_getmethods__["rsvId"] = _lsf.rsvInfoEnt_rsvId_get
    if _newclass:rsvId = property(_lsf.rsvInfoEnt_rsvId_get, _lsf.rsvInfoEnt_rsvId_set)
    __swig_setmethods__["name"] = _lsf.rsvInfoEnt_name_set
    __swig_getmethods__["name"] = _lsf.rsvInfoEnt_name_get
    if _newclass:name = property(_lsf.rsvInfoEnt_name_get, _lsf.rsvInfoEnt_name_set)
    __swig_setmethods__["numRsvHosts"] = _lsf.rsvInfoEnt_numRsvHosts_set
    __swig_getmethods__["numRsvHosts"] = _lsf.rsvInfoEnt_numRsvHosts_get
    if _newclass:numRsvHosts = property(_lsf.rsvInfoEnt_numRsvHosts_get, _lsf.rsvInfoEnt_numRsvHosts_set)
    __swig_setmethods__["rsvHosts"] = _lsf.rsvInfoEnt_rsvHosts_set
    __swig_getmethods__["rsvHosts"] = _lsf.rsvInfoEnt_rsvHosts_get
    if _newclass:rsvHosts = property(_lsf.rsvInfoEnt_rsvHosts_get, _lsf.rsvInfoEnt_rsvHosts_set)
    __swig_setmethods__["timeWindow"] = _lsf.rsvInfoEnt_timeWindow_set
    __swig_getmethods__["timeWindow"] = _lsf.rsvInfoEnt_timeWindow_get
    if _newclass:timeWindow = property(_lsf.rsvInfoEnt_timeWindow_get, _lsf.rsvInfoEnt_timeWindow_set)
    __swig_setmethods__["numRsvJobs"] = _lsf.rsvInfoEnt_numRsvJobs_set
    __swig_getmethods__["numRsvJobs"] = _lsf.rsvInfoEnt_numRsvJobs_get
    if _newclass:numRsvJobs = property(_lsf.rsvInfoEnt_numRsvJobs_get, _lsf.rsvInfoEnt_numRsvJobs_set)
    __swig_setmethods__["jobIds"] = _lsf.rsvInfoEnt_jobIds_set
    __swig_getmethods__["jobIds"] = _lsf.rsvInfoEnt_jobIds_get
    if _newclass:jobIds = property(_lsf.rsvInfoEnt_jobIds_get, _lsf.rsvInfoEnt_jobIds_set)
    __swig_setmethods__["jobStatus"] = _lsf.rsvInfoEnt_jobStatus_set
    __swig_getmethods__["jobStatus"] = _lsf.rsvInfoEnt_jobStatus_get
    if _newclass:jobStatus = property(_lsf.rsvInfoEnt_jobStatus_get, _lsf.rsvInfoEnt_jobStatus_set)
    __swig_setmethods__["desc"] = _lsf.rsvInfoEnt_desc_set
    __swig_getmethods__["desc"] = _lsf.rsvInfoEnt_desc_get
    if _newclass:desc = property(_lsf.rsvInfoEnt_desc_get, _lsf.rsvInfoEnt_desc_set)
    __swig_setmethods__["disabledDurations"] = _lsf.rsvInfoEnt_disabledDurations_set
    __swig_getmethods__["disabledDurations"] = _lsf.rsvInfoEnt_disabledDurations_get
    if _newclass:disabledDurations = property(_lsf.rsvInfoEnt_disabledDurations_get, _lsf.rsvInfoEnt_disabledDurations_set)
    __swig_setmethods__["state"] = _lsf.rsvInfoEnt_state_set
    __swig_getmethods__["state"] = _lsf.rsvInfoEnt_state_get
    if _newclass:state = property(_lsf.rsvInfoEnt_state_get, _lsf.rsvInfoEnt_state_set)
    __swig_setmethods__["nextInstance"] = _lsf.rsvInfoEnt_nextInstance_set
    __swig_getmethods__["nextInstance"] = _lsf.rsvInfoEnt_nextInstance_get
    if _newclass:nextInstance = property(_lsf.rsvInfoEnt_nextInstance_get, _lsf.rsvInfoEnt_nextInstance_set)
    __swig_setmethods__["creator"] = _lsf.rsvInfoEnt_creator_set
    __swig_getmethods__["creator"] = _lsf.rsvInfoEnt_creator_get
    if _newclass:creator = property(_lsf.rsvInfoEnt_creator_get, _lsf.rsvInfoEnt_creator_set)
    def __init__(self, *args): 
        this = _lsf.new_rsvInfoEnt(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _lsf.delete_rsvInfoEnt
    __del__ = lambda self : None;
rsvInfoEnt_swigregister = _lsf.rsvInfoEnt_swigregister
rsvInfoEnt_swigregister(rsvInfoEnt)

class slotInfoRequest(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, slotInfoRequest, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, slotInfoRequest, name)
    __repr__ = _swig_repr
    __swig_setmethods__["options"] = _lsf.slotInfoRequest_options_set
    __swig_getmethods__["options"] = _lsf.slotInfoRequest_options_get
    if _newclass:options = property(_lsf.slotInfoRequest_options_get, _lsf.slotInfoRequest_options_set)
    __swig_setmethods__["resReq"] = _lsf.slotInfoRequest_resReq_set
    __swig_getmethods__["resReq"] = _lsf.slotInfoRequest_resReq_get
    if _newclass:resReq = property(_lsf.slotInfoRequest_resReq_get, _lsf.slotInfoRequest_resReq_set)
    def __init__(self, *args): 
        this = _lsf.new_slotInfoRequest(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _lsf.delete_slotInfoRequest
    __del__ = lambda self : None;
slotInfoRequest_swigregister = _lsf.slotInfoRequest_swigregister
slotInfoRequest_swigregister(slotInfoRequest)
SLOT_OPTION_RESREQ = _lsf.SLOT_OPTION_RESREQ

class SRInfoEnt(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, SRInfoEnt, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, SRInfoEnt, name)
    __repr__ = _swig_repr
    __swig_setmethods__["numReserved"] = _lsf.SRInfoEnt_numReserved_set
    __swig_getmethods__["numReserved"] = _lsf.SRInfoEnt_numReserved_get
    if _newclass:numReserved = property(_lsf.SRInfoEnt_numReserved_get, _lsf.SRInfoEnt_numReserved_set)
    __swig_setmethods__["predictedStartTime"] = _lsf.SRInfoEnt_predictedStartTime_set
    __swig_getmethods__["predictedStartTime"] = _lsf.SRInfoEnt_predictedStartTime_get
    if _newclass:predictedStartTime = property(_lsf.SRInfoEnt_predictedStartTime_get, _lsf.SRInfoEnt_predictedStartTime_set)
    def __init__(self, *args): 
        this = _lsf.new_SRInfoEnt(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _lsf.delete_SRInfoEnt
    __del__ = lambda self : None;
SRInfoEnt_swigregister = _lsf.SRInfoEnt_swigregister
SRInfoEnt_swigregister(SRInfoEnt)

class hostSRInfoEnt(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, hostSRInfoEnt, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, hostSRInfoEnt, name)
    __repr__ = _swig_repr
    __swig_setmethods__["host"] = _lsf.hostSRInfoEnt_host_set
    __swig_getmethods__["host"] = _lsf.hostSRInfoEnt_host_get
    if _newclass:host = property(_lsf.hostSRInfoEnt_host_get, _lsf.hostSRInfoEnt_host_set)
    __swig_setmethods__["hStatus"] = _lsf.hostSRInfoEnt_hStatus_set
    __swig_getmethods__["hStatus"] = _lsf.hostSRInfoEnt_hStatus_get
    if _newclass:hStatus = property(_lsf.hostSRInfoEnt_hStatus_get, _lsf.hostSRInfoEnt_hStatus_set)
    __swig_setmethods__["userJobLimit"] = _lsf.hostSRInfoEnt_userJobLimit_set
    __swig_getmethods__["userJobLimit"] = _lsf.hostSRInfoEnt_userJobLimit_get
    if _newclass:userJobLimit = property(_lsf.hostSRInfoEnt_userJobLimit_get, _lsf.hostSRInfoEnt_userJobLimit_set)
    __swig_setmethods__["maxJobs"] = _lsf.hostSRInfoEnt_maxJobs_set
    __swig_getmethods__["maxJobs"] = _lsf.hostSRInfoEnt_maxJobs_get
    if _newclass:maxJobs = property(_lsf.hostSRInfoEnt_maxJobs_get, _lsf.hostSRInfoEnt_maxJobs_set)
    __swig_setmethods__["numJobs"] = _lsf.hostSRInfoEnt_numJobs_set
    __swig_getmethods__["numJobs"] = _lsf.hostSRInfoEnt_numJobs_get
    if _newclass:numJobs = property(_lsf.hostSRInfoEnt_numJobs_get, _lsf.hostSRInfoEnt_numJobs_set)
    __swig_setmethods__["numRUN"] = _lsf.hostSRInfoEnt_numRUN_set
    __swig_getmethods__["numRUN"] = _lsf.hostSRInfoEnt_numRUN_get
    if _newclass:numRUN = property(_lsf.hostSRInfoEnt_numRUN_get, _lsf.hostSRInfoEnt_numRUN_set)
    __swig_setmethods__["numSSUSP"] = _lsf.hostSRInfoEnt_numSSUSP_set
    __swig_getmethods__["numSSUSP"] = _lsf.hostSRInfoEnt_numSSUSP_get
    if _newclass:numSSUSP = property(_lsf.hostSRInfoEnt_numSSUSP_get, _lsf.hostSRInfoEnt_numSSUSP_set)
    __swig_setmethods__["numUSUSP"] = _lsf.hostSRInfoEnt_numUSUSP_set
    __swig_getmethods__["numUSUSP"] = _lsf.hostSRInfoEnt_numUSUSP_get
    if _newclass:numUSUSP = property(_lsf.hostSRInfoEnt_numUSUSP_get, _lsf.hostSRInfoEnt_numUSUSP_set)
    __swig_setmethods__["numRESERVE"] = _lsf.hostSRInfoEnt_numRESERVE_set
    __swig_getmethods__["numRESERVE"] = _lsf.hostSRInfoEnt_numRESERVE_get
    if _newclass:numRESERVE = property(_lsf.hostSRInfoEnt_numRESERVE_get, _lsf.hostSRInfoEnt_numRESERVE_set)
    __swig_setmethods__["numSR"] = _lsf.hostSRInfoEnt_numSR_set
    __swig_getmethods__["numSR"] = _lsf.hostSRInfoEnt_numSR_get
    if _newclass:numSR = property(_lsf.hostSRInfoEnt_numSR_get, _lsf.hostSRInfoEnt_numSR_set)
    __swig_setmethods__["SRInfo"] = _lsf.hostSRInfoEnt_SRInfo_set
    __swig_getmethods__["SRInfo"] = _lsf.hostSRInfoEnt_SRInfo_get
    if _newclass:SRInfo = property(_lsf.hostSRInfoEnt_SRInfo_get, _lsf.hostSRInfoEnt_SRInfo_set)
    __swig_setmethods__["numRELEASE"] = _lsf.hostSRInfoEnt_numRELEASE_set
    __swig_getmethods__["numRELEASE"] = _lsf.hostSRInfoEnt_numRELEASE_get
    if _newclass:numRELEASE = property(_lsf.hostSRInfoEnt_numRELEASE_get, _lsf.hostSRInfoEnt_numRELEASE_set)
    def __init__(self, *args): 
        this = _lsf.new_hostSRInfoEnt(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _lsf.delete_hostSRInfoEnt
    __del__ = lambda self : None;
hostSRInfoEnt_swigregister = _lsf.hostSRInfoEnt_swigregister
hostSRInfoEnt_swigregister(hostSRInfoEnt)

class slotInfoReply(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, slotInfoReply, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, slotInfoReply, name)
    __repr__ = _swig_repr
    __swig_setmethods__["masterTime"] = _lsf.slotInfoReply_masterTime_set
    __swig_getmethods__["masterTime"] = _lsf.slotInfoReply_masterTime_get
    if _newclass:masterTime = property(_lsf.slotInfoReply_masterTime_get, _lsf.slotInfoReply_masterTime_set)
    __swig_setmethods__["numHosts"] = _lsf.slotInfoReply_numHosts_set
    __swig_getmethods__["numHosts"] = _lsf.slotInfoReply_numHosts_get
    if _newclass:numHosts = property(_lsf.slotInfoReply_numHosts_get, _lsf.slotInfoReply_numHosts_set)
    __swig_setmethods__["hostInfo"] = _lsf.slotInfoReply_hostInfo_set
    __swig_getmethods__["hostInfo"] = _lsf.slotInfoReply_hostInfo_get
    if _newclass:hostInfo = property(_lsf.slotInfoReply_hostInfo_get, _lsf.slotInfoReply_hostInfo_set)
    __swig_setmethods__["numAR"] = _lsf.slotInfoReply_numAR_set
    __swig_getmethods__["numAR"] = _lsf.slotInfoReply_numAR_get
    if _newclass:numAR = property(_lsf.slotInfoReply_numAR_get, _lsf.slotInfoReply_numAR_set)
    __swig_setmethods__["ARInfo"] = _lsf.slotInfoReply_ARInfo_set
    __swig_getmethods__["ARInfo"] = _lsf.slotInfoReply_ARInfo_get
    if _newclass:ARInfo = property(_lsf.slotInfoReply_ARInfo_get, _lsf.slotInfoReply_ARInfo_set)
    def __init__(self, *args): 
        this = _lsf.new_slotInfoReply(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _lsf.delete_slotInfoReply
    __del__ = lambda self : None;
slotInfoReply_swigregister = _lsf.slotInfoReply_swigregister
slotInfoReply_swigregister(slotInfoReply)

LSB_RSRC_LIMIT_TYPE_SLOTS = _lsf.LSB_RSRC_LIMIT_TYPE_SLOTS
LSB_RSRC_LIMIT_TYPE_SLOT_PERPSR = _lsf.LSB_RSRC_LIMIT_TYPE_SLOT_PERPSR
LSB_RSRC_LIMIT_TYPE_MEM = _lsf.LSB_RSRC_LIMIT_TYPE_MEM
LSB_RSRC_LIMIT_TYPE_MEM_PERCENT = _lsf.LSB_RSRC_LIMIT_TYPE_MEM_PERCENT
LSB_RSRC_LIMIT_TYPE_SWP = _lsf.LSB_RSRC_LIMIT_TYPE_SWP
LSB_RSRC_LIMIT_TYPE_SWP_PERCENT = _lsf.LSB_RSRC_LIMIT_TYPE_SWP_PERCENT
LSB_RSRC_LIMIT_TYPE_TMP = _lsf.LSB_RSRC_LIMIT_TYPE_TMP
LSB_RSRC_LIMIT_TYPE_TMP_PERCENT = _lsf.LSB_RSRC_LIMIT_TYPE_TMP_PERCENT
LSB_RSRC_LIMIT_TYPE_JOBS = _lsf.LSB_RSRC_LIMIT_TYPE_JOBS
LSB_RSRC_LIMIT_TYPE_EXT_RSRC = _lsf.LSB_RSRC_LIMIT_TYPE_EXT_RSRC
LIMIT_QUEUES = _lsf.LIMIT_QUEUES
LIMIT_PER_QUEUE = _lsf.LIMIT_PER_QUEUE
LIMIT_USERS = _lsf.LIMIT_USERS
LIMIT_PER_USER = _lsf.LIMIT_PER_USER
LIMIT_HOSTS = _lsf.LIMIT_HOSTS
LIMIT_PER_HOST = _lsf.LIMIT_PER_HOST
LIMIT_PROJECTS = _lsf.LIMIT_PROJECTS
LIMIT_PER_PROJECT = _lsf.LIMIT_PER_PROJECT
LIMIT_LIC_PROJECTS = _lsf.LIMIT_LIC_PROJECTS
LIMIT_PER_LIC_PROJECT = _lsf.LIMIT_PER_LIC_PROJECT
class limitConsumer(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, limitConsumer, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, limitConsumer, name)
    __repr__ = _swig_repr
    __swig_setmethods__["type"] = _lsf.limitConsumer_type_set
    __swig_getmethods__["type"] = _lsf.limitConsumer_type_get
    if _newclass:type = property(_lsf.limitConsumer_type_get, _lsf.limitConsumer_type_set)
    __swig_setmethods__["name"] = _lsf.limitConsumer_name_set
    __swig_getmethods__["name"] = _lsf.limitConsumer_name_get
    if _newclass:name = property(_lsf.limitConsumer_name_get, _lsf.limitConsumer_name_set)
    def __init__(self, *args): 
        this = _lsf.new_limitConsumer(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _lsf.delete_limitConsumer
    __del__ = lambda self : None;
limitConsumer_swigregister = _lsf.limitConsumer_swigregister
limitConsumer_swigregister(limitConsumer)

class limitResource(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, limitResource, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, limitResource, name)
    __repr__ = _swig_repr
    __swig_setmethods__["name"] = _lsf.limitResource_name_set
    __swig_getmethods__["name"] = _lsf.limitResource_name_get
    if _newclass:name = property(_lsf.limitResource_name_get, _lsf.limitResource_name_set)
    __swig_setmethods__["type"] = _lsf.limitResource_type_set
    __swig_getmethods__["type"] = _lsf.limitResource_type_get
    if _newclass:type = property(_lsf.limitResource_type_get, _lsf.limitResource_type_set)
    __swig_setmethods__["val"] = _lsf.limitResource_val_set
    __swig_getmethods__["val"] = _lsf.limitResource_val_get
    if _newclass:val = property(_lsf.limitResource_val_get, _lsf.limitResource_val_set)
    def __init__(self, *args): 
        this = _lsf.new_limitResource(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _lsf.delete_limitResource
    __del__ = lambda self : None;
limitResource_swigregister = _lsf.limitResource_swigregister
limitResource_swigregister(limitResource)

class limitInfoReq(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, limitInfoReq, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, limitInfoReq, name)
    __repr__ = _swig_repr
    __swig_setmethods__["name"] = _lsf.limitInfoReq_name_set
    __swig_getmethods__["name"] = _lsf.limitInfoReq_name_get
    if _newclass:name = property(_lsf.limitInfoReq_name_get, _lsf.limitInfoReq_name_set)
    __swig_setmethods__["consumerC"] = _lsf.limitInfoReq_consumerC_set
    __swig_getmethods__["consumerC"] = _lsf.limitInfoReq_consumerC_get
    if _newclass:consumerC = property(_lsf.limitInfoReq_consumerC_get, _lsf.limitInfoReq_consumerC_set)
    __swig_setmethods__["consumerV"] = _lsf.limitInfoReq_consumerV_set
    __swig_getmethods__["consumerV"] = _lsf.limitInfoReq_consumerV_get
    if _newclass:consumerV = property(_lsf.limitInfoReq_consumerV_get, _lsf.limitInfoReq_consumerV_set)
    def __init__(self, *args): 
        this = _lsf.new_limitInfoReq(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _lsf.delete_limitInfoReq
    __del__ = lambda self : None;
limitInfoReq_swigregister = _lsf.limitInfoReq_swigregister
limitInfoReq_swigregister(limitInfoReq)

class limitItem(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, limitItem, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, limitItem, name)
    __repr__ = _swig_repr
    __swig_setmethods__["consumerC"] = _lsf.limitItem_consumerC_set
    __swig_getmethods__["consumerC"] = _lsf.limitItem_consumerC_get
    if _newclass:consumerC = property(_lsf.limitItem_consumerC_get, _lsf.limitItem_consumerC_set)
    __swig_setmethods__["consumerV"] = _lsf.limitItem_consumerV_set
    __swig_getmethods__["consumerV"] = _lsf.limitItem_consumerV_get
    if _newclass:consumerV = property(_lsf.limitItem_consumerV_get, _lsf.limitItem_consumerV_set)
    __swig_setmethods__["resourceC"] = _lsf.limitItem_resourceC_set
    __swig_getmethods__["resourceC"] = _lsf.limitItem_resourceC_get
    if _newclass:resourceC = property(_lsf.limitItem_resourceC_get, _lsf.limitItem_resourceC_set)
    __swig_setmethods__["resourceV"] = _lsf.limitItem_resourceV_set
    __swig_getmethods__["resourceV"] = _lsf.limitItem_resourceV_get
    if _newclass:resourceV = property(_lsf.limitItem_resourceV_get, _lsf.limitItem_resourceV_set)
    def __init__(self, *args): 
        this = _lsf.new_limitItem(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _lsf.delete_limitItem
    __del__ = lambda self : None;
limitItem_swigregister = _lsf.limitItem_swigregister
limitItem_swigregister(limitItem)

class limitInfoEnt(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, limitInfoEnt, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, limitInfoEnt, name)
    __repr__ = _swig_repr
    __swig_setmethods__["name"] = _lsf.limitInfoEnt_name_set
    __swig_getmethods__["name"] = _lsf.limitInfoEnt_name_get
    if _newclass:name = property(_lsf.limitInfoEnt_name_get, _lsf.limitInfoEnt_name_set)
    __swig_setmethods__["confInfo"] = _lsf.limitInfoEnt_confInfo_set
    __swig_getmethods__["confInfo"] = _lsf.limitInfoEnt_confInfo_get
    if _newclass:confInfo = property(_lsf.limitInfoEnt_confInfo_get, _lsf.limitInfoEnt_confInfo_set)
    __swig_setmethods__["usageC"] = _lsf.limitInfoEnt_usageC_set
    __swig_getmethods__["usageC"] = _lsf.limitInfoEnt_usageC_get
    if _newclass:usageC = property(_lsf.limitInfoEnt_usageC_get, _lsf.limitInfoEnt_usageC_set)
    __swig_setmethods__["usageInfo"] = _lsf.limitInfoEnt_usageInfo_set
    __swig_getmethods__["usageInfo"] = _lsf.limitInfoEnt_usageInfo_get
    if _newclass:usageInfo = property(_lsf.limitInfoEnt_usageInfo_get, _lsf.limitInfoEnt_usageInfo_set)
    def __init__(self, *args): 
        this = _lsf.new_limitInfoEnt(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _lsf.delete_limitInfoEnt
    __del__ = lambda self : None;
limitInfoEnt_swigregister = _lsf.limitInfoEnt_swigregister
limitInfoEnt_swigregister(limitInfoEnt)

ADD_THRESHOLD = _lsf.ADD_THRESHOLD
GET_THRESHOLD = _lsf.GET_THRESHOLD
DEL_THRESHOLD = _lsf.DEL_THRESHOLD
UPD_THRESHOLD = _lsf.UPD_THRESHOLD
CHK_THRESHOLD = _lsf.CHK_THRESHOLD
class thresholdEntry(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, thresholdEntry, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, thresholdEntry, name)
    __repr__ = _swig_repr
    __swig_setmethods__["attr"] = _lsf.thresholdEntry_attr_set
    __swig_getmethods__["attr"] = _lsf.thresholdEntry_attr_get
    if _newclass:attr = property(_lsf.thresholdEntry_attr_get, _lsf.thresholdEntry_attr_set)
    __swig_setmethods__["hostEntryPtr"] = _lsf.thresholdEntry_hostEntryPtr_set
    __swig_getmethods__["hostEntryPtr"] = _lsf.thresholdEntry_hostEntryPtr_get
    if _newclass:hostEntryPtr = property(_lsf.thresholdEntry_hostEntryPtr_get, _lsf.thresholdEntry_hostEntryPtr_set)
    def __init__(self, *args): 
        this = _lsf.new_thresholdEntry(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _lsf.delete_thresholdEntry
    __del__ = lambda self : None;
thresholdEntry_swigregister = _lsf.thresholdEntry_swigregister
thresholdEntry_swigregister(thresholdEntry)

lsb_limitInfo = _lsf.lsb_limitInfo
lsb_freeLimitInfoEnt = _lsf.lsb_freeLimitInfoEnt
LSB_RESIZE_REL_NONE = _lsf.LSB_RESIZE_REL_NONE
LSB_RESIZE_REL_ALL = _lsf.LSB_RESIZE_REL_ALL
LSB_RESIZE_REL_CANCEL = _lsf.LSB_RESIZE_REL_CANCEL
LSB_RESIZE_REL_NO_NOTIFY = _lsf.LSB_RESIZE_REL_NO_NOTIFY
class job_resize_release(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, job_resize_release, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, job_resize_release, name)
    __repr__ = _swig_repr
    __swig_setmethods__["jobId"] = _lsf.job_resize_release_jobId_set
    __swig_getmethods__["jobId"] = _lsf.job_resize_release_jobId_get
    if _newclass:jobId = property(_lsf.job_resize_release_jobId_get, _lsf.job_resize_release_jobId_set)
    __swig_setmethods__["options"] = _lsf.job_resize_release_options_set
    __swig_getmethods__["options"] = _lsf.job_resize_release_options_get
    if _newclass:options = property(_lsf.job_resize_release_options_get, _lsf.job_resize_release_options_set)
    __swig_setmethods__["nHosts"] = _lsf.job_resize_release_nHosts_set
    __swig_getmethods__["nHosts"] = _lsf.job_resize_release_nHosts_get
    if _newclass:nHosts = property(_lsf.job_resize_release_nHosts_get, _lsf.job_resize_release_nHosts_set)
    __swig_setmethods__["hosts"] = _lsf.job_resize_release_hosts_set
    __swig_getmethods__["hosts"] = _lsf.job_resize_release_hosts_get
    if _newclass:hosts = property(_lsf.job_resize_release_hosts_get, _lsf.job_resize_release_hosts_set)
    __swig_setmethods__["slots"] = _lsf.job_resize_release_slots_set
    __swig_getmethods__["slots"] = _lsf.job_resize_release_slots_get
    if _newclass:slots = property(_lsf.job_resize_release_slots_get, _lsf.job_resize_release_slots_set)
    __swig_setmethods__["notifyCmd"] = _lsf.job_resize_release_notifyCmd_set
    __swig_getmethods__["notifyCmd"] = _lsf.job_resize_release_notifyCmd_get
    if _newclass:notifyCmd = property(_lsf.job_resize_release_notifyCmd_get, _lsf.job_resize_release_notifyCmd_set)
    def __init__(self, *args): 
        this = _lsf.new_job_resize_release(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _lsf.delete_job_resize_release
    __del__ = lambda self : None;
job_resize_release_swigregister = _lsf.job_resize_release_swigregister
job_resize_release_swigregister(job_resize_release)

class job_resize_request(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, job_resize_request, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, job_resize_request, name)
    __repr__ = _swig_repr
    __swig_setmethods__["jobId"] = _lsf.job_resize_request_jobId_set
    __swig_getmethods__["jobId"] = _lsf.job_resize_request_jobId_get
    if _newclass:jobId = property(_lsf.job_resize_request_jobId_get, _lsf.job_resize_request_jobId_set)
    __swig_setmethods__["options"] = _lsf.job_resize_request_options_set
    __swig_getmethods__["options"] = _lsf.job_resize_request_options_get
    if _newclass:options = property(_lsf.job_resize_request_options_get, _lsf.job_resize_request_options_set)
    __swig_setmethods__["nHosts"] = _lsf.job_resize_request_nHosts_set
    __swig_getmethods__["nHosts"] = _lsf.job_resize_request_nHosts_get
    if _newclass:nHosts = property(_lsf.job_resize_request_nHosts_get, _lsf.job_resize_request_nHosts_set)
    __swig_setmethods__["hosts"] = _lsf.job_resize_request_hosts_set
    __swig_getmethods__["hosts"] = _lsf.job_resize_request_hosts_get
    if _newclass:hosts = property(_lsf.job_resize_request_hosts_get, _lsf.job_resize_request_hosts_set)
    __swig_setmethods__["notifyCmd"] = _lsf.job_resize_request_notifyCmd_set
    __swig_getmethods__["notifyCmd"] = _lsf.job_resize_request_notifyCmd_get
    if _newclass:notifyCmd = property(_lsf.job_resize_request_notifyCmd_get, _lsf.job_resize_request_notifyCmd_set)
    def __init__(self, *args): 
        this = _lsf.new_job_resize_request(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _lsf.delete_job_resize_request
    __del__ = lambda self : None;
job_resize_request_swigregister = _lsf.job_resize_request_swigregister
job_resize_request_swigregister(job_resize_request)

QUERY_DEPEND_RECURSIVELY = _lsf.QUERY_DEPEND_RECURSIVELY
QUERY_DEPEND_DETAIL = _lsf.QUERY_DEPEND_DETAIL
QUERY_DEPEND_UNSATISFIED = _lsf.QUERY_DEPEND_UNSATISFIED
QUERY_DEPEND_CHILD = _lsf.QUERY_DEPEND_CHILD
class jobDepRequest(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, jobDepRequest, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, jobDepRequest, name)
    __repr__ = _swig_repr
    __swig_setmethods__["jobId"] = _lsf.jobDepRequest_jobId_set
    __swig_getmethods__["jobId"] = _lsf.jobDepRequest_jobId_get
    if _newclass:jobId = property(_lsf.jobDepRequest_jobId_get, _lsf.jobDepRequest_jobId_set)
    __swig_setmethods__["options"] = _lsf.jobDepRequest_options_set
    __swig_getmethods__["options"] = _lsf.jobDepRequest_options_get
    if _newclass:options = property(_lsf.jobDepRequest_options_get, _lsf.jobDepRequest_options_set)
    __swig_setmethods__["level"] = _lsf.jobDepRequest_level_set
    __swig_getmethods__["level"] = _lsf.jobDepRequest_level_get
    if _newclass:level = property(_lsf.jobDepRequest_level_get, _lsf.jobDepRequest_level_set)
    def __init__(self, *args): 
        this = _lsf.new_jobDepRequest(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _lsf.delete_jobDepRequest
    __del__ = lambda self : None;
jobDepRequest_swigregister = _lsf.jobDepRequest_swigregister
jobDepRequest_swigregister(jobDepRequest)

class queriedJobs(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, queriedJobs, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, queriedJobs, name)
    __repr__ = _swig_repr
    __swig_setmethods__["jobId"] = _lsf.queriedJobs_jobId_set
    __swig_getmethods__["jobId"] = _lsf.queriedJobs_jobId_get
    if _newclass:jobId = property(_lsf.queriedJobs_jobId_get, _lsf.queriedJobs_jobId_set)
    __swig_setmethods__["dependcondition"] = _lsf.queriedJobs_dependcondition_set
    __swig_getmethods__["dependcondition"] = _lsf.queriedJobs_dependcondition_get
    if _newclass:dependcondition = property(_lsf.queriedJobs_dependcondition_get, _lsf.queriedJobs_dependcondition_set)
    __swig_setmethods__["satisfied"] = _lsf.queriedJobs_satisfied_set
    __swig_getmethods__["satisfied"] = _lsf.queriedJobs_satisfied_get
    if _newclass:satisfied = property(_lsf.queriedJobs_satisfied_get, _lsf.queriedJobs_satisfied_set)
    def __init__(self, *args): 
        this = _lsf.new_queriedJobs(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _lsf.delete_queriedJobs
    __del__ = lambda self : None;
queriedJobs_swigregister = _lsf.queriedJobs_swigregister
queriedJobs_swigregister(queriedJobs)

JOB_HAS_DEPENDENCY = _lsf.JOB_HAS_DEPENDENCY
JOB_HAS_INDIVIDUAL_CONDITION = _lsf.JOB_HAS_INDIVIDUAL_CONDITION
class dependJobs(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, dependJobs, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, dependJobs, name)
    __repr__ = _swig_repr
    __swig_setmethods__["jobId"] = _lsf.dependJobs_jobId_set
    __swig_getmethods__["jobId"] = _lsf.dependJobs_jobId_get
    if _newclass:jobId = property(_lsf.dependJobs_jobId_get, _lsf.dependJobs_jobId_set)
    __swig_setmethods__["jobname"] = _lsf.dependJobs_jobname_set
    __swig_getmethods__["jobname"] = _lsf.dependJobs_jobname_get
    if _newclass:jobname = property(_lsf.dependJobs_jobname_get, _lsf.dependJobs_jobname_set)
    __swig_setmethods__["level"] = _lsf.dependJobs_level_set
    __swig_getmethods__["level"] = _lsf.dependJobs_level_get
    if _newclass:level = property(_lsf.dependJobs_level_get, _lsf.dependJobs_level_set)
    __swig_setmethods__["jobstatus"] = _lsf.dependJobs_jobstatus_set
    __swig_getmethods__["jobstatus"] = _lsf.dependJobs_jobstatus_get
    if _newclass:jobstatus = property(_lsf.dependJobs_jobstatus_get, _lsf.dependJobs_jobstatus_set)
    __swig_setmethods__["hasDependency"] = _lsf.dependJobs_hasDependency_set
    __swig_getmethods__["hasDependency"] = _lsf.dependJobs_hasDependency_get
    if _newclass:hasDependency = property(_lsf.dependJobs_hasDependency_get, _lsf.dependJobs_hasDependency_set)
    __swig_setmethods__["condition"] = _lsf.dependJobs_condition_set
    __swig_getmethods__["condition"] = _lsf.dependJobs_condition_get
    if _newclass:condition = property(_lsf.dependJobs_condition_get, _lsf.dependJobs_condition_set)
    __swig_setmethods__["satisfied"] = _lsf.dependJobs_satisfied_set
    __swig_getmethods__["satisfied"] = _lsf.dependJobs_satisfied_get
    if _newclass:satisfied = property(_lsf.dependJobs_satisfied_get, _lsf.dependJobs_satisfied_set)
    __swig_setmethods__["depJobId"] = _lsf.dependJobs_depJobId_set
    __swig_getmethods__["depJobId"] = _lsf.dependJobs_depJobId_get
    if _newclass:depJobId = property(_lsf.dependJobs_depJobId_get, _lsf.dependJobs_depJobId_set)
    def __init__(self, *args): 
        this = _lsf.new_dependJobs(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _lsf.delete_dependJobs
    __del__ = lambda self : None;
dependJobs_swigregister = _lsf.dependJobs_swigregister
dependJobs_swigregister(dependJobs)

class jobDependInfo(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, jobDependInfo, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, jobDependInfo, name)
    __repr__ = _swig_repr
    __swig_setmethods__["options"] = _lsf.jobDependInfo_options_set
    __swig_getmethods__["options"] = _lsf.jobDependInfo_options_get
    if _newclass:options = property(_lsf.jobDependInfo_options_get, _lsf.jobDependInfo_options_set)
    __swig_setmethods__["numQueriedJobs"] = _lsf.jobDependInfo_numQueriedJobs_set
    __swig_getmethods__["numQueriedJobs"] = _lsf.jobDependInfo_numQueriedJobs_get
    if _newclass:numQueriedJobs = property(_lsf.jobDependInfo_numQueriedJobs_get, _lsf.jobDependInfo_numQueriedJobs_set)
    __swig_setmethods__["queriedJobs"] = _lsf.jobDependInfo_queriedJobs_set
    __swig_getmethods__["queriedJobs"] = _lsf.jobDependInfo_queriedJobs_get
    if _newclass:queriedJobs = property(_lsf.jobDependInfo_queriedJobs_get, _lsf.jobDependInfo_queriedJobs_set)
    __swig_setmethods__["level"] = _lsf.jobDependInfo_level_set
    __swig_getmethods__["level"] = _lsf.jobDependInfo_level_get
    if _newclass:level = property(_lsf.jobDependInfo_level_get, _lsf.jobDependInfo_level_set)
    __swig_setmethods__["numJobs"] = _lsf.jobDependInfo_numJobs_set
    __swig_getmethods__["numJobs"] = _lsf.jobDependInfo_numJobs_get
    if _newclass:numJobs = property(_lsf.jobDependInfo_numJobs_get, _lsf.jobDependInfo_numJobs_set)
    __swig_setmethods__["depJobs"] = _lsf.jobDependInfo_depJobs_set
    __swig_getmethods__["depJobs"] = _lsf.jobDependInfo_depJobs_get
    if _newclass:depJobs = property(_lsf.jobDependInfo_depJobs_get, _lsf.jobDependInfo_depJobs_set)
    def __init__(self, *args): 
        this = _lsf.new_jobDependInfo(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _lsf.delete_jobDependInfo
    __del__ = lambda self : None;
jobDependInfo_swigregister = _lsf.jobDependInfo_swigregister
jobDependInfo_swigregister(jobDependInfo)

PRINT_SHORT_NAMELIST = _lsf.PRINT_SHORT_NAMELIST
PRINT_LONG_NAMELIST = _lsf.PRINT_LONG_NAMELIST
PRINT_MCPU_HOSTS = _lsf.PRINT_MCPU_HOSTS
class NAMELIST(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, NAMELIST, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, NAMELIST, name)
    __repr__ = _swig_repr
    __swig_setmethods__["listSize"] = _lsf.NAMELIST_listSize_set
    __swig_getmethods__["listSize"] = _lsf.NAMELIST_listSize_get
    if _newclass:listSize = property(_lsf.NAMELIST_listSize_get, _lsf.NAMELIST_listSize_set)
    __swig_setmethods__["names"] = _lsf.NAMELIST_names_set
    __swig_getmethods__["names"] = _lsf.NAMELIST_names_get
    if _newclass:names = property(_lsf.NAMELIST_names_get, _lsf.NAMELIST_names_set)
    __swig_setmethods__["counter"] = _lsf.NAMELIST_counter_set
    __swig_getmethods__["counter"] = _lsf.NAMELIST_counter_get
    if _newclass:counter = property(_lsf.NAMELIST_counter_get, _lsf.NAMELIST_counter_set)
    def __init__(self, *args): 
        this = _lsf.new_NAMELIST(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _lsf.delete_NAMELIST
    __del__ = lambda self : None;
NAMELIST_swigregister = _lsf.NAMELIST_swigregister
NAMELIST_swigregister(NAMELIST)

lsb_parseShortStr = _lsf.lsb_parseShortStr
lsb_parseLongStr = _lsf.lsb_parseLongStr
lsb_printNameList = _lsf.lsb_printNameList
lsb_compressStrList = _lsf.lsb_compressStrList
lsb_splitName = _lsf.lsb_splitName
lsb_errno = _lsf.lsb_errno
lsb_readparam = _lsf.lsb_readparam
lsb_readuser = _lsf.lsb_readuser
lsb_readuser_ex = _lsf.lsb_readuser_ex
lsb_readhost = _lsf.lsb_readhost
lsb_readqueue = _lsf.lsb_readqueue
updateClusterConf = _lsf.updateClusterConf
lsb_hostpartinfo = _lsf.lsb_hostpartinfo
lsb_init = _lsf.lsb_init
sch_lsb_init = _lsf.sch_lsb_init
lsb_openjobinfo = _lsf.lsb_openjobinfo
lsb_openjobinfo_a = _lsf.lsb_openjobinfo_a
lsb_openjobinfo_a_ext = _lsf.lsb_openjobinfo_a_ext
lsb_openjobinfo_req = _lsf.lsb_openjobinfo_req
lsb_queryjobinfo = _lsf.lsb_queryjobinfo
lsb_queryjobinfo_ext = _lsf.lsb_queryjobinfo_ext
lsb_fetchjobinfo = _lsf.lsb_fetchjobinfo
lsb_fetchjobinfo_ext = _lsf.lsb_fetchjobinfo_ext
lsb_readjobinfo = _lsf.lsb_readjobinfo
lsb_submit = _lsf.lsb_submit
lsb_submitPack = _lsf.lsb_submitPack
lsb_readjobinfo_cond = _lsf.lsb_readjobinfo_cond
lsb_readframejob = _lsf.lsb_readframejob
lsb_closejobinfo = _lsf.lsb_closejobinfo
lsb_hostcontrol = _lsf.lsb_hostcontrol
lsb_hghostcontrol = _lsf.lsb_hghostcontrol
lsb_queueinfo = _lsf.lsb_queueinfo
lsb_reconfig = _lsf.lsb_reconfig
lsb_signaljob = _lsf.lsb_signaljob
lsb_killbulkjobs = _lsf.lsb_killbulkjobs
lsb_msgjob = _lsf.lsb_msgjob
lsb_chkpntjob = _lsf.lsb_chkpntjob
lsb_deletejob = _lsf.lsb_deletejob
lsb_forcekilljob = _lsf.lsb_forcekilljob
lsb_submitframe = _lsf.lsb_submitframe
lsb_requeuejob = _lsf.lsb_requeuejob
lsb_sysmsg = _lsf.lsb_sysmsg
lsb_perror = _lsf.lsb_perror
lsb_errorByCmd = _lsf.lsb_errorByCmd
lsb_sperror = _lsf.lsb_sperror
lsb_peekjob = _lsf.lsb_peekjob
lsb_mig = _lsf.lsb_mig
lsb_clusterinfo = _lsf.lsb_clusterinfo
lsb_clusterinfoEx = _lsf.lsb_clusterinfoEx
lsb_hostinfo = _lsf.lsb_hostinfo
lsb_hostinfo_ex = _lsf.lsb_hostinfo_ex
lsb_hostinfo_cond = _lsf.lsb_hostinfo_cond
lsb_movejob = _lsf.lsb_movejob
lsb_switchjob = _lsf.lsb_switchjob
lsb_queuecontrol = _lsf.lsb_queuecontrol
lsb_userinfo = _lsf.lsb_userinfo
lsb_hostgrpinfo = _lsf.lsb_hostgrpinfo
lsb_usergrpinfo = _lsf.lsb_usergrpinfo
lsb_parameterinfo = _lsf.lsb_parameterinfo
lsb_modify = _lsf.lsb_modify
getCpuFactor = _lsf.getCpuFactor
lsb_suspreason = _lsf.lsb_suspreason
lsb_pendreason = _lsf.lsb_pendreason
lsb_calendarinfo = _lsf.lsb_calendarinfo
lsb_calExprOccs = _lsf.lsb_calExprOccs
lsb_calendarop = _lsf.lsb_calendarop
lsb_puteventrec = _lsf.lsb_puteventrec
lsb_puteventrecRaw = _lsf.lsb_puteventrecRaw
lsb_geteventrec = _lsf.lsb_geteventrec
lsb_geteventrec_decrypt = _lsf.lsb_geteventrec_decrypt
lsb_geteventrecord = _lsf.lsb_geteventrecord
lsb_geteventrecordEx = _lsf.lsb_geteventrecordEx
lsb_getnewjob_from_string = _lsf.lsb_getnewjob_from_string
lsb_eventinfo = _lsf.lsb_eventinfo
lsb_sharedresourceinfo = _lsf.lsb_sharedresourceinfo
lsb_geteventrecbyline = _lsf.lsb_geteventrecbyline
lsb_rcvconnect = _lsf.lsb_rcvconnect
lsb_sndmsg = _lsf.lsb_sndmsg
lsb_rcvmsg = _lsf.lsb_rcvmsg
lsb_runjob = _lsf.lsb_runjob
lsb_addjgrp = _lsf.lsb_addjgrp
lsb_modjgrp = _lsf.lsb_modjgrp
lsb_holdjgrp = _lsf.lsb_holdjgrp
lsb_reljgrp = _lsf.lsb_reljgrp
lsb_deljgrp = _lsf.lsb_deljgrp
lsb_deljgrp_ext = _lsf.lsb_deljgrp_ext
lsb_listjgrp = _lsf.lsb_listjgrp
lsb_serviceClassInfo = _lsf.lsb_serviceClassInfo
lsb_appInfo = _lsf.lsb_appInfo
lsb_freeAppInfoEnts = _lsf.lsb_freeAppInfoEnts
lsb_jobid2str = _lsf.lsb_jobid2str
lsb_jobid2str_r = _lsf.lsb_jobid2str_r
lsb_jobidinstr = _lsf.lsb_jobidinstr
jobId32To64 = _lsf.jobId32To64
jobId64To32 = _lsf.jobId64To32
lsb_setjobattr = _lsf.lsb_setjobattr
lsb_rexecv = _lsf.lsb_rexecv
lsb_catch = _lsf.lsb_catch
lsb_throw = _lsf.lsb_throw
lsb_postjobmsg = _lsf.lsb_postjobmsg
lsb_readjobmsg = _lsf.lsb_readjobmsg
lsb_bulkJobInfoUpdate = _lsf.lsb_bulkJobInfoUpdate
lsb_addreservation = _lsf.lsb_addreservation
lsb_removereservation = _lsf.lsb_removereservation
lsb_reservationinfo = _lsf.lsb_reservationinfo
lsb_freeRsvExecCmd = _lsf.lsb_freeRsvExecCmd
lsb_dupRsvExecCmd = _lsf.lsb_dupRsvExecCmd
lsb_parseRsvExecOption = _lsf.lsb_parseRsvExecOption
lsb_modreservation = _lsf.lsb_modreservation
initSortIntList = _lsf.initSortIntList
insertSortIntList = _lsf.insertSortIntList
getNextSortIntList = _lsf.getNextSortIntList
freeSortIntList = _lsf.freeSortIntList
getMinSortIntList = _lsf.getMinSortIntList
getMaxSortIntList = _lsf.getMaxSortIntList
getTotalSortIntList = _lsf.getTotalSortIntList
updateJobIdIndexFile = _lsf.updateJobIdIndexFile
class jobExtschInfoReq(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, jobExtschInfoReq, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, jobExtschInfoReq, name)
    __repr__ = _swig_repr
    __swig_setmethods__["qCnt"] = _lsf.jobExtschInfoReq_qCnt_set
    __swig_getmethods__["qCnt"] = _lsf.jobExtschInfoReq_qCnt_get
    if _newclass:qCnt = property(_lsf.jobExtschInfoReq_qCnt_get, _lsf.jobExtschInfoReq_qCnt_set)
    __swig_setmethods__["queues"] = _lsf.jobExtschInfoReq_queues_set
    __swig_getmethods__["queues"] = _lsf.jobExtschInfoReq_queues_get
    if _newclass:queues = property(_lsf.jobExtschInfoReq_queues_get, _lsf.jobExtschInfoReq_queues_set)
    def __init__(self, *args): 
        this = _lsf.new_jobExtschInfoReq(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _lsf.delete_jobExtschInfoReq
    __del__ = lambda self : None;
jobExtschInfoReq_swigregister = _lsf.jobExtschInfoReq_swigregister
jobExtschInfoReq_swigregister(jobExtschInfoReq)

class jobExtschInfo(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, jobExtschInfo, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, jobExtschInfo, name)
    __repr__ = _swig_repr
    __swig_setmethods__["jobId"] = _lsf.jobExtschInfo_jobId_set
    __swig_getmethods__["jobId"] = _lsf.jobExtschInfo_jobId_get
    if _newclass:jobId = property(_lsf.jobExtschInfo_jobId_get, _lsf.jobExtschInfo_jobId_set)
    __swig_setmethods__["status"] = _lsf.jobExtschInfo_status_set
    __swig_getmethods__["status"] = _lsf.jobExtschInfo_status_get
    if _newclass:status = property(_lsf.jobExtschInfo_status_get, _lsf.jobExtschInfo_status_set)
    __swig_setmethods__["jRusageUpdateTime"] = _lsf.jobExtschInfo_jRusageUpdateTime_set
    __swig_getmethods__["jRusageUpdateTime"] = _lsf.jobExtschInfo_jRusageUpdateTime_get
    if _newclass:jRusageUpdateTime = property(_lsf.jobExtschInfo_jRusageUpdateTime_get, _lsf.jobExtschInfo_jRusageUpdateTime_set)
    __swig_setmethods__["runRusage"] = _lsf.jobExtschInfo_runRusage_set
    __swig_getmethods__["runRusage"] = _lsf.jobExtschInfo_runRusage_get
    if _newclass:runRusage = property(_lsf.jobExtschInfo_runRusage_get, _lsf.jobExtschInfo_runRusage_set)
    def __init__(self, *args): 
        this = _lsf.new_jobExtschInfo(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _lsf.delete_jobExtschInfo
    __del__ = lambda self : None;
jobExtschInfo_swigregister = _lsf.jobExtschInfo_swigregister
jobExtschInfo_swigregister(jobExtschInfo)

class jobExtschInfoReply(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, jobExtschInfoReply, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, jobExtschInfoReply, name)
    __repr__ = _swig_repr
    __swig_setmethods__["jobCnt"] = _lsf.jobExtschInfoReply_jobCnt_set
    __swig_getmethods__["jobCnt"] = _lsf.jobExtschInfoReply_jobCnt_get
    if _newclass:jobCnt = property(_lsf.jobExtschInfoReply_jobCnt_get, _lsf.jobExtschInfoReply_jobCnt_set)
    __swig_setmethods__["jobs"] = _lsf.jobExtschInfoReply_jobs_set
    __swig_getmethods__["jobs"] = _lsf.jobExtschInfoReply_jobs_get
    if _newclass:jobs = property(_lsf.jobExtschInfoReply_jobs_get, _lsf.jobExtschInfoReply_jobs_set)
    def __init__(self, *args): 
        this = _lsf.new_jobExtschInfoReply(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _lsf.delete_jobExtschInfoReply
    __del__ = lambda self : None;
jobExtschInfoReply_swigregister = _lsf.jobExtschInfoReply_swigregister
jobExtschInfoReply_swigregister(jobExtschInfoReply)

getjobinfo4queues = _lsf.getjobinfo4queues
free_jobExtschInfoReply = _lsf.free_jobExtschInfoReply
free_jobExtschInfoReq = _lsf.free_jobExtschInfoReq
longer_strcpy = _lsf.longer_strcpy
class diagnoseJobReq(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, diagnoseJobReq, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, diagnoseJobReq, name)
    __repr__ = _swig_repr
    __swig_setmethods__["jobCnt"] = _lsf.diagnoseJobReq_jobCnt_set
    __swig_getmethods__["jobCnt"] = _lsf.diagnoseJobReq_jobCnt_get
    if _newclass:jobCnt = property(_lsf.diagnoseJobReq_jobCnt_get, _lsf.diagnoseJobReq_jobCnt_set)
    __swig_setmethods__["jobId"] = _lsf.diagnoseJobReq_jobId_set
    __swig_getmethods__["jobId"] = _lsf.diagnoseJobReq_jobId_get
    if _newclass:jobId = property(_lsf.diagnoseJobReq_jobId_get, _lsf.diagnoseJobReq_jobId_set)
    def __init__(self, *args): 
        this = _lsf.new_diagnoseJobReq(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _lsf.delete_diagnoseJobReq
    __del__ = lambda self : None;
diagnoseJobReq_swigregister = _lsf.diagnoseJobReq_swigregister
diagnoseJobReq_swigregister(diagnoseJobReq)

lsb_diagnosejob = _lsf.lsb_diagnosejob
SIM_STATUS_RUN = _lsf.SIM_STATUS_RUN
SIM_STATUS_SUSPEND = _lsf.SIM_STATUS_SUSPEND
class simStatusReply(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, simStatusReply, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, simStatusReply, name)
    __repr__ = _swig_repr
    __swig_setmethods__["simStatus"] = _lsf.simStatusReply_simStatus_set
    __swig_getmethods__["simStatus"] = _lsf.simStatusReply_simStatus_get
    if _newclass:simStatus = property(_lsf.simStatusReply_simStatus_get, _lsf.simStatusReply_simStatus_set)
    __swig_setmethods__["curTime"] = _lsf.simStatusReply_curTime_set
    __swig_getmethods__["curTime"] = _lsf.simStatusReply_curTime_get
    if _newclass:curTime = property(_lsf.simStatusReply_curTime_get, _lsf.simStatusReply_curTime_set)
    def __init__(self, *args): 
        this = _lsf.new_simStatusReply(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _lsf.delete_simStatusReply
    __del__ = lambda self : None;
simStatusReply_swigregister = _lsf.simStatusReply_swigregister
simStatusReply_swigregister(simStatusReply)

lsb_simstatus = _lsf.lsb_simstatus
free_simStatusReply = _lsf.free_simStatusReply
LSB_HOST_OPTION_EXPORT = _lsf.LSB_HOST_OPTION_EXPORT
LSB_HOST_OPTION_EXCEPT = _lsf.LSB_HOST_OPTION_EXCEPT
LSB_HOST_OPTION_BATCH = _lsf.LSB_HOST_OPTION_BATCH
LSB_HOST_OPTION_CONDENSED = _lsf.LSB_HOST_OPTION_CONDENSED
RMS_NON_RMS_OPTIONS_ERR = _lsf.RMS_NON_RMS_OPTIONS_ERR
RMS_NODE_PTILE_ERR = _lsf.RMS_NODE_PTILE_ERR
RMS_RAIL_RAILMASK_ERR = _lsf.RMS_RAIL_RAILMASK_ERR
RMS_NODES_OUT_BOUND_ERR = _lsf.RMS_NODES_OUT_BOUND_ERR
RMS_PTILE_OUT_BOUND_ERR = _lsf.RMS_PTILE_OUT_BOUND_ERR
RMS_RAIL_OUT_BOUND_ERR = _lsf.RMS_RAIL_OUT_BOUND_ERR
RMS_RAILMASK_OUT_BOUND_ERR = _lsf.RMS_RAILMASK_OUT_BOUND_ERR
RMS_NODES_SYNTAX_ERR = _lsf.RMS_NODES_SYNTAX_ERR
RMS_PTILE_SYNTAX_ERR = _lsf.RMS_PTILE_SYNTAX_ERR
RMS_RAIL_SYNTAX_ERR = _lsf.RMS_RAIL_SYNTAX_ERR
RMS_RAILMASK_SYNTAX_ERR = _lsf.RMS_RAILMASK_SYNTAX_ERR
RMS_BASE_SYNTAX_ERR = _lsf.RMS_BASE_SYNTAX_ERR
RMS_BASE_TOO_LONG = _lsf.RMS_BASE_TOO_LONG
RMS_TOO_MANY_ALLOCTYPE_ERR = _lsf.RMS_TOO_MANY_ALLOCTYPE_ERR
RMS_NO_LSF_EXTSCHED_Y_ERR = _lsf.RMS_NO_LSF_EXTSCHED_Y_ERR
RMS_READ_ENV_ERR = _lsf.RMS_READ_ENV_ERR
RMS_MEM_ALLOC_ERR = _lsf.RMS_MEM_ALLOC_ERR
RMS_BRACKETS_MISMATCH_ERR = _lsf.RMS_BRACKETS_MISMATCH_ERR
RMS_ALLOC_TYPE_UNKNOWN = _lsf.RMS_ALLOC_TYPE_UNKNOWN
RMS_ALLOC_TYPE_SLOAD = _lsf.RMS_ALLOC_TYPE_SLOAD
RMS_ALLOC_TYPE_SNODE = _lsf.RMS_ALLOC_TYPE_SNODE
RMS_ALLOC_TYPE_MCONT = _lsf.RMS_ALLOC_TYPE_MCONT
RMS_TOPOLOGY_UNKNOWN = _lsf.RMS_TOPOLOGY_UNKNOWN
RMS_TOPOLOGY_PTILE = _lsf.RMS_TOPOLOGY_PTILE
RMS_TOPOLOGY_NODES = _lsf.RMS_TOPOLOGY_NODES
RMS_FLAGS_UNKNOWN = _lsf.RMS_FLAGS_UNKNOWN
RMS_FLAGS_RAILS = _lsf.RMS_FLAGS_RAILS
RMS_FLAGS_RAILMASK = _lsf.RMS_FLAGS_RAILMASK
class rmsExtschedOption_t(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, rmsExtschedOption_t, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, rmsExtschedOption_t, name)
    __repr__ = _swig_repr
    __swig_setmethods__["alloc_type"] = _lsf.rmsExtschedOption_t_alloc_type_set
    __swig_getmethods__["alloc_type"] = _lsf.rmsExtschedOption_t_alloc_type_get
    if _newclass:alloc_type = property(_lsf.rmsExtschedOption_t_alloc_type_get, _lsf.rmsExtschedOption_t_alloc_type_set)
    __swig_setmethods__["topology"] = _lsf.rmsExtschedOption_t_topology_set
    __swig_getmethods__["topology"] = _lsf.rmsExtschedOption_t_topology_get
    if _newclass:topology = property(_lsf.rmsExtschedOption_t_topology_get, _lsf.rmsExtschedOption_t_topology_set)
    __swig_setmethods__["topology_value"] = _lsf.rmsExtschedOption_t_topology_value_set
    __swig_getmethods__["topology_value"] = _lsf.rmsExtschedOption_t_topology_value_get
    if _newclass:topology_value = property(_lsf.rmsExtschedOption_t_topology_value_get, _lsf.rmsExtschedOption_t_topology_value_set)
    __swig_setmethods__["set_base"] = _lsf.rmsExtschedOption_t_set_base_set
    __swig_getmethods__["set_base"] = _lsf.rmsExtschedOption_t_set_base_get
    if _newclass:set_base = property(_lsf.rmsExtschedOption_t_set_base_get, _lsf.rmsExtschedOption_t_set_base_set)
    __swig_setmethods__["base"] = _lsf.rmsExtschedOption_t_base_set
    __swig_getmethods__["base"] = _lsf.rmsExtschedOption_t_base_get
    if _newclass:base = property(_lsf.rmsExtschedOption_t_base_get, _lsf.rmsExtschedOption_t_base_set)
    __swig_setmethods__["flags"] = _lsf.rmsExtschedOption_t_flags_set
    __swig_getmethods__["flags"] = _lsf.rmsExtschedOption_t_flags_get
    if _newclass:flags = property(_lsf.rmsExtschedOption_t_flags_get, _lsf.rmsExtschedOption_t_flags_set)
    __swig_setmethods__["flags_value"] = _lsf.rmsExtschedOption_t_flags_value_set
    __swig_getmethods__["flags_value"] = _lsf.rmsExtschedOption_t_flags_value_get
    if _newclass:flags_value = property(_lsf.rmsExtschedOption_t_flags_value_get, _lsf.rmsExtschedOption_t_flags_value_set)
    def __init__(self, *args): 
        this = _lsf.new_rmsExtschedOption_t(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _lsf.delete_rmsExtschedOption_t
    __del__ = lambda self : None;
rmsExtschedOption_t_swigregister = _lsf.rmsExtschedOption_t_swigregister
rmsExtschedOption_t_swigregister(rmsExtschedOption_t)

parseRmsOptions = _lsf.parseRmsOptions
MBD_DEF_STREAM_SIZE = _lsf.MBD_DEF_STREAM_SIZE
DEF_MAX_STREAM_FILE_NUMBER = _lsf.DEF_MAX_STREAM_FILE_NUMBER
class lsbStream(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, lsbStream, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, lsbStream, name)
    __repr__ = _swig_repr
    __swig_setmethods__["streamFile"] = _lsf.lsbStream_streamFile_set
    __swig_getmethods__["streamFile"] = _lsf.lsbStream_streamFile_get
    if _newclass:streamFile = property(_lsf.lsbStream_streamFile_get, _lsf.lsbStream_streamFile_set)
    __swig_setmethods__["maxStreamSize"] = _lsf.lsbStream_maxStreamSize_set
    __swig_getmethods__["maxStreamSize"] = _lsf.lsbStream_maxStreamSize_get
    if _newclass:maxStreamSize = property(_lsf.lsbStream_maxStreamSize_get, _lsf.lsbStream_maxStreamSize_set)
    __swig_setmethods__["maxStreamFileNum"] = _lsf.lsbStream_maxStreamFileNum_set
    __swig_getmethods__["maxStreamFileNum"] = _lsf.lsbStream_maxStreamFileNum_get
    if _newclass:maxStreamFileNum = property(_lsf.lsbStream_maxStreamFileNum_get, _lsf.lsbStream_maxStreamFileNum_set)
    __swig_setmethods__["trace"] = _lsf.lsbStream_trace_set
    __swig_getmethods__["trace"] = _lsf.lsbStream_trace_get
    if _newclass:trace = property(_lsf.lsbStream_trace_get, _lsf.lsbStream_trace_set)
    __swig_setmethods__["trs"] = _lsf.lsbStream_trs_set
    __swig_getmethods__["trs"] = _lsf.lsbStream_trs_get
    if _newclass:trs = property(_lsf.lsbStream_trs_get, _lsf.lsbStream_trs_set)
    __swig_setmethods__["statusFile"] = _lsf.lsbStream_statusFile_set
    __swig_getmethods__["statusFile"] = _lsf.lsbStream_statusFile_get
    if _newclass:statusFile = property(_lsf.lsbStream_statusFile_get, _lsf.lsbStream_statusFile_set)
    __swig_setmethods__["pendingreasonsFile"] = _lsf.lsbStream_pendingreasonsFile_set
    __swig_getmethods__["pendingreasonsFile"] = _lsf.lsbStream_pendingreasonsFile_get
    if _newclass:pendingreasonsFile = property(_lsf.lsbStream_pendingreasonsFile_get, _lsf.lsbStream_pendingreasonsFile_set)
    def __init__(self, *args): 
        this = _lsf.new_lsbStream(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _lsf.delete_lsbStream
    __del__ = lambda self : None;
lsbStream_swigregister = _lsf.lsbStream_swigregister
lsbStream_swigregister(lsbStream)

lsb_openstream = _lsf.lsb_openstream
lsb_closestream = _lsf.lsb_closestream
lsb_streamversion = _lsf.lsb_streamversion
lsb_writestream = _lsf.lsb_writestream
lsb_readstream = _lsf.lsb_readstream
lsb_readstreamline = _lsf.lsb_readstreamline
lsb_openstatus = _lsf.lsb_openstatus
lsb_closestatus = _lsf.lsb_closestatus
lsb_writestatus = _lsf.lsb_writestatus
lsb_readstatus = _lsf.lsb_readstatus
lsb_openpendingreasons = _lsf.lsb_openpendingreasons
lsb_closependingreasons = _lsf.lsb_closependingreasons
lsb_writependingreasons = _lsf.lsb_writependingreasons
lsb_readpendingreasons = _lsf.lsb_readpendingreasons
NUM_EXITRATE_TYPES = _lsf.NUM_EXITRATE_TYPES
JOB_EXIT = _lsf.JOB_EXIT
JOB_INIT = _lsf.JOB_INIT
HPC_INIT = _lsf.HPC_INIT
JOB_EXIT_NONLSF = _lsf.JOB_EXIT_NONLSF
class apsFactorInfo(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, apsFactorInfo, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, apsFactorInfo, name)
    __repr__ = _swig_repr
    __swig_setmethods__["name"] = _lsf.apsFactorInfo_name_set
    __swig_getmethods__["name"] = _lsf.apsFactorInfo_name_get
    if _newclass:name = property(_lsf.apsFactorInfo_name_get, _lsf.apsFactorInfo_name_set)
    __swig_setmethods__["weight"] = _lsf.apsFactorInfo_weight_set
    __swig_getmethods__["weight"] = _lsf.apsFactorInfo_weight_get
    if _newclass:weight = property(_lsf.apsFactorInfo_weight_get, _lsf.apsFactorInfo_weight_set)
    __swig_setmethods__["limit"] = _lsf.apsFactorInfo_limit_set
    __swig_getmethods__["limit"] = _lsf.apsFactorInfo_limit_get
    if _newclass:limit = property(_lsf.apsFactorInfo_limit_get, _lsf.apsFactorInfo_limit_set)
    __swig_setmethods__["gracePeriod"] = _lsf.apsFactorInfo_gracePeriod_set
    __swig_getmethods__["gracePeriod"] = _lsf.apsFactorInfo_gracePeriod_get
    if _newclass:gracePeriod = property(_lsf.apsFactorInfo_gracePeriod_get, _lsf.apsFactorInfo_gracePeriod_set)
    def __init__(self, *args): 
        this = _lsf.new_apsFactorInfo(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _lsf.delete_apsFactorInfo
    __del__ = lambda self : None;
apsFactorInfo_swigregister = _lsf.apsFactorInfo_swigregister
apsFactorInfo_swigregister(apsFactorInfo)

JGRP_DEL_USER_GROUPS = _lsf.JGRP_DEL_USER_GROUPS
JGRP_DEL_CHILD_GROUPS = _lsf.JGRP_DEL_CHILD_GROUPS
JGRP_DEL_ALL = _lsf.JGRP_DEL_ALL
lsb_getallocFromHostfile = _lsf.lsb_getallocFromHostfile
lsb_resize_cancel = _lsf.lsb_resize_cancel
lsb_resize_release = _lsf.lsb_resize_release
lsb_resize_request = _lsf.lsb_resize_request
lsb_getjobdepinfo = _lsf.lsb_getjobdepinfo
class guaranteedResourcePoolInfoReq(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, guaranteedResourcePoolInfoReq, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, guaranteedResourcePoolInfoReq, name)
    __repr__ = _swig_repr
    __swig_setmethods__["poolsC"] = _lsf.guaranteedResourcePoolInfoReq_poolsC_set
    __swig_getmethods__["poolsC"] = _lsf.guaranteedResourcePoolInfoReq_poolsC_get
    if _newclass:poolsC = property(_lsf.guaranteedResourcePoolInfoReq_poolsC_get, _lsf.guaranteedResourcePoolInfoReq_poolsC_set)
    __swig_setmethods__["poolNames"] = _lsf.guaranteedResourcePoolInfoReq_poolNames_set
    __swig_getmethods__["poolNames"] = _lsf.guaranteedResourcePoolInfoReq_poolNames_get
    if _newclass:poolNames = property(_lsf.guaranteedResourcePoolInfoReq_poolNames_get, _lsf.guaranteedResourcePoolInfoReq_poolNames_set)
    def __init__(self, *args): 
        this = _lsf.new_guaranteedResourcePoolInfoReq(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _lsf.delete_guaranteedResourcePoolInfoReq
    __del__ = lambda self : None;
guaranteedResourcePoolInfoReq_swigregister = _lsf.guaranteedResourcePoolInfoReq_swigregister
guaranteedResourcePoolInfoReq_swigregister(guaranteedResourcePoolInfoReq)

class guarConsumer(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, guarConsumer, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, guarConsumer, name)
    __repr__ = _swig_repr
    __swig_setmethods__["name"] = _lsf.guarConsumer_name_set
    __swig_getmethods__["name"] = _lsf.guarConsumer_name_get
    if _newclass:name = property(_lsf.guarConsumer_name_get, _lsf.guarConsumer_name_set)
    __swig_setmethods__["share"] = _lsf.guarConsumer_share_set
    __swig_getmethods__["share"] = _lsf.guarConsumer_share_get
    if _newclass:share = property(_lsf.guarConsumer_share_get, _lsf.guarConsumer_share_set)
    __swig_setmethods__["shareType"] = _lsf.guarConsumer_shareType_set
    __swig_getmethods__["shareType"] = _lsf.guarConsumer_shareType_get
    if _newclass:shareType = property(_lsf.guarConsumer_shareType_get, _lsf.guarConsumer_shareType_set)
    __swig_setmethods__["deserved"] = _lsf.guarConsumer_deserved_set
    __swig_getmethods__["deserved"] = _lsf.guarConsumer_deserved_get
    if _newclass:deserved = property(_lsf.guarConsumer_deserved_get, _lsf.guarConsumer_deserved_set)
    __swig_setmethods__["guarUsed"] = _lsf.guarConsumer_guarUsed_set
    __swig_getmethods__["guarUsed"] = _lsf.guarConsumer_guarUsed_get
    if _newclass:guarUsed = property(_lsf.guarConsumer_guarUsed_get, _lsf.guarConsumer_guarUsed_set)
    __swig_setmethods__["totalUsed"] = _lsf.guarConsumer_totalUsed_set
    __swig_getmethods__["totalUsed"] = _lsf.guarConsumer_totalUsed_get
    if _newclass:totalUsed = property(_lsf.guarConsumer_totalUsed_get, _lsf.guarConsumer_totalUsed_set)
    def __init__(self, *args): 
        this = _lsf.new_guarConsumer(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _lsf.delete_guarConsumer
    __del__ = lambda self : None;
guarConsumer_swigregister = _lsf.guarConsumer_swigregister
guarConsumer_swigregister(guarConsumer)
GUAR_CONSUMER_SHARE_TYPE_ABSOLUTE = _lsf.GUAR_CONSUMER_SHARE_TYPE_ABSOLUTE
GUAR_CONSUMER_SHARE_TYPE_PERCENT = _lsf.GUAR_CONSUMER_SHARE_TYPE_PERCENT

class guaranteedResourcePoolEnt(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, guaranteedResourcePoolEnt, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, guaranteedResourcePoolEnt, name)
    __repr__ = _swig_repr
    __swig_setmethods__["name"] = _lsf.guaranteedResourcePoolEnt_name_set
    __swig_getmethods__["name"] = _lsf.guaranteedResourcePoolEnt_name_get
    if _newclass:name = property(_lsf.guaranteedResourcePoolEnt_name_get, _lsf.guaranteedResourcePoolEnt_name_set)
    __swig_setmethods__["description"] = _lsf.guaranteedResourcePoolEnt_description_set
    __swig_getmethods__["description"] = _lsf.guaranteedResourcePoolEnt_description_get
    if _newclass:description = property(_lsf.guaranteedResourcePoolEnt_description_get, _lsf.guaranteedResourcePoolEnt_description_set)
    __swig_setmethods__["type"] = _lsf.guaranteedResourcePoolEnt_type_set
    __swig_getmethods__["type"] = _lsf.guaranteedResourcePoolEnt_type_get
    if _newclass:type = property(_lsf.guaranteedResourcePoolEnt_type_get, _lsf.guaranteedResourcePoolEnt_type_set)
    __swig_setmethods__["rsrcName"] = _lsf.guaranteedResourcePoolEnt_rsrcName_set
    __swig_getmethods__["rsrcName"] = _lsf.guaranteedResourcePoolEnt_rsrcName_get
    if _newclass:rsrcName = property(_lsf.guaranteedResourcePoolEnt_rsrcName_get, _lsf.guaranteedResourcePoolEnt_rsrcName_set)
    __swig_setmethods__["slotsPerHost"] = _lsf.guaranteedResourcePoolEnt_slotsPerHost_set
    __swig_getmethods__["slotsPerHost"] = _lsf.guaranteedResourcePoolEnt_slotsPerHost_get
    if _newclass:slotsPerHost = property(_lsf.guaranteedResourcePoolEnt_slotsPerHost_get, _lsf.guaranteedResourcePoolEnt_slotsPerHost_set)
    __swig_setmethods__["status"] = _lsf.guaranteedResourcePoolEnt_status_set
    __swig_getmethods__["status"] = _lsf.guaranteedResourcePoolEnt_status_get
    if _newclass:status = property(_lsf.guaranteedResourcePoolEnt_status_get, _lsf.guaranteedResourcePoolEnt_status_set)
    __swig_setmethods__["total"] = _lsf.guaranteedResourcePoolEnt_total_set
    __swig_getmethods__["total"] = _lsf.guaranteedResourcePoolEnt_total_get
    if _newclass:total = property(_lsf.guaranteedResourcePoolEnt_total_get, _lsf.guaranteedResourcePoolEnt_total_set)
    __swig_setmethods__["free"] = _lsf.guaranteedResourcePoolEnt_free_set
    __swig_getmethods__["free"] = _lsf.guaranteedResourcePoolEnt_free_get
    if _newclass:free = property(_lsf.guaranteedResourcePoolEnt_free_get, _lsf.guaranteedResourcePoolEnt_free_set)
    __swig_setmethods__["guar"] = _lsf.guaranteedResourcePoolEnt_guar_set
    __swig_getmethods__["guar"] = _lsf.guaranteedResourcePoolEnt_guar_get
    if _newclass:guar = property(_lsf.guaranteedResourcePoolEnt_guar_get, _lsf.guaranteedResourcePoolEnt_guar_set)
    __swig_setmethods__["unused"] = _lsf.guaranteedResourcePoolEnt_unused_set
    __swig_getmethods__["unused"] = _lsf.guaranteedResourcePoolEnt_unused_get
    if _newclass:unused = property(_lsf.guaranteedResourcePoolEnt_unused_get, _lsf.guaranteedResourcePoolEnt_unused_set)
    __swig_setmethods__["consumerC"] = _lsf.guaranteedResourcePoolEnt_consumerC_set
    __swig_getmethods__["consumerC"] = _lsf.guaranteedResourcePoolEnt_consumerC_get
    if _newclass:consumerC = property(_lsf.guaranteedResourcePoolEnt_consumerC_get, _lsf.guaranteedResourcePoolEnt_consumerC_set)
    __swig_setmethods__["consumerV"] = _lsf.guaranteedResourcePoolEnt_consumerV_set
    __swig_getmethods__["consumerV"] = _lsf.guaranteedResourcePoolEnt_consumerV_get
    if _newclass:consumerV = property(_lsf.guaranteedResourcePoolEnt_consumerV_get, _lsf.guaranteedResourcePoolEnt_consumerV_set)
    __swig_setmethods__["configuredHosts"] = _lsf.guaranteedResourcePoolEnt_configuredHosts_set
    __swig_getmethods__["configuredHosts"] = _lsf.guaranteedResourcePoolEnt_configuredHosts_get
    if _newclass:configuredHosts = property(_lsf.guaranteedResourcePoolEnt_configuredHosts_get, _lsf.guaranteedResourcePoolEnt_configuredHosts_set)
    __swig_setmethods__["resSelect"] = _lsf.guaranteedResourcePoolEnt_resSelect_set
    __swig_getmethods__["resSelect"] = _lsf.guaranteedResourcePoolEnt_resSelect_get
    if _newclass:resSelect = property(_lsf.guaranteedResourcePoolEnt_resSelect_get, _lsf.guaranteedResourcePoolEnt_resSelect_set)
    __swig_setmethods__["currentHostsC"] = _lsf.guaranteedResourcePoolEnt_currentHostsC_set
    __swig_getmethods__["currentHostsC"] = _lsf.guaranteedResourcePoolEnt_currentHostsC_get
    if _newclass:currentHostsC = property(_lsf.guaranteedResourcePoolEnt_currentHostsC_get, _lsf.guaranteedResourcePoolEnt_currentHostsC_set)
    __swig_setmethods__["currentHosts"] = _lsf.guaranteedResourcePoolEnt_currentHosts_set
    __swig_getmethods__["currentHosts"] = _lsf.guaranteedResourcePoolEnt_currentHosts_get
    if _newclass:currentHosts = property(_lsf.guaranteedResourcePoolEnt_currentHosts_get, _lsf.guaranteedResourcePoolEnt_currentHosts_set)
    __swig_setmethods__["policies"] = _lsf.guaranteedResourcePoolEnt_policies_set
    __swig_getmethods__["policies"] = _lsf.guaranteedResourcePoolEnt_policies_get
    if _newclass:policies = property(_lsf.guaranteedResourcePoolEnt_policies_get, _lsf.guaranteedResourcePoolEnt_policies_set)
    __swig_setmethods__["loanDelay"] = _lsf.guaranteedResourcePoolEnt_loanDelay_set
    __swig_getmethods__["loanDelay"] = _lsf.guaranteedResourcePoolEnt_loanDelay_get
    if _newclass:loanDelay = property(_lsf.guaranteedResourcePoolEnt_loanDelay_get, _lsf.guaranteedResourcePoolEnt_loanDelay_set)
    __swig_setmethods__["queuesC"] = _lsf.guaranteedResourcePoolEnt_queuesC_set
    __swig_getmethods__["queuesC"] = _lsf.guaranteedResourcePoolEnt_queuesC_get
    if _newclass:queuesC = property(_lsf.guaranteedResourcePoolEnt_queuesC_get, _lsf.guaranteedResourcePoolEnt_queuesC_set)
    __swig_setmethods__["queues"] = _lsf.guaranteedResourcePoolEnt_queues_set
    __swig_getmethods__["queues"] = _lsf.guaranteedResourcePoolEnt_queues_get
    if _newclass:queues = property(_lsf.guaranteedResourcePoolEnt_queues_get, _lsf.guaranteedResourcePoolEnt_queues_set)
    def __init__(self, *args): 
        this = _lsf.new_guaranteedResourcePoolEnt(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _lsf.delete_guaranteedResourcePoolEnt
    __del__ = lambda self : None;
guaranteedResourcePoolEnt_swigregister = _lsf.guaranteedResourcePoolEnt_swigregister
guaranteedResourcePoolEnt_swigregister(guaranteedResourcePoolEnt)
GUAR_RESOURCE_POOL_TYPE_SLOTS = _lsf.GUAR_RESOURCE_POOL_TYPE_SLOTS
GUAR_RESOURCE_POOL_TYPE_HOSTS = _lsf.GUAR_RESOURCE_POOL_TYPE_HOSTS
GUAR_RESOURCE_POOL_TYPE_RESOURCE = _lsf.GUAR_RESOURCE_POOL_TYPE_RESOURCE
GUAR_RESOURCE_POOL_STATUS_OK = _lsf.GUAR_RESOURCE_POOL_STATUS_OK
GUAR_RESOURCE_POOL_STATUS_OVERCOMMIT = _lsf.GUAR_RESOURCE_POOL_STATUS_OVERCOMMIT
GUAR_RESOURCE_POOL_STATUS_UNKNOWN = _lsf.GUAR_RESOURCE_POOL_STATUS_UNKNOWN
GUAR_RESOURCE_POOL_STATUS_LOANSUSP = _lsf.GUAR_RESOURCE_POOL_STATUS_LOANSUSP
GUAR_RESOURCE_POOL_POLICIES_NONE = _lsf.GUAR_RESOURCE_POOL_POLICIES_NONE
GUAR_RESOURCE_POOL_POLICIES_LOAN_DELAY = _lsf.GUAR_RESOURCE_POOL_POLICIES_LOAN_DELAY
GUAR_RESOURCE_POOL_POLICIES_LOAN_RESTRICT = _lsf.GUAR_RESOURCE_POOL_POLICIES_LOAN_RESTRICT

class guaranteedResourcePoolInfoReply(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, guaranteedResourcePoolInfoReply, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, guaranteedResourcePoolInfoReply, name)
    __repr__ = _swig_repr
    __swig_setmethods__["numEnt"] = _lsf.guaranteedResourcePoolInfoReply_numEnt_set
    __swig_getmethods__["numEnt"] = _lsf.guaranteedResourcePoolInfoReply_numEnt_get
    if _newclass:numEnt = property(_lsf.guaranteedResourcePoolInfoReply_numEnt_get, _lsf.guaranteedResourcePoolInfoReply_numEnt_set)
    __swig_setmethods__["entries"] = _lsf.guaranteedResourcePoolInfoReply_entries_set
    __swig_getmethods__["entries"] = _lsf.guaranteedResourcePoolInfoReply_entries_get
    if _newclass:entries = property(_lsf.guaranteedResourcePoolInfoReply_entries_get, _lsf.guaranteedResourcePoolInfoReply_entries_set)
    def __init__(self, *args): 
        this = _lsf.new_guaranteedResourcePoolInfoReply(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _lsf.delete_guaranteedResourcePoolInfoReply
    __del__ = lambda self : None;
guaranteedResourcePoolInfoReply_swigregister = _lsf.guaranteedResourcePoolInfoReply_swigregister
guaranteedResourcePoolInfoReply_swigregister(guaranteedResourcePoolInfoReply)

lsb_guaranteedResourcePoolInfo = _lsf.lsb_guaranteedResourcePoolInfo
lsb_freeGuaranteedResourcePoolEntArray = _lsf.lsb_freeGuaranteedResourcePoolEntArray
lsb_liveconfig = _lsf.lsb_liveconfig
get_host_names = _lsf.get_host_names
get_host_info = _lsf.get_host_info
get_load_of_hosts = _lsf.get_load_of_hosts
get_host_load = _lsf.get_host_load


