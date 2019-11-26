angular.module("mainpage")
    .controller("mainCtrl", function ($scope, $interval, $rootScope, $state, mainpageHttpRequest) {
        var initialize = function () {
            $scope.want_to_enter_text = true;
            $rootScope.is_loading = false;
            $scope.new_ocean_data = {
                "personal_text": ""
            };

        };
        $scope.predict = function () {
            $rootScope.is_loading = true;
            mainpageHttpRequest.perform_process($scope.new_ocean_data)
                .then(function (data) {
                    $rootScope.is_loading = false;
                    var response = data['response_code'];
                    if (response === 200) {
                        $scope.ocean_data = data['ocean'];
                        $scope.want_to_enter_text = false;
                    }
                }, function (error) {
                    console.log(error);
                });
        };

        initialize();

    });