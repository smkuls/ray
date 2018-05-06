s=$1
e=$2
n=$(($e - $s + 1))
echo $n
rg=$3
vm_prefix="ray-auto-vm"
file_name=$4
params=$5
commands="az vm run-command invoke -g $rg -n $vm_prefix{} --command-id RunShellScript --scripts @$file_name --parameters $params"
seq $s $e | xargs -n1 -P$n -I{} sh -c "$commands"
