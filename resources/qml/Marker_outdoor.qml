import QtLocation 5.8
import QtPositioning 5.8
import QtQuick 2.0
MapQuickItem {
    property string name: ""

    visible: true
    coordinate: QtPositioning.coordinate(0.0, 0.0)
    anchorPoint.x: iconID.width / 2
    anchorPoint.y: iconID.height * 1.8

    sourceItem: Column {
        Text {
            id: nameID
            text: name
            color: 'deepskyblue'
            font.bold: true
        }
        Image {
            id: iconID
            source: 'qrc:/images/markers/marker.png'
        }
    }
}



