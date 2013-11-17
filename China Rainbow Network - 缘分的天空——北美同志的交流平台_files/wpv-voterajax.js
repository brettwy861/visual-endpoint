jQuery(document).ready( function($) {

    $(".wpv_voting").click( function(){
        var currentobj = $(this);
        var wpv_votewidget = currentobj.parents(".wpv_votebtn").parents(".wpv_votebtncon").parents(".wpv_votewidget");
        var wpv_votebtn = currentobj.parents(".wpv_votebtn");
        var pID = currentobj.children(".postID").val();
        var uID = currentobj.children(".userID").val();
        var aID = currentobj.children(".authorID").val();

        /*Display loading image*/
          wpv_votewidget.children(".wpv_votecount").children(".loadingimage").css("visibility", "visible");
          wpv_votewidget.children(".wpv_votecount").children(".loadingimage").css("display", "inline-block");
        
        /*Do voting*/
        $.post(
            wpvAjax.ajaxurl,
            {
              action: 'wpv-submit',
              postID: pID,
              userID: uID,
              authorID: aID,
              wpv_nonce: wpvAjax.wpv_nonce
            },
            function(response){
                currentobj.css("display", "none");
                wpv_votebtn.children(".wpv_voted_icon").css("display", "inline-block");
                wpv_votebtn.children(".wpv_votebtn_txt").css("display", "inline-block");
                wpv_votewidget.children(".wpv_votecount").children(".loadingimage").css("visibility", "hidden");
                wpv_votewidget.children(".wpv_votecount").children(".loadingimage").remove();
                wpv_votewidget.children(".wpv_votecount").children(".wpv_vcount").html(response+' ');
                currentobj.remove();
                
                /*Do updating widget*/
                $.post(
                    wpvAjax.ajaxurl,
                    {
                      action: 'wpv-top-widget',
                      postID: pID,
                      userID: uID,
                      authorID: aID,
                      wpv_nonce: wpvAjax.wpv_nonce
                    },
                    function(response){
                        if($(".widget_wpv_top_voted_widget"))
                            $(".widget_wpv_top_voted_widget").children(".wpvtopvoted").html(response);
                    }
                );
            }
        );
        return false;
    });
});