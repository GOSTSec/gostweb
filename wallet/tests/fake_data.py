from decimal import Decimal

DEMO_TRANSACTIONS = [
    {
        'txid': '3c03439fab4f53c97185e66217fe5fe61cdc4e80b25dfe5a0d19bf0b8c77f994',
        'blocktime': 1491951914,
        'blockindex': 1,
        'timereceived': 1491951811,
        'category': 'receive',
        'time': 1491951811,
        'blockhash': '0000004d184d3df898180937bd22c2717543706443b33ec7e16e369fa9d8c334',
        'amount': Decimal('616.00000000'),
        'account': '',
        'confirmations': 6238,
        'address': 'GXaNvzURu4fRAkjSodybjcXnwwUPKxB6rQ'
    }, 
    {
        'txid': '62abf6d27ea48937e2979948012b353bf0710c2df91b0d7c63c5cdeba034b835',
        'time': 1492013400,
        'timereceived': 1492013400,
        'confirmations': 5453,
        'account': '',
        'fee': Decimal('0E-8'),
        'blockindex': 1,
        'category': 'send',
        'blockhash': '00000018021fcb42490ab49053994ddb71f9316278625ec1d3d8119d98a18333',
        'amount': Decimal('-616.00000000'),
        'blocktime': 1492013470,
        'address': 'GWAYdECe4rQfrjyynHHNx72FqGCoxSW939'
    },

    {
        'txid': 'a94b83eec4f267aa503cc9ec65a229350cae60799ff73c28283a7aa5dad15435',
        'blocktime': 1492779489,
        'blockindex': 1,
        'timereceived': 1492779203,
        'category': 'receive',
        'time': 1492779203,
        'blockhash': '000000060161934be4eeb7670c8ab004306e9bc5333fa0fb560d597a3220fc97',
        'amount': Decimal('1.00000000'),
        'account': '',
        'confirmations': 1134,
        'address': 'GHwVSdza9QB5zPa9kZWjFdByynTAtDb6M9'
    },
    {
        'txid': 'a94b83eec4f267aa503cc9ec65a229350cae60799ff73c28283a7aa5dad15435',
        'blocktime': 1492779489,
        'blockindex': 1,
        'timereceived': 1492779203,
        'category': 'receive',
        'time': 1492779203,
        'blockhash': '000000060161934be4eeb7670c8ab004306e9bc5333fa0fb560d597a3220fc97',
        'amount': Decimal('1.00000000'),
        'account': '',
        'confirmations': 1134,
        'address': 'GHwVSdza9QB5zPa9kZWjFdByynTAtD0000'
    },
    {
        'txid': 'a94b83eec4f267aa503cc9ec65a229350cae60799ff73c28283a7aa5dad15435',
        'time': 1492779203,
        'timereceived': 1492779203,
        'confirmations': 1134,
        'account': '',
        'fee': Decimal('0E-8'),
        'blockindex': 1,
        'category': 'send',
        'blockhash': '000000060161934be4eeb7670c8ab004306e9bc5333fa0fb560d597a3220fc97',
        'amount': Decimal('-1.00000000'),
        'blocktime': 1492779489,
        'address': 'GHwVSdza9QB5zPa9kZWjFdByynTAtDb6M9'
    }
]

DEMO_UNSPENT = [
    {'address': 'GdNgGq9S78N1nr5HMyKPmHoFTnPqt5PXAU', 'vout': 1, 'txid': '16c0d08bf53e9c132a8522cca2544d53fe4389167329731f7f9645963f92d595', 'scriptPubKey': '76a914d63b7a8ba4f33cbd2f723c6ba68449166630472188ac', 'amount': Decimal('4.00000000'), 'confirmations': 904}, 
    {'address': 'GQtF5PvK4WRdAjMKjXCSmrqDbUEXz6W7z5', 'vout': 1, 'txid': '192b1cabf1b199909da44678daf0e4fac3559cd8e0c222c24ec86a9609decf84', 'scriptPubKey': '76a9144d3949f0f4207438acbb1c71177b0bb42bda614088ac', 'amount': Decimal('0.99800000'), 'confirmations': 889}, 
    {'address': 'GQ5V5DKrAo1QWoEpPLWfbwrbY55jqGFsCN', 'vout': 0, 'txid': '1e2f148fd3655fae34459791d7127afca31ac87d16af737eb9410f656ce56588', 'scriptPubKey': '76a91444616c30428e6c1581d899fc276e5205e61381c788ac', 'amount': Decimal('0.07000000'), 'confirmations': 803}, 
    {'address': 'GcKiTtJ1BL5ddZJZEqL6Q3Ax52k5MYhebm', 'account': '', 'vout': 1, 'txid': '1e2f148fd3655fae34459791d7127afca31ac87d16af737eb9410f656ce56588', 'scriptPubKey': '76a914cab3ef02db6ebf0d17f29e6ebfa43e94da58c4db88ac', 'amount': Decimal('2.00000000'), 'confirmations': 803}, 
    {'address': 'GepEjzLppwxsft6KSrT8poBRKhkeaT8pvw', 'vout': 1, 'txid': '3190ed2a9be245fc80505a0f46054009821af64865edd85bfe52bd9e9dc85e97', 'scriptPubKey': '76a914e6091b4d99fb48e261e1c965025d15200b55b0f788ac', 'amount': Decimal('200.90000000'), 'confirmations': 1297}, 
    {'address': 'GRKtS8H84k6Ta9rH1GbxtJkCgh3unSsWyY', 'vout': 1, 'txid': '476aca8593d4a292a1d08a9872b8736c54a1867a3b4394c841aa56752f6b9edd', 'scriptPubKey': '76a9145212df4dcd2e9cf805fc7c8db1cced27f06fc8cd88ac', 'amount': Decimal('4.00000000'), 'confirmations': 904}, 
    {'address': 'GZr7csPKkJhCs7Ybk6V4RjQnGDiwe7SjNG', 'account': '', 'vout': 0, 'txid': '529c78221fd9f8f88eb8e57c71afb8c5ae80255fa943c2aea24d43669f8d51c4', 'scriptPubKey': '76a914af8b5d2729e6736ed876571af8c06cc3c9c52ee888ac', 'amount': Decimal('10.00000000'), 'confirmations': 1294}, 
    {'address': 'GcKiTtJ1BL5ddZJZEqL6Q3Ax52k5MYhebm', 'account': '', 'vout': 0, 'txid': '586bd540f917f5472feee45d709554183395dd350b6ce76e4654534a4be28cf1', 'scriptPubKey': '76a914cab3ef02db6ebf0d17f29e6ebfa43e94da58c4db88ac', 'amount': Decimal('2.00000000'), 'confirmations': 803}, 
    {'address': 'GXa6TrdAHMMnKZY8UC1ACXq41LqLomsnrX', 'vout': 1, 'txid': '586bd540f917f5472feee45d709554183395dd350b6ce76e4654534a4be28cf1', 'scriptPubKey': '76a91496937e10d514abce8df94a8c024491f8a25e8ea388ac', 'amount': Decimal('0.01200000'), 'confirmations': 803}, 
    {'address': 'GU9HLpYFErjnVGsgnpwUiCsakk8uApLSFk', 'account': '', 'vout': 0, 'txid': 'c76350792f44c4d8a0fbc499ed7090ed67cbd2ecb490faffde1e1c0c1f62838d', 'scriptPubKey': '76a91470f9cc102e2807ad439531abe07601b0e97ec82188ac', 'amount': Decimal('22.16000000'), 'confirmations': 397}, 
    {'address': 'GPFEKc6dsUbTJBWGCDmtwdB1DDhhdBAsue', 'account': '', 'vout': 0, 'txid': 'd3c7dd35d371312443327fc66982092f96ac612272aa4d66fdf01f653e4e85e1', 'scriptPubKey': '76a9143b4124688a92cd772e787a305e7282409ca6cf2388ac', 'amount': Decimal('2.00000000'), 'confirmations': 887}
 ]

DEMO_DATA_1 = {
    "listunspent": [{'address': 'GJS2ua47eTe19eBtCdjKuYdMUSJ6uZP8wL', 'txid': '71ea479aca93b1fb6f44b2081c711b54b1261711462ab6b7121b39763b19f328', 'account': '', 'amount': Decimal('30.00000000'), 'scriptPubKey': '76a91406738f84bdd0b95764154de9ed66976f3a76bb1288ac', 'vout': 1, 'confirmations': 2492}, {'address': 'GXpJEiv2koV4RxbpgHWtAHrPXKABPVtQ7x', 'txid': '286d116d918345a1a737f991f686a8a869126fefdd5db74de94ffdc6e68cd198', 'account': '', 'amount': Decimal('19.16000000'), 'scriptPubKey': '76a914994324dc98a6561b9dc8889c9dce6bf2cde8e85288ac', 'vout': 0, 'confirmations': 2267}, {'address': 'GZagQvQJcKLhEp5rkuXrEXMLGp1KLUjUQs', 'txid': '71ea479aca93b1fb6f44b2081c711b54b1261711462ab6b7121b39763b19f328', 'account': '', 'amount': Decimal('7.99800000'), 'scriptPubKey': '76a914aca0156313983bbc9a9f80fdc7435f483dedbb4588ac', 'vout': 0, 'confirmations': 2492}, {'address': 'GZagQvQJcKLhEp5rkuXrEXMLGp1KLUjUQs', 'txid': 'a8cf18264fce1adceb2e85b183373054d193659d9b5c8ae78b0930c5f41676c4', 'account': '', 'amount': Decimal('1859.99800000'), 'scriptPubKey': '76a914aca0156313983bbc9a9f80fdc7435f483dedbb4588ac', 'vout': 0, 'confirmations': 8}, {'address': 'GPFEKc6dsUbTJBWGCDmtwdB1DDhhdBAsue', 'txid': 'd3c7dd35d371312443327fc66982092f96ac612272aa4d66fdf01f653e4e85e1', 'account': '', 'amount': Decimal('2.00000000'), 'scriptPubKey': '76a9143b4124688a92cd772e787a305e7282409ca6cf2388ac', 'vout': 0, 'confirmations': 5356}, {'address': 'GcKiTtJ1BL5ddZJZEqL6Q3Ax52k5MYhebm', 'txid': '1e2f148fd3655fae34459791d7127afca31ac87d16af737eb9410f656ce56588', 'account': '', 'amount': Decimal('2.00000000'), 'scriptPubKey': '76a914cab3ef02db6ebf0d17f29e6ebfa43e94da58c4db88ac', 'vout': 1, 'confirmations': 5272}, {'address': 'GcKiTtJ1BL5ddZJZEqL6Q3Ax52k5MYhebm', 'txid': '586bd540f917f5472feee45d709554183395dd350b6ce76e4654534a4be28cf1', 'account': '', 'amount': Decimal('2.00000000'), 'scriptPubKey': '76a914cab3ef02db6ebf0d17f29e6ebfa43e94da58c4db88ac', 'vout': 0, 'confirmations': 5272}, {'address': 'GQtF5PvK4WRdAjMKjXCSmrqDbUEXz6W7z5', 'txid': '192b1cabf1b199909da44678daf0e4fac3559cd8e0c222c24ec86a9609decf84', 'confirmations': 5358, 'amount': Decimal('0.99800000'), 'scriptPubKey': '76a9144d3949f0f4207438acbb1c71177b0bb42bda614088ac', 'vout': 1}, {'address': 'GQ5V5DKrAo1QWoEpPLWfbwrbY55jqGFsCN', 'txid': '1e2f148fd3655fae34459791d7127afca31ac87d16af737eb9410f656ce56588', 'confirmations': 5272, 'amount': Decimal('0.07000000'), 'scriptPubKey': '76a91444616c30428e6c1581d899fc276e5205e61381c788ac', 'vout': 0}, {'address': 'GJS2ua47eTe19eBtCdjKuYdMUSJ6uZP8wL', 'txid': 'a8cf18264fce1adceb2e85b183373054d193659d9b5c8ae78b0930c5f41676c4', 'account': '', 'amount': Decimal('30.00000000'), 'scriptPubKey': '76a91406738f84bdd0b95764154de9ed66976f3a76bb1288ac', 'vout': 1, 'confirmations': 8}, {'address': 'GXa6TrdAHMMnKZY8UC1ACXq41LqLomsnrX', 'txid': '586bd540f917f5472feee45d709554183395dd350b6ce76e4654534a4be28cf1', 'confirmations': 5272, 'amount': Decimal('0.01200000'), 'scriptPubKey': '76a91496937e10d514abce8df94a8c024491f8a25e8ea388ac', 'vout': 1}],
    "createrawtransaction": "010000000228f3193b76391b12b7b62a46111726b1541b711c08b2446ffbb193ca9a47ea710100000000ffffffff98d18ce6c6fd4fe94db75dddef6f1269a8a886f691f937a7a14583916d116d280000000000ffffffff02c0c93072000000001976a914aca0156313983bbc9a9f80fdc7435f483dedbb4588ac005ed0b2000000001976a91406738f84bdd0b95764154de9ed66976f3a76bb1288ac00000000",
    "signrawtransaction": {'complete': True, 'hex': '010000000228f3193b76391b12b7b62a46111726b1541b711c08b2446ffbb193ca9a47ea71010000006b483045022100ee57ecd2d136ac6bba120db2c4ded470d66e7b1f1f550186a795a847d5c499a20220188847e8a1df6d68aa202203a126ddac4d6b6f0d20afef7ea37fc3af29b6c879012103ce84ad18c5997fc1ffd7ef124bd39f7c7fa201ab42fc86daafa43067491a0d6bffffffff98d18ce6c6fd4fe94db75dddef6f1269a8a886f691f937a7a14583916d116d28000000006b483045022038d44f3f3b299ed7838d3d53dc597b9e96fe47e6b691d1d61805be226ddc2ee0022100d5ea3855d88cd3cc762251956f2cfee7e8f1def8df3f4feb88fd17a8e7696de5012103821021c870844de0661765569edfbf617fc5122217c86e0e98fac8326f00dbfcffffffff02c0c93072000000001976a914aca0156313983bbc9a9f80fdc7435f483dedbb4588ac005ed0b2000000001976a91406738f84bdd0b95764154de9ed66976f3a76bb1288ac00000000'},
    "sendrawtransaction": "71ea479aca93b1fb6f44b2081c711b54b1261711462ab6b7121b39763b19f328"
        }
