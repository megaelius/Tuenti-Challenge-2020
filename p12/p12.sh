read ascii1 < ./testdata/ciphered/test1.txt
read ascii2 < ./testdata/ciphered/test2.txt

read plain1 < ./testdata/plaintexts/test1.txt
read plain2 < ./testdata/plaintexts/test2.txt


#echo -ne "$ascii1" | od -An -tuC

hexp1=$(echo $plain2 | xxd -ps)
hexp2=$(echo $plain1 | xxd -ps)

hex1=$(echo $ascii1 | xxd -ps)
hex2=$(echo $ascii2 | xxd -ps)

echo $hex1 > hex1.txt
echo $hex2 > hex2.txt
echo $hexp1 > hexp1.txt
echo $hexp2 > hexp2.txt
