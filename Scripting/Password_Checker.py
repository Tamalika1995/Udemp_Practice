import requests
import hashlib
import sys
def request_api_data(query_char):
    url='https://api.pwnedpasswords.com/range/'+query_char
    res=requests.get(url)
    #print(res)
    if res.status_code!=200:
        raise RuntimeError(f'error fetching {res.status_code} please check the api and try again')
    return res
def read_response(response):
    print(response.text)
def pwned_api_check(password):
    #print(str(password).encode('utf-8'))
    sha1password=hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    #print(sha1password)
    firstfive_char,tail=sha1password[:5],sha1password[5:]
    response=request_api_data(firstfive_char)
    #print(firstfive_char)
    #print(tail)
    #print(read_response(response))
    return password_leaks_count(response,tail)
def password_leaks_count(hashes,hash_to_check):
    hashes=(line.split(':') for line in hashes.text.splitlines())
    for h,count in hashes:
        if h==hash_to_check:
            #print(h)
            #print(hash_to_check)
            return count
    return 0
def main(args):
    for i in args:
        count=pwned_api_check(i)
        if count:
            print(f'ur {i} found {count} times... you should chnage it')
        else:
            print(f'{i} not found.. happy going')
    return 'done'
if __name__=='__main__':

    sys.exit(main(sys.argv[1:]))
