(
    function greet(){
        console.log("hii I am self invokin function");
    }
)();

(
    function greet(fn, ln){
        console.log(`hii I am ${fn} ${ln}`);
    }
)("Ashish", "gupta");