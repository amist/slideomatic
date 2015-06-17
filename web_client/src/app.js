var myApp = angular.module('myApp', [])
myApp.controller('myController', function($scope) {
    var slide =  function(){
        this.title = '';
    this.content = ''}

    $scope.slides = [new slide()]  ;

    $scope.add_slide = function(){

        $scope.slides.push(new slide())
        $scope.$apply()
    }

    $scope.remove_slide = function(slide_index){

        $scope.slides.splice(slide_index, 1);
        $scope.$apply()
    }

    $scope.apply = function() {
        alert("generating your slides ......")
        alert('slides are '+ JSON.stringify($scope.slides))
    }


    }   )
