$(function(){
    $("#TestBtn").on("click",function(event){
        var setType=$("#TestType option:selected").text();
	$.ajax({
	    url:"/test",
	    type:"POST",
	    data:JSON.stringify({"test_type":setType}),
	    dataType:"json",
	    success: function(results){
		    $("#TestRes").empty();
		    var parsedJson = eval(results); 
		    dataRes=parsedJson.data;
		    $("#TestRes").val(dataRes);
		}
	    })
    })
})
