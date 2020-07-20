
syntax = "proto2";
package infos;


message Person{
    required int32 age=2;
    required string name=3;
    enum PhoneType{
        MOBILE = 0;
        WORK = 1;
        HOME = 2;
    }
    message Score{
        required string object=1;
        optional int32 score = 2;
    }
    message PhoneNumber{
        required int32 phone=1;
        optional PhoneType type=2 [default = MOBILE];
    }
    repeated Score score=4;
    optional PhoneNumber number=5;
}
message one{
    required int32 id=1;
    required Person people =2;
}