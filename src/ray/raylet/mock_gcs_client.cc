#include "ray/raylet/mock_gcs_client.h"

namespace ray {

const std::unordered_set<ClientID, UniqueIDHasher> &ObjectTable::GetObjectClientIDs(const ray::ObjectID &object_id){
  if (client_lookup.count(object_id) > 0){
    return client_lookup[object_id];
  } else {
    return empty_set_;
  };
};

ray::Status ObjectTable::Add(const ObjectID &object_id, const ClientID &client_id){
  if (client_lookup.count(object_id) == 0){
    client_lookup[object_id] = std::unordered_set<ClientID, UniqueIDHasher>();
  } else if (client_lookup[object_id].count(client_id) != 0){
    return ray::Status::KeyError("ClientID already exists.");
  }
  client_lookup[object_id].insert(client_id);
  return ray::Status::OK();
};

ray::Status ObjectTable::Remove(const ObjectID &object_id, const ClientID &client_id){
  if (client_lookup.count(object_id) == 0){
    return ray::Status::KeyError("ObjectID doesn't exist.");
  } else if (client_lookup[object_id].count(client_id) == 0){
    return ray::Status::KeyError("ClientID doesn't exist.");
  }
  client_lookup[object_id].erase(client_id);
  return ray::Status::OK();
};


std::vector<ClientID> ClientTable::GetClientIds(){
  std::vector<ClientID> keys;
  keys.reserve(info_lookup.size());
  for(auto kv : info_lookup) {
    keys.push_back(kv.first);
  }
  return keys;
};

const ClientInformation &ClientTable::GetClientInformation(const ClientID &client_id){
  if (info_lookup.count(client_id) == 0){
    throw std::runtime_error("ClientID doesn't exist.");
  }
  return info_lookup.at(client_id);
}

ray::Status ClientTable::Add(const ClientID &client_id,
                             const std::string &ip,
                             ushort port){
  if (info_lookup.count(client_id) != 0){
    return ray::Status::KeyError("ClientID already exists.");
  }
  info_lookup.emplace(client_id, ClientInformation(client_id, ip, port));
  return ray::Status::OK();
};

ray::Status ClientTable::Remove(const ClientID &client_id){
  if (info_lookup.count(client_id) == 0){
    return ray::Status::KeyError("ClientID doesn't exist.");
  }
  info_lookup.erase(client_id);
  return ray::Status::OK();
};


ClientID GcsClient::Register(const std::string &ip, ushort port) {
  ClientID client_id = ClientID().from_random();
  client_table().Add(std::move(client_id), ip, port);
  return client_id;
};

ObjectTable &GcsClient::object_table(){
  return *object_table_;
};

ClientTable &GcsClient::client_table(){
  return *client_table_;
};

};
