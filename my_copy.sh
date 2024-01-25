
SOURCE_DIR=$1
DEST_DIR=$2
mkdir -p "$DEST_DIR"
cp -R "$SOURCE_DIR/"* "$DEST_DIR"
echo "Files copied from $SOURCE_DIR to $DEST_DIR."

