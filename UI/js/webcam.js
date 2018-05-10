
var app = angular.module("myModule", ['camera']);

app.controller("myContoller", function ($scope, $http, $log) {

    /*$scope.onSuccess = function () {
        // The video element contains the captured camera data
        _video = $scope.channel.video;
        $scope.$apply(function() {
            $scope.patOpts.w = _video.width;
            $scope.patOpts.h = _video.height;
            //$scope.showDemos = true;
        });
    };*/

    navigator.mediaDevices.getUserMedia({video: true})
    .then(function(stream) {
        document.getElementById('camera').src = URL.createObjectURL(stream);
    }).catch(function() {
        alert('could not connect stream');
    });


});