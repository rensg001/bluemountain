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
                    // 读取html并请求保存日志接口
                    $.post('/web-log', {"content": editor.txt.html()}, 'json')
                        .done(function () {
                            alert("保存成功！");
                        })
                        .fail(function (xhr, status, error) {
                        alert("保存失败" + JSON.parse(xhr.responseText).data);
                    });
                },
                '取消': function () {
                }
            }
        });

    });

});
