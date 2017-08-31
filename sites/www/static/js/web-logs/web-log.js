/**
 * Created by renshangui on 2017/8/30.
 *
 * web-log相关js代码
 */


$(function () {
    var E = window.wangEditor;
    var editor = new E('#div1');
    editor.create();

    $('#saveButton').click(function () {
        $.confirm({
            title: '确认框',
            content: '确认保存吗？',
            buttons: {
                '确认': function () {
                    // 读取 html
                    alert(editor.txt.html());

                },
                '取消': function () {
                }
            }
        });

    });

});
