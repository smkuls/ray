# 'deallocate' 'start'
# DO NOT CALL STOP! THE VM IS STILL BILLED!
s=$1
e=$2
n=$(($e - $s + 1))
rg=$3
vm_prefix='ray-auto-vm'
vm_action=$4
command="az vm $vm_action -g $rg -n $vm_prefix{}"
seq $s $e | xargs -n1 -P$n -I{} sh -c "$command"
