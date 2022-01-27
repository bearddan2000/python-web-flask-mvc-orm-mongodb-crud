if [ "$MONGO_INITDB_ROOT_USERNAME" ] && [ "$MONGO_INITDB_ROOT_PASSWORD" ]; then
  "${mongo[@]}" "$MONGO_INITDB_DATABASE" <<-EOJS
  db.createUser({
     user: $(_js_escape "$MONGO_INITDB_ROOT_USERNAME"),
     pwd: $(_js_escape "$MONGO_INITDB_ROOT_PASSWORD"),
     roles: [ "readWrite", "dbAdmin" ]
     })
  use $MONGO_INITDB_DATABASE
EOJS
fi
function import_json() {
  #statements
  local file=$1
  local collection=$1
  local path="/docker-entrypoint-initdb.d"

  mongoimport --host localhost --db $MONGO_INITDB_DATABASE --collection $collection --type json --file $path/${file}.json --jsonArray -u $MONGO_INITDB_ROOT_USERNAME -p $MONGO_INITDB_ROOT_PASSWORD

}

import_json "weapon"

echo ======================================================
echo created $MONGO_INITDB_ROOT_USERNAME in database $MONGO_INITDB_DATABASE
echo ======================================================
