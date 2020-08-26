import QtQuick 2.13
import QtQuick.Layouts 1.11
import QtQuick.Controls 2.4
import QtQuick.Controls.Material 2.4
import QtQuick.Controls.Universal 2.4
import QtCharts 2.2

ApplicationWindow {
  visible: true
  minimumHeight: 700
  minimumWidth: 1500
  Material.theme: Material[subTheme.currentText]
  Material.accent: Material[accentColor.currentText]
  Material.primary: Material[primaryColor.currentText]
  Universal.theme: Universal[subTheme.currentText]
  Universal.accent: Universal[accentColor.currentText]
  menuBar: MenuBar {
    Menu {
      title: '&File'
      Action { text: '&New...' }
      Action { text: '&Open...' }
      Action { text: '&Save' }
      Action { text: 'Save &As...' }
      MenuSeparator {}
      Action { text: '&Quit' }
    }
    Menu {
      title: '&Edit'
      Action { text: 'Cu&t' }
      Action { text: '&Copy' }
      Action { text: '&Paste' }
    }
    Menu {
      title: '&Help'
      Action { text: '&About' }
    }
  }

  Pane {
    padding: 10
    anchors.fill: parent
    GridLayout {
      anchors.fill: parent
      flow: GridLayout.TopToBottom
      rows: 3
      CellBox {
        Layout.rowSpan: 3; Layout.minimumWidth: 1000
        title: 'Login Data'
        ColumnLayout {
          // ScrollView will not work if we use ColumnLayout as
          // ColumnLayout always measures its size depending on its
          // contents.
          anchors.fill: parent
          //anchors.rightMargin: 25
          //anchors.leftMargin: 25
          spacing: 5
          TextField {
              id: loginTextField
              objectName: 'loginTextField'
              placeholderText: 'Login'
              selectByMouse: true
              font.pointSize: 15
              horizontalAlignment: Text.AlignHCenter
              text: ''
          }
          TextField {
              id: passwordTextField
              objectName: 'passwordTextField'
              placeholderText: 'Password'
              selectByMouse: true
              font.pointSize: 15
              horizontalAlignment: Text.AlignHCenter
              echoMode: TextInput.Password
              text: ''
          }
          CellBox {
          Layout.rowSpan: 3; Layout.minimumWidth: 1000
          title: 'Controlling'
            RowLayout {
              anchors.fill: parent
              //anchors.rightMargin: 25
              //anchors.leftMargin: 25
              spacing: 5
              Button {
                id: startButton
                objectName: 'startButton'
                text: "Start"
                down: true 
              }
              Button {
                id: stopButton
                objectName: 'stopButton'
                text: "Stop"
                down: true 
              }
            }
          }
        }
      }
    }
  }
  footer: RowLayout {
    width: parent.width
    RowLayout {
      Layout.margins: 10
      Layout.alignment: Qt.AlignHCenter
      Label { text: 'QtQuick Charts Themes: ' }
      ComboBox {
        id: qtquickChartsThemes
        model: [
          'ChartThemeLight', 'ChartThemeBlueCerulean',
          'ChartThemeDark', 'ChartThemeBrownSand',
          'ChartThemeBlueNcs', 'ChartThemeHighContrast',
          'ChartThemeBlueIcy', 'ChartThemeQt'
        ]
        Layout.fillWidth: true
      }
    }
    RowLayout {
      Layout.margins: 10
      Layout.alignment: Qt.AlignHCenter
      Label { text: 'QtQuick 2 Themes: ' }
      Label {
        id: qtquick2Themes
        objectName: 'qtquick2Themes'
        Layout.fillWidth: true
      }
    }
    RowLayout {
      Layout.margins: 10
      Layout.alignment: Qt.AlignHCenter
      Label { text: 'Sub-Theme: ' }
      ComboBox {
        id: subTheme
        model: ['Light', 'Dark']
        Layout.fillWidth: true
        enabled: qtquick2Themes.text == 'Material' || qtquick2Themes.text == 'Universal'
      }
    }
    RowLayout {
      property var materialColors: [
        'Red', 'Pink', 'Purple', 'DeepPurple', 'Indigo', 'Blue',
        'LightBlue', 'Cyan', 'Teal', 'Green', 'LightGreen', 'Lime',
        'Yello', 'Amber', 'Orange', 'DeepOrange', 'Brown', 'Grey',
        'BlueGrey'
      ]
      property var universalColors: [
        'Lime', 'Green', 'Emerald', 'Teal', 'Cyan', 'Cobalt',
        'Indigo', 'Violet', 'Pink', 'Magenta', 'Crimson', 'Red',
        'Orange', 'Amber', 'Yellow', 'Brown', 'Olive', 'Steel', 'Mauve',
        'Taupe'
      ]
      Layout.margins: 10
      Layout.alignment: Qt.AlignHCenter
      Label { text: 'Colors: ' }
      Label { text: 'Accent' }
      ComboBox {
        id: accentColor
        Layout.fillWidth: true
        enabled: qtquick2Themes.text == 'Material' || qtquick2Themes.text == 'Universal'
        model: {
          if (qtquick2Themes.text == 'Universal') return parent.universalColors
          return parent.materialColors
        }
      }
      Label { text: 'Primary' }
      ComboBox {
        id: primaryColor
        Layout.fillWidth: true
        enabled: qtquick2Themes.text == 'Material'
        model: parent.materialColors
      }
    }
  }
}