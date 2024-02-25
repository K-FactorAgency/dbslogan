import requests
import json

def generate_slogan(target_customer, product_description):
    # 네이버 하이퍼클로바 API 키
    api_key = "YOUR_API_KEY"

    # API 요청 URL
    url = "https://api.naver.com/v1/hyperclova/clova.ai/language/generate"

    # API 요청 헤더
    headers = {
        "Authorization": "Bearer " + api_key,
        "Content-Type": "application/json"
    }

    # API 요청 본문
    body = {
        "query": {
            "target_customer": target_customer,
            "product_description": product_description
        }
    }

    # API 요청
    response = requests.post(url, headers=headers, data=json.dumps(body))

    # API 응답 처리
    if response.status_code == 200:
        # 응답 본문 추출
        response_body = json.loads(response.content)

        # 마케팅 슬로건 추출
        slogan = response_body["result"]["slogan"]

        return slogan
    else:
        # API 요청 오류 처리
        raise Exception("API 요청 오류: " + str(response.status_code))

# 사용자가 입력한 타겟 고객과 제품 소개를 받아 마케팅 슬로건을 생성
def main():
    target_customer = input("타겟 고객: ")
    product_description = input("제품 소개: ")

    slogan = generate_slogan(target_customer, product_description)

    print("마케팅 슬로건: " + slogan)

# main 함수 실행
if __name__ == "__main__":
    main()
