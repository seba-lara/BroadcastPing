#!/bin/bash
#echo 
read -p " Desea instalar las dependencias? [si/no] : " response

asd () {
    pip install -r requirements.txt
}

if [[ $response == 'si' ]]; then
    asd
    echo "Dependencias instaladas, gracias!"
    
elif [[ $response == 'no' ]]; then
    echo " No se instalará ninguna dependencia"
else
    echo " Hubo un error vuelva a intentarlo."
    
fi