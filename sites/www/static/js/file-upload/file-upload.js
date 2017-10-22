/**
 * Created by renshangui on 2017/10/21.
 */
/*globals $:false */
$(function (){
    $("#file-0a").fileinput({
        uploadUrl: "/file-upload",
        maxFileCount: 1
    });
});