/**
 * Created by renshangui on 2017/10/22.
 */
function initTable() {
    //先销毁表格
    $('#table1').bootstrapTable('destroy');
    //初始化表格,动态从服务器加载数据
    $("#table1").bootstrapTable({
        method: "get",  //使用get请求到服务器获取数据
        url: "/files?action=all", //获取数据的Servlet地址
        striped: true,  //表格显示条纹
        pagination: true, //启动分页
        pageSize: 10,
        search: false,  //是否启用查询
        showColumns: true,  //显示下拉框勾选要显示的列
        showRefresh: true,  //显示刷新按钮
        sidePagination: "client", //表示服务端请求
        onLoadSuccess: function (json) {  //加载成功时执行
            $("#table1").bootstrapTable('load', json.rows);
        },
        onLoadError: function () {  //加载失败时执行
            alert("加载数据失败");
        }
    });
}

function actionFormatter(value, row, index) {
    var downLoadUrl = "/files/" + row.file_id.toString() + "?action=download";
    return [
        '<a class="download" href=' + downLoadUrl + ' title="下载">',
        '<i class="glyphicon glyphicon-download"></i>',
        '</a>'
    ];
}

window.actionEvents = {
    'click .download': function (e, value, row, index) {
        console.log(value, row, index);
    }
};

$(function () {
    //调用函数，初始化表格
    initTable();
});