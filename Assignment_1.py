size = 3
client_list = [None] * 3

def add_client():
    client_id = int(input("Client ID : ")
    name = input("Client Name : ")
    telephone = input("Client Telephone number : ")
    client_details = [client_id, name, telephone]

    index = client_id % size

    for i in range(size):
        if client_list[index] == None:
            client_list[index] = client_details
            print("Adding Data ", index, client_details
            break
        else:
            index = (index + 1) % size

def search_client():
    client_id = int(input("Client ID : ")
    index = client_id % size
    for i in range(size):
        if client_list[index] != None:
            if client_list[index][0] == client_id:
                print("Client found at index ,index, client_list[index]")
                break
            index = (index + 1) % size    
        else:
            print("Element not found")

def delete_client():
    client_id = int(input("Client ID : ")
    index = client_id % size
    for i in range(size):
        if client_list[index] != None:
            if client_list[index][0] == client_id:
                client_list[index] = None
                print("Client deleted")
                break
            index = (index + 1) % size
        else:
            print("Element not found")

add_client()
add_client()
add_client()
print("Search Client")
search_client()
print("Delete Client")
delete_client()
print("Search Client")
search_client()
            