require('angular')

var app = angular.module('TodoApp', []);

app.factory('taskListService', function($http){
    return {
        getTaskList : function(callback){
            var taskList = [];
            var url = '/get-task-list/';
            $http.get(url).success(callback)
            .error(function(errResp){
                console.log("inside error");
            });
        }
    }
})


app.controller('MainCtrl', function($scope, taskListService, $http){
    var updateTaskLeft = function(taskList){
        var taskLeft = taskList.filter(function(t){
            return !t.done
        })
        return taskLeft
    }
    taskListService.getTaskList(function(data){
        $scope.taskList = data;
        $scope.taskLeft = updateTaskLeft($scope.taskList);
    });

    $scope.formTodoText = null;
    $scope.addTodo = function(){
        var url = '/add-new-task/';
        var data = {taskName: $scope.formTodoText}
        $http.post(url, data).success(function(data){
            $scope.taskList.push(data);
            $scope.taskLeft = updateTaskLeft($scope.taskList);
            $scope.formTodoText = '';
        })
        .error(function(errResp){
            console.log("error", errResp);
        })
    }
    $scope.toggleBookmark = function(index, task){
        var url = '/edit-task/';
        var data = {taskId:task.taskId, taskName: task.taskName, bookmark:!task.bookmark, done:task.done};
        $http.post(url, data).success(function(data){
            $scope.taskList[index] = data;
        })
        .error(function(errResp){
            console.log("error", errResp);
        })
    }
    $scope.toggleDone = function(index, task){
        var url = '/edit-task/';
        var data = {taskId:task.taskId, taskName: task.taskName, bookmark:task.bookmark, done:task.done};
        $http.post(url, data).success(function(data){
            $scope.taskList[index] = data;
            $scope.taskLeft = updateTaskLeft($scope.taskList);
        })
        .error(function(errResp){
            console.log("error", errResp);
        })
    }
    $scope.deleteTask = function(task){
        var url = '/delete-task/';
        var data = {taskId:task.taskId}
        $http.post(url, data).success(function(data){
            if(data.status === 'success'){
                $scope.taskList = $scope.taskList.filter(function(todo){
                    return todo.taskId !== task.taskId;
                })
                $scope.taskLeft = updateTaskLeft($scope.taskList);
            }
        })
    }
});