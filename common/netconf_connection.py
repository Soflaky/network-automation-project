from ncclient import manager
DEVICE = {
"host": "192.168.56.101",
"port": 830,
"username": "admin",
"password": "admin"
}
def connect_device():
"""
Shared NETCONF connection function.
Other members can import this function in their scripts.
"""
return manager.connect(
host=DEVICE["host"],
port=DEVICE["port"],
username=DEVICE["username"],
password=DEVICE["password"],
hostkey_verify=False,
device_params={"name": "csr"},
allow_agent=False,
look_for_keys=False,
timeout=30
)
def test_connection():
try:
with connect_device() as m:
print("NETCONF connection successful.")
print("Device capabilities retrieved successfully.")
print("\nFirst 5 server capabilities:")
for capability in list(m.server_capabilities)[:5]:
print("-", capability)
except Exception as error:
print("NETCONF connection failed.")
print("Error:", error)
if __name__ == "__main__":
test_connection()
