import { MongoClient } from 'mongodb';
async function main() {
    try {
        const uri = "mongodb+srv://root:r00tUser@cluster0-zbhfi.mongodb.net/DnDDatabase?retryWrites=true&w=majority";
        const client = new MongoClient(uri);
        await client.connect();
        await listDatabases(client);

    } catch (e) {
        console.error(e);
    }
    finally {
        await client.close();
    }
}
main().catch(console.error);