$(document).ready(function(){
    $("#submit").click(function(){
        var id = $("#id").val();
        var content = $("#preview").html();
        var md_content=$("#text-input").val();md_content
        var pd = {"id":id, "content":content, "md_content":md_content};
        $.ajax({
            type:"post",
            url:"/post",
            data:pd,
            cache:false,
            success:function(data){
                // window.location.href = "/home";
            },
            error:function(){
                alert("error!");
            },
        });
    });
});