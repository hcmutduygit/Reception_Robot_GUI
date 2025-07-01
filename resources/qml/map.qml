    import QtQuick 2.0
import QtPositioning 5.8
import QtLocation 5.8

Rectangle {
    id: window
    objectName: "rect"
    width: 1180
    height: 780
    visible: true


// Dữ liệu lấy từ Google
//    Nhà thi đấu 10.881583   106.805778  0

//    d1          10.881306   106.806194  1

//    d2          10.88060    106.80574   2

//    H3          10.88088    106.80530   3

//    d3          10.88022    106.80548   4

//    H2          10.88053    106.80501   5

//    d4          10.87959    106.80510   6

//    d5          10.87990    106.80461   7  x,y = 34.986099, -19.910474

//    H1          10.88006    106.80470   8  x,y = 44.825916, -2.212247

//    d6          10.87948    106.80527   9

//    H6          10.880000   106.805611  10

//    d7          10.880500   106.80592   11

//    d8          10.881194   106.806389  12

//    Trạm bus    10.88020    106.80637   13

//    Uniservice  10.88008    106.80429   14    x,y = 0 0

    // Dữ liệu lấy từ GPS
    //    Nhà thi đấu   0

    //    d1            1

    //    d2             2

    //    H3             3

    //    d3             4

    //    H2             5

    //    d4            10.87962  106.80507                6  x,y = 85.1731134, -51.1495568

    //    d5            10.87991  106.80458                7  x,y = 31.6668960, -18.9031224

    //    H1             8

    //    d6             10.87948 106.80528                9  x, y = 108.1043870, -66.7167797

    //    H6             10.87999 106.80563                10  x, y = 146.3228593, -10.0072204

    //    d7             11

    //    d8          12

    //    Trạm bus      13

    //    Uniservice  10.88008    106.80429                14 x,y = 0 0


//    property var nameList: ["0","1","2","3","4","5","6","7","8","9","10","11","12","13","14"]
//    property var lList: ["0","1","2","3","4","5","6","7","8","9","10","11","12","13","14"]
////  google
//   // property var latList: [10.881583,  10.881306,  10.880611,  10.88088,  10.88022,  10.88053, 10.87959, 10.87990, 10.88006, 10.87948, 10.880000, 10.880500, 10.881194, 10.88020, 10.88008]
//   // property var lonList: [106.805778, 106.806194, 106.805750, 106.80530, 106.80548, 106.80501,106.80510,106.80461,106.80470,106.80527,106.805611,106.80592, 106.806389,106.80637, 106.80429]
//    //  GPS                       0            1          2            3          4         5         6         7         8         9          10        11          12       13         14
//        property var latList: [10.881583,  10.881306,  10.880611,  10.88088,  10.88022,  10.88053, 10.87962, 10.87991, 10.88006, 10.87948, 10.87999, 10.880500, 10.881194, 10.88020, 10.88008]
//        property var lonList: [106.805778, 106.806194, 106.805750, 106.80530, 106.80548, 106.80501,106.80507,106.80458,106.80470,106.80528,106.80563,106.80592, 106.806389,106.80637, 106.80429]

//    property var location: ["Nhà Thi Đấu", "d1", "d2", "Tòa H3", "d3", "Tòa H2", "d4", "d5", "Tòa H1", "d6", "Tòa H6", "d7", "d8", "Trạm xe bus H6","UniService"]
//    property var edgeList: ["0,1", "1,0", "1,2","1,12","2,1","2,3","2,4","2,11","3,2","4,2","4,5","4,6","5,4","6,4","6,7","6,9","7,6","7,8","8,7","9,6","9,10","10,9","10,11","11,2","11,10","11,12","11,13","12,1","12,11","13,11","14,7"]

//==================================================================================================================================================================================================================================================================
    //    khu dân cư

                //                base 1                              base 2
//              base 1      10.904197   106.797314        0

//                  d1   10.904113  106.797607            1
//                  d1_  10.904472  106.797694            2   10.904113   106.797591
//                  d2   10.903993  106.797998            3
//                  d2_  10.90379   106.797932            4
//                  d3   10.903936  106.798193            5

//              base 2   10.903798 106.798681             6

    property var nameList: ["0","1","2","3","4","5","6"]
    property var lList: ["0","1","2","3","4","5","6"]
    //  GPS                       0            1          2            3          4            5           6
        property var latList: [10.904197 ,  10.904113,  10.904472,  10.903993,  10.90379,  10.903936 , 10.903798 ]
        property var lonList: [106.797314, 106.797591, 106.797694, 106.797998, 106.797932, 106.798193, 106.798681]

    property var location: ["Base 1", "d1","d1_", "d2","d2_", "d3", "Base 2"]
    property var edgeList: ["0,1", "1,0", "1,2","1,3","2,1","3,1","3,4","3,5","4,3","5,3","5,6","6,5"]


//    property var nameList: ["0","1","2","3","4","5","6","7","8","9"]
//    property var lList: ["0","1","2","3","4","5","6","7","8","9"]
//    property var latList: [10.880028, 10.880528, 10.880944, 10.881417,10.880000,10.77351,10.77373,10.77398,10.77462,10.77462]
//    property var lonList: [106.804667, 106.805000,106.805222, 106.806056,106.805611,106.65947,106.65929,106.65994,106.65959,106.65959]

//    property var location: ["Tòa H1", "d1", "Tòa H2", "d2", "Tòa H3", "d3","Nhà thi đấu BK","d4","Tòa H6","d5"]
//    property var edgeList: ["0,1", "1,0", "1,2", "2,1","2,3", "3,2"]

    property var location_indoor: ["Cổng thư viện C2", "dd1", "phòng công tác A1", "dd2", "BKfood cổng 1", "BKfood cổng 2", "Phòng xây dựng", "dd3", "Phòng sinh hoạt C1", "Phòng tự học C1","dd4"]
    property var location_indoor_x: []
    property var location_indoor_y: []
    property var latList_inddor: [10.77302,10.77273,10.77266,10.77353,10.77346,10.77366,10.77406,10.77469,10.77456,10.77491,10.77478]
    property var lonList_indoor: [106.66008,106.66022,106.66007,106.65889,106.65875,106.65878,106.65856,106.65955,106.65929,106.65945,106.65918]
    property var location_indoor_list: ["0","1","2","3","4","5","6","7","8","9","10"]
    property var location_indoor_llist: ["0","2","4","5","6","8","9"]

    function updateRealPath(point) {
        realPath.addCoordinate(point)
        target_marker.coordinate = point
        target_marker.visible = true
    }

    function createDesiredPath(point) {
        desiredPath.addCoordinate(point)
//        for (var i = 0; i < pointList.length; i++) {
//            desiredPath.addCoordinate(pointList[i])
//        }
    }

    function clearRealPath() {
        realPath.path = []
    }

    Plugin {
        id: mapPlugin
        name: 'osm'
        PluginParameter {
            name: 'osm.mapping.custom.host'
            value: 'qrc:/maps/bachkhoa.osm.pdf'
        }
        PluginParameter {
            name: 'osm.mapping.providersrepository.disabled'
            value: true
        }
    }

    Map {
        id: mapView
        anchors.fill: parent
        activeMapType: mapView.supportedMapTypes[1]
        center: QtPositioning.coordinate(10.903993, 106.797998)
        zoomLevel: maximumZoomLevel
        rotation: 0
        plugin: mapPlugin

        gesture.enabled: true
        gesture.acceptedGestures: MapGestureArea.PinchGesture | MapGestureArea.PanGesture

        MapPolyline {
            id: realPath
            line.width: 3
            line.color: 'red'
        }

        MapPolyline {
            id: desiredPath
//            objectName: 'desiredPath'
            line.width: 3
            line.color: 'blue'
//            path:[QtPositioning.coordinate(10.7725199382, 106.658854267),
//                QtPositioning.coordinate(10.7729817708, 106.659619141),
//                QtPositioning.coordinate(10.7726765951, 106.659814453)]

        }

//        MapPolyline {
//            id: cubePath
////            objectName: 'cubePath'
//            line.width: 3
//            line.color: 'green'
//            path:[QtPositioning.coordinate(10.7725524902, 106.658837891),
//                QtPositioning.coordinate(10.7730041504, 106.659651693),
//                QtPositioning.coordinate(10.7726338704, 106.659847005),
//                QtPositioning.coordinate(10.7722066243, 106.659098307),
//            QtPositioning.coordinate(10.7725524902, 106.658837891)]

//        }

        MapQuickItem {
            id: target_marker
            coordinate: QtPositioning.coordinate(0, 0)
            anchorPoint.x: target_marker_image.width / 2
            anchorPoint.y: target_marker_image.height
            sourceItem: Image{
                id: target_marker_image
                source: 'qrc:/images/markers/marker2.png'
            }
            visible: false
        }

        MouseArea {
            id: mouseArea
            anchors.fill: parent
            acceptedButtons: Qt.LeftButton | Qt.RightButton
//            pressAndHoldInterval: 200

            onDoubleClicked: {
                var mouseGeoPos = mapView.toCoordinate(Qt.point(mouse.x, mouse.y));
                var preZoomPoint = mapView.fromCoordinate(mouseGeoPos, false);
                if (mouse.button === Qt.LeftButton) {
                    mapView.zoomLevel = Math.floor(mapView.zoomLevel + 1)
                } else if (mouse.button === Qt.RightButton) {
                    mapView.zoomLevel = Math.floor(mapView.zoomLevel - 1)
                }
                var postZoomPoint = mapView.fromCoordinate(mouseGeoPos, false);
                var dx = postZoomPoint.x - preZoomPoint.x;
                var dy = postZoomPoint.y - preZoomPoint.y;

                var mapCenterPoint = Qt.point(mapView.width / 2.0 + dx, mapView.height / 2.0 + dy);
                mapView.center = mapView.toCoordinate(mapCenterPoint);
            }
        }

        Component.onCompleted: {
            for (var i = 0; i < nameList.length; i++) {
                var name = nameList[i];
                if (lList.indexOf(name) !== -1) {
                    var component = Qt.createComponent("Marker_outdoor.qml").createObject(mapView)
                    component.coordinate = QtPositioning.coordinate(latList[i], lonList[i])
                    component.name = location[i]
                    mapView.addMapItem(component)
                }
           }
            for (var ii = 0; ii < location_indoor_list.length; ii++) {
                name = location_indoor_list[ii];
                if (location_indoor_llist.indexOf(name) !== -1) {
                    var component = Qt.createComponent("Marker_indoor.qml").createObject(mapView)
                    component.coordinate = QtPositioning.coordinate(latList_inddor[ii], lonList_indoor[ii])
                    component.name = location_indoor[ii]
                    mapView.addMapItem(component)
                }
           }
        }
    }
}
