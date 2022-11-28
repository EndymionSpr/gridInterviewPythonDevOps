while read myVar
do
        if [ $(echo $myVar | cut -d' ' -f1) -gt 199 ];
        then
                echo $(echo $myVar | cut -d' ' -f1,2,4)
        fi

done
