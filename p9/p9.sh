chr() {
    printf \\$(printf '%03o' $1)
}

# imprime el número en hexadecimal
function hex() {
    printf '%02X\n' $1
}

function encrypt() {
    key=$1
    msg=$2
    crpt_msg=""
    for ((i=0; i<${#msg}; i++));do
        c=${msg:$i:1}
        asc_chr=$(echo -ne "$c" | od -An -tuC)
        #echo -n $asc_chr
        key_pos=$((${#key} - 1 - ${i}))
        key_char=${key:$key_pos:1}
        #echo -n " "${key_char}
        crpt_chr=$(( $asc_chr ^ ${key_char} ))
        #echo -n " "$crpt_chr
        hx_crpt_chr=$(hex $crpt_chr)
        #echo " "$hx_crpt_chr
        crpt_msg=${crpt_msg}${hx_crpt_chr}
   done
   echo $crpt_msg
}

function get_key(){
    encmsg=$1
    decmsg=$2
    key=""
    j=0
    for ((i=0; i<${#encmsg}-1; i=i+2));do
        #convertir de hexadecimal a char
        encc=$(echo -n ${encmsg:$i:2} | xxd -r -p)
        #convertir de char a ascii
        encc=$(echo -ne "$encc" | od -An -tuC)
        #convertir de char a ascii
        decc=$(echo -ne "${decmsg:$j:1}" | od -An -tuC)
        #echo $encc" "$decc
        keyc=$(($encc ^ $decc))
        #echo $c
        j=$((j+1))
        key=$keyc$key
   done
   echo $key
}

function decript(){
    encmsg=$2
    key=$1
    msg=""
    j=$((${#key}-1))
    for ((i=0; i<${#encmsg}-1; i=i+2));do
        #convertir de hexadecimal a char
        encc=$(echo -n ${encmsg:$i:2} | xxd -r -p)
        #convertir de char a ascii
        encc=$(echo -ne "$encc" | od -An -tuC)
        #convertir de char a ascii
        keyc=$(echo -ne "${key:$j:1}" | od -An -tuC)
        #echo $encc" "$decc
        msgc="$(($encc ^ $keyc))"
        #echo $c
        j=$((j-1))
        if [ $msgc -eq 11 ]
        then
            msgc=";"
        fi
        msg=$msg$msgc
   done
   echo $msg
}

key=$(get_key $1 $2)
decript $key $3
