
function printmiddlechar(str){
    len = str.length;
    mid = parseInt(len/2 )
  
    if(len % 2 ===  0){
        
        console.log( str[mid-1], str[mid]);
    }else{
        console.log(str[mid]);
    }  
}

printmiddlechar("javas");
printmiddlechar("java");