import serial
import time
from serial import STOPBITS_ONE, PARITY_NONE, EIGHTBITS  # 修正常量名称


def control_laser(com_port='COM7', baudrate=115200):
    try:
        ser = serial.Serial(
            port=com_port,
            baudrate=baudrate,
            timeout=1,
            parity=PARITY_NONE,
            stopbits=STOPBITS_ONE,  # 使用修正后的常量
            bytesize=EIGHTBITS
        )

        if not ser.is_open:
            ser.open()
        print(f"已打开串口: {com_port}")
        print("输入 'Y' 开启激光，'N' 关闭激光，输入 'Q' 退出程序")

        while True:
            user_input = input("请输入指令 (Y/N/Q): ").strip().upper()

            if user_input == 'Q':
                print("退出程序")
                break
            elif user_input in ['Y', 'N']:
                ser.write(user_input.encode('utf-8'))
                print(f"已发送指令: {user_input}")
                time.sleep(0.1)
            else:
                print("无效指令，请输入 'Y'、'N' 或 'Q'")

    except serial.SerialException as e:
        print(f"串口错误: {e}")
    except Exception as e:
        print(f"发生错误: {e}")
    finally:
        if 'ser' in locals() and ser.is_open:
            ser.close()
            print("串口已关闭")


if __name__ == "__main__":
    control_laser(com_port='COM7')
