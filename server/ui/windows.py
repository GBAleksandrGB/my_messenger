from PyQt6.QtWidgets import QMainWindow
from server.ui.server_monitor import Ui_ServerWindow as server_ui_class


class ServerMonitorWindow(QMainWindow):
    def __init__(self, parsed_args, server_instance, parent=None):
        super().__init__(parent)
        self.parsed_args = parsed_args
        self.server_instance = server_instance
        self.ui = server_ui_class()
        self.ui.setupUi(self)
        self.ui.refresh_action.triggered.connect(self.refresh_action)
        self.after_start()
    
    def after_start(self):
        self.update_clients()

    def update_clients(self):
        contacts = self.server_instance.get_all_clients()
        self.ui.clients_list.clear()
        self.ui.clients_list.addItems(
            [contact.username for contact in contacts])
        
    def refresh_action(self):
        """Refresh from menu"""

        print('refresh')
        self.update_clients()
    
    def closeEvent(self, Event):
        self.server_instance._cm.dal.session.close()
    
    def update_history_messages(self, username):
        """Get all events from client's history"""

        self.ui.msg_history_list.clear()
        msgs = self.server_instance.get_client_history(username)
        _resp = [m.time.strftime(
            "%Y-%m-%d %H:%M:%S") + '_' + m.ip_addr + '_' + m.client.username
                 for m in msgs]
        self.ui.msg_history_list.addItems(_resp)

    def on_clients_list_itemDoubleClicked(self):
        """Event, when double clicked on user in client's list -> 
        update history and go to history tab
        """
        
        selected_client = self.ui.clients_list.currentItem().text()
        self.update_history_messages(selected_client)
        self.ui.tabWidgetClients.setCurrentIndex(1)  # set history tab active
