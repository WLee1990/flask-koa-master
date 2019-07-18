$(function(){
    $("#botnetBtn").on("click",function(event){
        var setType=$("#signatureType option:selected").text();
	var setNum=$("#signatureNum").val()
	
	$.ajax({
	    url:"signature",
	    type:"POST",
	    data:JSON.stringify({"botnet_type":setType,"number":setNum}),
	    //dataType:"text",
	    dataType:"json",
	    success: function(results){
		    $("#signatureRes").empty();
		    var parsedJson = eval(results); 
		    dataRes=parsedJson.data;
		    var textRes=dataRes.join("\n");
		     $("#signatureRes").val(textRes);
		}
	    })
    })
})
