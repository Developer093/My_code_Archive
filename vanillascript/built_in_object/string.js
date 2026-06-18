/**
 * sting 객체는 문자열을 나타내는 빌트인 객체입니다.
 * 
 * 사용법 >> 변수명.메서드()
 *          문자열.메서드()
 */
    // 1. length : 문자열의 길이를 반환
    // How to use >> 문자열.length

    const str_1 = "Hello, World!";
    console.log(str_1.length); 

    // 2. toUpperCase() : 문자열을 대문자로 변환
    // How to use >> 문자열.toUpperCase()

    const str_2 = "kimsangwon";
    console.log(str_2.toUpperCase());

    // 3. toLowerCase() : 문자열을 소문자로 변환
    // How to use >> 문자열.toLowerCase()

    const str_3 = "PENPINEAPPLE,APPLEPEN";
    console.log(str_3.toLowerCase());

    // 4. include() : 문자열이 특정 문자열을 포함하는지 여부를 반환
    // How to use >> 문자열.include("찾을 문자열")

    const str_4 = "javascript is intersting";
    console.log(str_4.includes("java"));

    // 5. slice() : 문자열의 일부를 추출하여 새로운 문자열을 반환
    // How to use >> 문자열.slice(시작 인덱스, 끝 인덱스)

    const text = "javascript is funny";
    console.log(text.slice(0, 4));

    // 6. replace() : 문자열의 일부를 다른 문자열로 대체
    // How to use >> 문자열.replace("바꿀 문자열", "새로운 문자열")

    const text_2 = "python is easy";
    console.log(text_2.replace('python', 'javascript'));

    // 7. indexOf() >> 문자열이 처음 나타나는 위치를 알려줌
    // How to use >> 문자열.indexOf("문자열")

    const text_3 = "vanilla is funny";
    console.log(text_3.indexOf("funny"));

    // 8. lastIndexOf() >> 문자열을 뒤에서 부터 찾아서 마지막으로 발견된 위치를 반환하는 메서드
    // How to use >> 문자열.lastIndexOf()

    const text_4 = "I'm Korean";
    console.log(text_4.lastIndexOf("K"));
