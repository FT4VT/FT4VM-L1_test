import time
import logging
import sys
import os
import subprocess
import re
from autotest.client.shared import error
from virttest import utils_test
from virttest import kill


virttest_dir = os.environ['VIRTTEST_PATH']
temp_file_n = virttest_dir+"/FT_kvm/tests/temp.txt"
temp_file1_n = virttest_dir+"/FT_kvm/tests/temp1.txt"

def find_vm_pid(name):
  """
  find vm's process id
  """
  subprocess.call("ps aux | grep \"kvm\" > "+temp_file_n, shell=True)
  subprocess.call("grep \"name "+name+"\" "+temp_file_n+" > "+temp_file1_n, shell=True)
  f = open_file(temp_file1_n)
  line = read_line(f)
  pid = get_id(line)
  delete_file(temp_file_n)
  delete_file(temp_file1_n)
  return pid

def open_file(file_name):
  """
  open file
  """
  return open(file_name, "r")

def read_line(f):
  """
  read line in file
  """
  return f.readline()

def get_id(line):
  """
  get id string
  """
  line_arr = transfer_line_to_arr(line)
  return line_arr[1]

def delete_file(file_name):
  """
  delete temp file
  """
  subprocess.call("rm "+file_name, shell=True)

def kill_vm(name):
  """
  kill vm's process
  """
  pid = find_vm_pid(name)
  kill.kill(pid, '9')

def transfer_line_to_arr(line):
  """
  transfer line to array
  """
  line = re.sub(' +',' ',line)
  line_arr = line.split(' ')
  return line_arr



def run_L1_FT_VM_crash(test, params, env):
  """
  Testing Level1 FTVM
  When VM crash FTVM system will reboot VM or not

  """
  """
  below is temp code
  """
  vms = env.get_all_vms()
  for vm in vms:
    time.sleep(20)
    timeout = time.time()+30
    while time.time() < timeout:
      if vm.is_alive():
        break;
      time.sleep(2)
    if not vm.is_alive():
      raise Exception("first start error")

    
    kill_vm(vm.name)
    time.sleep(1)
    
    time.sleep(20)
    timeout = time.time()+30
    while time.time() < timeout:
      if vm.is_alive():
        break;
      time.sleep(2)
    if not vm.is_alive():
      raise Exception("reboot fail")
  return True


