var myApp = angular.module('myApp', [])
myApp.controller('myController', function($scope) {
    var slide =  function(num){this.num = num;
        this.title = '';
    this.content = ''}

    $scope.slides = [new slide(1)]  ;

    $scope.add_slide = function(){

        $scope.slides.push(new slide($scope.slides.length +1))
        $scope.$apply()
    }


    $scope.apply = function() {
        alert("generating your slides ......")
        alert('slides are '+ JSON.stringify($scope.slides))
    }


    }   )
